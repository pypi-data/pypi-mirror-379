import hashlib
import logging
import re
import threading
import urllib.parse
from typing import Optional, Dict, Any

import requests

logger = logging.getLogger(__name__)


# --- inside _InFlightPoster ---
class _InFlightPoster:
    """
    Fire-and-forget poster with a hard cap on concurrent posts.
    If the cap is reached, events are dropped immediately.
    No queues, no background loop.
    """
    def __init__(self, url: str, max_in_flight: int = 20, connect_to: float = 0.8, read_to: float = 0.8):
        self.url = url
        self._sem = threading.Semaphore(max_in_flight)
        self._timeout = (connect_to, read_to)
        self._dropped = 0

    def post(self, payload: Dict[str, Any], headers: Dict[str, Any]) -> None:
        if not self._sem.acquire(blocking=False):
            self._dropped += 1
            if self._dropped % 100 == 1:
                logger.debug("tracker dropped (in-flight cap reached), total_dropped=%s", self._dropped)
            return

        def _worker():
            try:
                with requests.Session() as s:
                    s.post(self.url, json=payload, timeout=self._timeout, headers=headers)
            except Exception as e:
                # swallow errors; telemetry must never affect app
                logger.debug("error posting tracker: %s", e)
                pass
            finally:
                # always release, even if post() failed
                self._sem.release()

        try:
            threading.Thread(
                target=_worker,
                name="tracker-fire-and-forget",
                daemon=True
            ).start()
        except Exception:
            # if the thread couldn't even start, release immediately
            self._sem.release()
            raise
        
