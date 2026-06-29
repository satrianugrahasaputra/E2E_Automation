import os
import subprocess
import time
import socket
from datetime import datetime
import pytest
from dotenv import load_dotenv
from utils.logger import logger

# Load environment variables
load_dotenv()

def is_port_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

@pytest.fixture(scope="session", autouse=True)
def local_server():
    """Starts the local mock web server for testing in the background."""
    server_process = None
    if not is_port_open(8000):
        logger.info("Starting local mock server on port 8000...")
        server_process = subprocess.Popen(
            ["python", "-m", "http.server", "8000", "--directory", "demo_site"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        time.sleep(1)
    else:
        logger.info("Local mock server is already running.")
    
    yield
    
    if server_process:
        logger.info("Stopping local mock server...")
        server_process.terminate()
        server_process.wait()

@pytest.fixture(scope="session")
def base_url():
    """Returns the base url for the application."""
    env_url = os.getenv("BASE_URL", "http://localhost:8000")
    if "localhost" in env_url or "127.0.0.1" in env_url:
        return env_url
    return "http://localhost:8000"

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Overrides browser context arguments to configure video recording."""
    os.makedirs("videos", exist_ok=True)
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshots on failure and embed them into the HTML report."""
    outcome = yield
    rep = outcome.get_result()
    
    # Capture screenshot only if test failed during call phase
    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("screenshots", exist_ok=True)
            # Safe filename by removing invalid characters
            safe_name = "".join([c if c.isalnum() or c in ("-", "_") else "_" for c in item.name])
            screenshot_name = f"{safe_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            screenshot_path = os.path.join("screenshots", screenshot_name)
            
            try:
                page.screenshot(path=screenshot_path)
                logger.error(f"Test failed! Screenshot saved to: {screenshot_path}")
                
                # Embed screenshot in pytest-html report
                html = item.config.pluginmanager.get_plugin("html")
                if html:
                    # Resolve relative path for html integration
                    relative_path = os.path.relpath(screenshot_path, start="reports")
                    extra = getattr(rep, "extra", [])
                    extra.append(html.extras.image(relative_path, name="Screenshot on Failure"))
                    rep.extra = extra
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {str(e)}")
