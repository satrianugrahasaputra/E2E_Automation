import os
import subprocess
import time
import socket
import pytest
from dotenv import load_dotenv

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
        # Start python build-in HTTP server in demo_site directory
        server_process = subprocess.Popen(
            ["python", "-m", "http.server", "8000", "--directory", "demo_site"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # Give it a short moment to spin up
        time.sleep(1)
    
    yield
    
    if server_process:
        server_process.terminate()
        server_process.wait()

@pytest.fixture(scope="session")
def base_url():
    """Returns the base url for the application."""
    # Use environment variable base URL, default to local server if not specified or saucedemo
    env_url = os.getenv("BASE_URL", "http://localhost:8000")
    # If the user has it set to saucedemo but we want our local server for local pages
    if "localhost" in env_url or "127.0.0.1" in env_url:
        return env_url
    return "http://localhost:8000"