class Tracker:
    # Set this value to false to disable dbdemo toolkit tracker.
    enable_tracker = True
    URL = "https://ppxrzfxige.execute-api.us-west-2.amazonaws.com/v1/analytics"
    _poster = _InFlightPoster(URL, max_in_flight=20, connect_to=2, read_to=2)

    def __init__(self, org_id, email=None, demo_name=None):
        self.org_id = org_id
        self.demo_name = demo_name
        # This is aggregating user behavior within Databricks at the org level to better understand dbdemos usage and improve the product.
        # We are not collecting any email/PII data. Please reach out to the demo team if you have any questions.
        if email is not None and email.endswith("@databricks.com"):
            self.email = email
        else:
            self.email = None
    

    def track_install(self, category, demo_name, email=None):
        self.track(category, demo_name, "INSTALL", email=email)
    
    def track_create_cluster(self, category, demo_name, email=None):
        self.track(category, demo_name, "CREATE_CLUSTER", email=email)
    
    def track_list(self, email=None):
        self.track("list_demos", "list_demos", "LIST", email=email)

    def track_app_view_demo(self, user_email, demo_name: str, app_path: str):
        self.track("demo-app", demo_name, "APP-VIEW", app_path=app_path, email=user_email)

    def track_app_view(self, user_email, app_path):
        if self.demo_name is None:
            raise ValueError("demo_name is required when creating a tracker instance and tracking app views")
        self.track("demo-app", self.demo_name, "APP-VIEW", app_path=app_path, email=user_email)

    def track_catalog_view(self, user_email, industry, app_path: str = None):
        self.track("catalog-app", "catalog", "CATALOG-VIEW", app_path=app_path, email=user_email, industry=industry)

    def track_catalog_open_demo(self, user_email, industry, demo_name: str, app_path: str = None):
        self.track("catalog-app", demo_name, "CATALOG-OPEN", app_path=app_path, email=user_email, industry=industry)

    def get_user_hash(self, email=None):
        # Use provided email or fallback to instance email
        email_to_hash = email if email is not None else self.email
        if email_to_hash is None or not email_to_hash.endswith("@databricks.com"):
            return None
        return hashlib.sha256(email_to_hash.encode()).hexdigest()

    def get_track_url(self, category, demo_name, event, notebook=None, email=None):
        params = self.get_track_params(category, demo_name, event, notebook, email=email)
        return Tracker.URL + "?" + urllib.parse.urlencode(params)

    def get_track_params(self, category, demo_name, event, notebook=None, app_path=None, email=None, industry=None):
        if not Tracker.enable_tracker:
            return {}
        
        params = {"category": category,
                  "org_id": self.org_id,  # legacy "cid"
                  "demo_name": demo_name,
                  "event": event,
                  "industry": industry,
                  "version": 1}
        
        # Add notebook if provided
        if notebook is not None:
            params["notebook"] = '/' + notebook if len(notebook) > 0 else notebook
            params["path"] = f"/_dbdemos/{category}/{demo_name}/{notebook}"  # legacy tracking "dp"
        else:
            params["path"] = f"/_dbdemos/{category}/{demo_name}"  # legacy tracking "dp"
        
        # Add app_path if provided
        if app_path is not None:
            params["app_path"] = app_path
        
        # Analyze internal usage only - tracking is aggregated at a higher level so that we don't track individual users (user hash isn't saved).
        user_hash = self.get_user_hash(email)
        if user_hash is not None:
            params["user_hash"] = user_hash
        return params

    def track(self, category, demo_name, event, notebook=None, app_path=None, email=None, industry=None):
        logger.debug(f"Tracking event: category={category}, demo={demo_name}, event={event}, notebook={notebook}, app_path={app_path}, industry={industry}")
        
        if self.org_id == "1660015457675682":
            logger.info("Skipping tracker for test / dev workspace")
            return
        elif Tracker.enable_tracker:
            headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                      "accept-encoding": "gzip, deflate, br",
                      "accept-language": "en-US,en;q=0.9",
                      "cache-control": "max-age=0",
                      "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            try:
                params = self.get_track_params(category, demo_name, event, notebook, app_path, email, industry)
                logger.debug(f"Sending tracking request with params: {params}")
                if not params:
                    return

                # fire-and-forget with dropping when busy
                Tracker._poster.post(params, headers)
            except Exception as e:
                logger.error(f"Usage report error. See readme to disable it. Error: {str(e)}")
        else:
            logger.debug("Tracking disabled globally")


    @staticmethod
    def add_tracker_fastapi(app, demo_name: str, workspace_client=None, patterns=None):
        from fastapi import Request

        """
        Create a FastAPI middleware that automatically tracks all requests.
        Args:
            demo_name: Name of the demo to track
            workspace_client: Optional WorkspaceClient instance. If None, creates a new one.
            patterns: List of regex patterns to match against the request path.
        """
        if patterns is None:
            patterns = []

        if workspace_client is None:
            from databricks.sdk import WorkspaceClient
            workspace_client = WorkspaceClient()

        tracker = Tracker(demo_name=demo_name, org_id=workspace_client.get_workspace_id())

        @app.middleware("http")
        async def track_app_usage(request: Request, call_next):
            path = request.url.path

            # Only track if path matches one of the provided patterns (regex)
            if not patterns or any(re.match(pattern, path) for pattern in patterns):
                user_email = request.headers.get("X-Forwarded-Email")
                if user_email:
                    try:
                        tracker.track_app_view(user_email=user_email, app_path=path)
                    except Exception as e:
                        logger.warning(f"Tracking error: {e}")

            response = await call_next(request)
            return response

    @staticmethod
    def setup_streamlit_interceptor(demo_name: str, workspace_client=None):
        """
        Setup Streamlit interceptor that automatically tracks all interactions.
        
        Args:
            demo_name: Name of the demo to track
            workspace_client: Optional WorkspaceClient instance. If None, creates a new one.
        
        Returns:
            None - sets up automatic tracking for all Streamlit interactions
        """
        try:
            # Get workspace ID
            if workspace_client is None:
                from databricks.sdk import WorkspaceClient
                org = WorkspaceClient().get_workspace_id()
            else:
                org = workspace_client.get_workspace_id()
            
            # Create tracker instance
            tracker = Tracker(org)
            
            # Import streamlit and set up interceptor
            import streamlit as st
            
            # Store tracker in session state for access throughout the app
            if 'dbdemos_tracker' not in st.session_state:
                st.session_state.dbdemos_tracker = tracker
                st.session_state.dbdemos_demo_name = demo_name
            
            # Set up automatic tracking for common Streamlit interactions
            def track_interaction():
                try:
                    # Get email from session state or environment
                    email = st.session_state.get('user_email', None)
                    if email is not None and not email.endswith("@databricks.com"):
                        email = None
                    
                    # Track the interaction
                    tracker.track("demo-app", demo_name, "STREAMLIT-INTERACTION", email=email)
                except Exception as e:
                    logger.error(f"Streamlit tracking error: {str(e)}")
            
            # Monkey patch common Streamlit methods to include tracking
            original_button = st.button
            original_form_submit_button = st.form_submit_button
            original_selectbox = st.selectbox
            original_slider = st.slider
            original_checkbox = st.checkbox
            original_radio = st.radio
            
            def tracked_button(*args, **kwargs):
                result = original_button(*args, **kwargs)
                if result:
                    track_interaction()
                return result
            
            def tracked_form_submit_button(*args, **kwargs):
                result = original_form_submit_button(*args, **kwargs)
                if result:
                    track_interaction()
                return result
            
            def tracked_selectbox(*args, **kwargs):
                result = original_selectbox(*args, **kwargs)
                track_interaction()
                return result
            
            def tracked_slider(*args, **kwargs):
                result = original_slider(*args, **kwargs)
                track_interaction()
                return result
            
            def tracked_checkbox(*args, **kwargs):
                result = original_checkbox(*args, **kwargs)
                track_interaction()
                return result
            
            def tracked_radio(*args, **kwargs):
                result = original_radio(*args, **kwargs)
                track_interaction()
                return result
            
            # Replace the original methods
            st.button = tracked_button
            st.form_submit_button = tracked_form_submit_button
            st.selectbox = tracked_selectbox
            st.slider = tracked_slider
            st.checkbox = tracked_checkbox
            st.radio = tracked_radio
            
            logger.info(f"Streamlit interceptor set up for demo: {demo_name}")
            
        except Exception as e:
            logger.error(f"Failed to setup Streamlit interceptor: {str(e)}")

    @staticmethod
    def track_streamlit_app(demo_name: str, workspace_client=None, email: str = None):
        """
        Track Streamlit app interaction - single method for all backend interactions.
        
        Args:
            demo_name: Name of the demo to track
            workspace_client: Optional WorkspaceClient instance. If None, creates a new one.
            email: Optional email to track (will be filtered to Databricks emails only)
        
        Returns:
            None - tracks the interaction automatically
        """
        try:
            # Get workspace ID
            if workspace_client is None:
                from databricks.sdk import WorkspaceClient
                org = WorkspaceClient().get_workspace_id()
            else:
                org = workspace_client.get_workspace_id()
            
            # Filter email to Databricks only
            if email is not None and not email.endswith("@databricks.com"):
                email = None
            
            # Create tracker and track the interaction
            tracker = Tracker(org)
            tracker.track("demo-app", demo_name, "STREAMLIT-INTERACTION", email=email)
            
        except Exception as e:
            logger.error(f"Streamlit tracking error: {str(e)}") 