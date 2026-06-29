import json
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

def load_login_data():
    with open("data/login_data.json", "r") as f:
        return json.load(f)

@pytest.mark.parametrize("data", load_login_data())
def test_login(page: Page, base_url: str, data: dict):
    login_page = LoginPage(page)
    login_page.navigate_to_login(base_url)
    
    # Act
    login_page.input_username(data["username"])
    login_page.input_password(data["password"])
    login_page.click_login()
    
    # Assert
    if data["expected_status"] == "success":
        login_page.verify_login_success()
    else:
        login_page.verify_login_failed(data["error_message"])
