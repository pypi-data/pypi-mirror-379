import argparse
import asyncio
import csv
import io
import json
import logging
import logging.handlers
import math
import multiprocessing
import sys
import time
from queue import Empty

import psutil
import streamlit as st
from streamlit_local_storage import LocalStorage

from ljobx.api.proxy.proxy_manager import ProxyManager
from ljobx.core.config import config
from ljobx.core.config_loader import ConfigLoader
from ljobx.core.scraper import run_scraper
from ljobx.utils.const import FILTERS
from ljobx.utils.logger import QueueLogHandler, configure_logging

st.set_page_config(page_title="ljobx | LinkedIn Job Extractor", page_icon="🔎", layout="centered")
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2.3rem;
        }
        .stElementContainer hr {
            display: none !important;
        }
        div.stCode {
            max-height: 300px;
            overflow-y: auto;
        }
        .st-emotion-cache-1w723zb {
            max-width: 936px
        }
    </style>
    """, unsafe_allow_html=True)


# --- Helper functions ---

def _flatten_dict(d: dict, parent_key: str = '', sep: str = '_') -> dict:
    """Flattens a nested dictionary."""
    items = {}
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, dict):
            items.update(_flatten_dict(v, new_key, sep=sep))
        else:
            items[new_key] = str(v).strip().replace("\n", "; ") if v is not None else ""
    return items

def generate_csv_data(results: list) -> bytes:
    """Generates a CSV byte string from results for download."""
    if not results:
        return b""

    flat_results = [_flatten_dict(res) for res in results]
    all_keys = set(key for res in flat_results for key in res.keys())
    all_keys.discard('recruiter')

    preferred_order = [
        'job_id', 'title', 'company', 'location', 'posted_date', 'applicants',
        'salary_range', 'apply_url', 'apply_is_easy_apply', 'recruiter_name',
        'recruiter_title', 'recruiter_profile_url', 'description'
    ]

    ordered_keys = [key for key in preferred_order if key in all_keys]
    remaining_keys = sorted(list(all_keys - set(ordered_keys)))
    final_ordered_keys = ordered_keys + remaining_keys

    overrides = {
        "apply_is_easy_apply": "EASY_APPLY",
        "recruiter_profile_url": "RECRUITER_PROFILE",
    }
    final_headers = [overrides.get(h, h.upper()) for h in final_ordered_keys]

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(final_headers)
    for res in flat_results:
        row = [res.get(key, "") for key in final_ordered_keys]
        writer.writerow(row)

    return output.getvalue().encode("utf-8-sig")

def run_scraper_in_process(results_q, log_q, progress_q, _search_criteria, _scraper_settings, _log_level):
    """Target function for the scraper process."""
    configure_logging(_log_level.upper())
    root_logger = logging.getLogger()
    root_logger.handlers = []

    log_format = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s", "%H:%M:%S")

    # Add QueueHandler to send logs back to the UI
    log_handler_queue = QueueLogHandler(log_q)
    log_handler_queue.setFormatter(log_format)
    root_logger.addHandler(log_handler_queue)

    file_handler = logging.handlers.RotatingFileHandler(
        filename=config.LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=3, encoding='utf-8'
    )
    file_handler.setFormatter(log_format)
    root_logger.addHandler(file_handler)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        logging.info("Scraper process started...")
        results = loop.run_until_complete(run_scraper(search_criteria=_search_criteria, progress_queue=progress_q, **_scraper_settings))
        results_q.put(results)
        logging.info("Scraper process finished.")
    except Exception as e:
        logging.error(f"Scraper process failed: {e}", exc_info=True)
        results_q.put(e)
    finally:
        loop.close()

def handle_proxy_upload():
    """Reads an uploaded proxy file and updates the session state."""
    if st.session_state.proxy_uploader is not None:
        st.session_state.proxy_config_content = st.session_state.proxy_uploader.read().decode("utf-8")
        st.session_state.just_uploaded_proxy = True
        st.session_state.using_default_proxy = False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--basic", action="store_true")
    parser.add_argument("--concurrency", type=int, default=None)
    parser.add_argument("--delay", type=int, nargs=2, default=None)
    parser.add_argument("--log-level", type=str, default=None)

    args, _ = parser.parse_known_args(sys.argv[1:])
    basic_mode = args.basic
    local_storage = LocalStorage()

    if 'app_initialized' not in st.session_state:
        initial_state = local_storage.getItem("form_inputs")
        initial_state = json.loads(initial_state) if isinstance(initial_state, str) else initial_state or {}

        # noinspection PyUnusedLocal
        final_proxy_content = None
        using_default = False
        default_content_on_disk = None

        if config.DEFAULT_PROXY_CONFIG_PATH.exists():
            # noinspection PyBroadException
            try:
                default_content_on_disk = config.DEFAULT_PROXY_CONFIG_PATH.read_text()
            except Exception:
                pass

        if basic_mode:
            # In basic mode, ALWAYS prioritize the default system config file.
            final_proxy_content = default_content_on_disk
            using_default = True if final_proxy_content else False
        else:
            # In advanced mode, load from browser storage first, then fall back to default.
            proxy_from_storage = initial_state.get("proxy_config_content")
            if proxy_from_storage:
                final_proxy_content = proxy_from_storage
                if proxy_from_storage == default_content_on_disk:
                    using_default = True
            else:
                final_proxy_content = default_content_on_disk
                using_default = True if final_proxy_content else False

        st.session_state.proxy_config_content = final_proxy_content
        st.session_state.using_default_proxy = using_default

        defaults = {
            "keywords": "", "location": "", "max_jobs": 5, "concurrency": 2,
            "delay_range": (3.0, 8.0), "log_level": "INFO", "date_posted": "Any time",
            "job_type": [], "experience_level": [], "remote": "On-site",
        }
        for key, value in defaults.items():
            st.session_state[key] = initial_state.get(key, value)

        st.session_state.searching = False
        st.session_state.pid = None
        st.session_state.log_lines = []
        st.session_state.results = None
        st.session_state.status_message = None
        st.session_state.start_job = False
        st.session_state.just_uploaded_proxy = False
        st.session_state.app_initialized = True
        st.session_state.progress = 0
        st.session_state.progress_phase = 0
        st.session_state.total_jobs_found = 0
        st.session_state.pages_processed = 0
        st.session_state.jobs_processed = 0

    if basic_mode:
        concurrency_to_use = 2
        delay_to_use = (3.0, 8.0)
        log_level_to_use = "INFO"
        if st.session_state.proxy_config_content: # Use more aggressive defaults if proxies are loaded
            concurrency_to_use = 5
            delay_to_use = (2.0, 4.0)

        st.session_state.concurrency = args.concurrency if args.concurrency is not None else concurrency_to_use
        st.session_state.delay_range = (float(args.delay[0]), float(args.delay[1])) if args.delay is not None else delay_to_use
        st.session_state.log_level = args.log_level if args.log_level is not None else log_level_to_use

    st.title("LinkedIn Job Extractor")
    st.markdown("An interactive UI for the `ljobx` scraping tool. Enter your search criteria and start the search.")

    with st.container(border=True):
        st.subheader("🎯 Search Criteria")
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("**Keywords**", key="keywords", placeholder="e.g., Senior Python Developer")
        with c2:
            st.text_input("**Location**", key="location", placeholder="e.g., Noida, India or Remote")

        st.subheader("📊 Filters")
        f1, f2 = st.columns(2)
        with f1:
            st.selectbox("Date Posted", options=list(FILTERS["date_posted"]["options"].keys()), key="date_posted")
            st.multiselect("Job Type", options=list(FILTERS["job_type"]["options"].keys()), key="job_type")
        with f2:
            st.multiselect("Experience Level", options=list(FILTERS["experience_level"]["options"].keys()), key="experience_level")
            st.selectbox("Remote Options", options=list(FILTERS["remote"]["options"].keys()), key="remote")

        st.subheader("⚙️ Scraper Settings")
        st.number_input("**Max Jobs to Scrape**", min_value=1, max_value=1000, key="max_jobs")

        if not basic_mode:
            with st.expander("🛠️ Advanced Settings"):
                sc1, sc2 = st.columns(2)
                with sc1:
                    st.slider("**Concurrency**", 1, 10, key="concurrency")
                    st.selectbox("Log Level", ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"], key="log_level")
                with sc2:
                    st.slider("**Delay Range (s)**", 0.0, 20.0, key="delay_range")

                st.markdown("---")
                st.subheader("🔌 Proxy Configuration")

                if st.session_state.proxy_config_content:
                    if st.session_state.get('using_default_proxy'):
                        st.success("✅ Using the system's default proxy configuration.")
                    else:
                        st.info("ℹ️ Using a user-uploaded proxy configuration.")
                    if not st.session_state.get('using_default_proxy'):
                        if st.button("Restore to default proxy settings"):
                            # noinspection PyUnboundLocalVariable
                            st.session_state.proxy_config_content = default_content_on_disk
                            st.session_state.using_default_proxy = True if default_content_on_disk else False
                            st.rerun()

                st.file_uploader("Upload Proxy Config", type=['yml', 'yaml'], key="proxy_uploader", on_change=handle_proxy_upload)

    b1, b2 = st.columns(2)
    with b1:
        start_search = st.button("🟢 Start Search", disabled=st.session_state.searching, use_container_width=True)
    with b2:
        stop_search = st.button("🔴 Stop Search", disabled=not st.session_state.searching, use_container_width=True)

    st.markdown("---")
    progress_placeholder = st.empty()
    log_placeholder = st.empty()
    results_placeholder = st.empty()
    status_placeholder = st.empty()

    if st.session_state.searching:
        progress_text = "Initializing..."
        if st.session_state.progress_phase == 1:
            total_pages = math.ceil(st.session_state.max_jobs / 10)
            progress_text = f"Phase 2/3: Searching... (Page {st.session_state.pages_processed}/{total_pages})"
        elif st.session_state.progress_phase == 2:
            progress_text = f"Phase 3/3: Scraping details... ({st.session_state.jobs_processed}/{st.session_state.total_jobs_found})"
        progress_placeholder.progress(st.session_state.progress / 100, progress_text)

    if st.session_state.status_message:
        msg_type, msg_text = st.session_state.status_message
        if msg_type == "success": status_placeholder.success(msg_text)
        elif msg_type == "warning": status_placeholder.warning(msg_text)
        else: status_placeholder.error(msg_text)

    if st.session_state.results:
        with results_placeholder.container():
            st.subheader("📄 Results")

            # st.session_state.results is now a list of dictionaries
            results_list = st.session_state.results
            flat_results = [_flatten_dict(res) for res in results_list]

            if flat_results:
                # Determine the optimal column order and headers
                all_keys = set(key for res in flat_results for key in res.keys())
                all_keys.discard('recruiter')

                preferred_order = [
                    'job_id', 'title', 'company', 'location', 'posted_date', 'applicants',
                    'salary_range', 'apply_url', 'apply_is_easy_apply', 'recruiter_name',
                    'recruiter_title', 'recruiter_profile_url', 'description'
                ]

                ordered_keys = [key for key in preferred_order if key in all_keys]
                remaining_keys = sorted(list(all_keys - set(ordered_keys)))
                final_ordered_keys = ordered_keys + remaining_keys

                header_overrides = {
                    "apply_is_easy_apply": "EASY_APPLY",
                    "recruiter_profile_url": "RECRUITER_PROFILE",
                }

                # Create a new list of dictionaries with ordered and renamed keys for display
                display_data = []
                for res in flat_results:
                    ordered_row = {}
                    for key in final_ordered_keys:
                        header = header_overrides.get(key, key.upper())
                        ordered_row[header] = res.get(key, "")
                    display_data.append(ordered_row)

                # Pass the list of dictionaries directly to Streamlit
                st.dataframe(display_data)
            else:
                # Display an empty dataframe if there are no results
                st.dataframe([])

            st.markdown("---")
            ts = time.strftime("%Y%m%d_%H%M%S")
            file_name_base = st.session_state.keywords.replace(' ', '_').lower()
            csv_data = generate_csv_data(results_list)

            # The download button logic remains unchanged
            if basic_mode:
                st.download_button("📥 Download as CSV", csv_data, f"{file_name_base}_{ts}.csv", "text/csv", use_container_width=True)
            else:
                dl1, dl2 = st.columns(2)
                with dl1:
                    st.download_button("📥 Download as CSV", csv_data, f"{file_name_base}_{ts}.csv", "text/csv", use_container_width=True)
                with dl2:
                    json_data = json.dumps(results_list, indent=2, ensure_ascii=False).encode('utf-8')
                    st.download_button("📥 Download as JSON", json_data, f"{file_name_base}_{ts}.json", "application/json", use_container_width=True)

    if not basic_mode and st.session_state.log_lines:
        with log_placeholder.container():
            st.subheader("📜 Live Log")
            st.code("\n".join(st.session_state.log_lines[-200:]), language="log")

    if start_search:
        if not st.session_state.keywords or not st.session_state.location:
            st.error("Please provide both Keywords and Location.")
        else:
            st.session_state.log_lines = []
            st.session_state.results = None
            st.session_state.status_message = None
            st.session_state.searching = True
            st.session_state.start_job = True
            st.rerun()

    if stop_search:
        if st.session_state.pid:
            try:
                p = psutil.Process(st.session_state.pid)
                p.terminate()
                st.warning("✅ Search stopped by user.")
            except psutil.NoSuchProcess:
                st.info("Process was already finished.")
            st.session_state.searching = False
            st.session_state.pid = None
            st.session_state.queues = None
            st.rerun()

    if st.session_state.start_job:
        manager = multiprocessing.Manager()
        results_queue = manager.Queue()
        log_queue = manager.Queue()
        progress_queue = manager.Queue()
        st.session_state.queues = (results_queue, log_queue, progress_queue)

        st.session_state.progress = 0
        st.session_state.progress_phase = 0
        st.session_state.total_jobs_found = 0
        st.session_state.pages_processed = 0
        st.session_state.jobs_processed = 0

        proxies = []
        if st.session_state.proxy_config_content:
            try:
                logging.info("Loading proxy configuration...")
                config_data = ConfigLoader.load(st.session_state.proxy_config_content)
                validate = config_data.get("validate_proxies", True)
                proxies = asyncio.run(ProxyManager.get_proxies_from_config(config_data, validate=validate))
                if not proxies:
                    logging.warning("No working proxies found. Scraper will run without proxies.")
            except (ValueError, FileNotFoundError) as e:
                logging.error(f"Failed to load proxies: {e}")
                st.error(f"Failed to load proxies: {e}")
                st.session_state.searching = False
                st.rerun()

        search_criteria = {
            'keywords': st.session_state.keywords, 'location': st.session_state.location,
            'date_posted': st.session_state.date_posted if st.session_state.date_posted != "Any time" else None,
            'job_type': st.session_state.job_type, 'experience_level': st.session_state.experience_level,
            'remote': st.session_state.remote if st.session_state.remote != "On-site" else None,
        }

        delay_min, delay_max = st.session_state.delay_range
        scraper_settings = {
            "max_jobs": st.session_state.max_jobs, "concurrency_limit": st.session_state.concurrency,
            "delay": {"min_val": int(delay_min), "max_val": int(delay_max)}, "proxies": proxies
        }

        p = multiprocessing.Process(target=run_scraper_in_process, args=(results_queue, log_queue, progress_queue, search_criteria, scraper_settings, st.session_state.log_level))
        p.start()
        st.session_state.pid = p.pid
        st.session_state.start_job = False
        st.rerun()

    if st.session_state.searching:
        results_queue, log_queue, progress_queue = st.session_state.queues
        try:
            while True:
                log_line = log_queue.get_nowait()
                st.session_state.log_lines.append(log_line)
        except Empty:
            pass

        try:
            while True:
                progress_update = progress_queue.get_nowait()
                if progress_update == "INIT":
                    st.session_state.progress = 5
                    st.session_state.progress_phase = 1
                elif progress_update == "PAGE":
                    if st.session_state.progress_phase == 1:
                        st.session_state.pages_processed += 1
                        total_pages = math.ceil(st.session_state.max_jobs / 10)
                        if total_pages > 0:
                            st.session_state.progress = 5 + int((st.session_state.pages_processed / total_pages) * 25)
                elif isinstance(progress_update, str) and progress_update.startswith("PAGE_END"):
                    st.session_state.total_jobs_found = int(progress_update.split(":")[1])
                    st.session_state.progress = 30
                    st.session_state.progress_phase = 2
                elif progress_update == "JOB":
                    if st.session_state.progress_phase == 2 and st.session_state.total_jobs_found > 0:
                        st.session_state.jobs_processed += 1
                        st.session_state.progress = 30 + int((st.session_state.jobs_processed / st.session_state.total_jobs_found) * 70)
        except Empty:
            pass

        if st.session_state.pid:
            if not psutil.pid_exists(st.session_state.pid):
                st.session_state.progress = 100
                progress_placeholder.progress(1.0, "Search complete!")
                try:
                    final_output = results_queue.get_nowait()
                    if isinstance(final_output, Exception):
                        st.session_state.status_message = ("error", f"An error occurred: {final_output}")
                    elif final_output:
                        st.session_state.status_message = ("success", f"✅ Search complete! Found {len(final_output)} jobs.")
                        st.session_state.results = final_output
                    else:
                        st.session_state.status_message = ("warning", "Search complete. No jobs found.")
                        st.session_state.results = []
                except Empty:
                    st.session_state.status_message = ("warning", "Process finished unexpectedly.")
                    st.session_state.results = []
                st.session_state.searching = False
                st.session_state.pid = None
                st.session_state.queues = None
                st.rerun()
            else:
                time.sleep(0.5)
                st.rerun()
        else:
            time.sleep(0.5)
            st.rerun()

    if not basic_mode:
        current_state = {
            key: st.session_state[key] for key in [
                "keywords", "location", "max_jobs", "concurrency", "delay_range",
                "date_posted", "job_type", "experience_level", "remote",
                "proxy_config_content", "log_level"
            ] if key in st.session_state
        }
        local_storage.setItem("form_inputs", json.dumps(current_state))

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()