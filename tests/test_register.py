import pandas as pd
import pytest
from playwright.sync_api import Page
from pages.register_page import RegisterPage

def load_register_data():
    df = pd.read_csv("data/register_data.csv")
    # Replace NaN values with empty string
    df = df.fillna("")
    return df.to_dict(orient="records")

@pytest.mark.parametrize("data", load_register_data())
def test_register(page: Page, base_url: str, data: dict):
    register_page = RegisterPage(page)
    register_page.navigate_to_register(base_url)
    
    # Act
    register_page.input_username(data["username"])
    register_page.input_email(data["email"])
    register_page.input_password(data["password"])
    register_page.input_confirm_password(data["confirm_password"])
    register_page.click_register()
    
    # Assert
    if data["expected_status"] == "success":
        register_page.verify_register_success()
    else:
        register_page.verify_register_failed(data["error_message"])
