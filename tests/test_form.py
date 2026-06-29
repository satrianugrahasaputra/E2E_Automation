import os
import pytest
from faker import Faker
from playwright.sync_api import Page
from pages.form_page import FormPage

fake = Faker()

def test_form_submission_valid(page: Page, base_url: str):
    form_page = FormPage(page)
    form_page.navigate_to_form(base_url)
    
    # Generate dynamic test data using Faker
    fullname = fake.name()
    email = fake.email()
    dob = "1995-05-15"
    
    # Paths for upload
    cv_path = os.path.abspath("data/sample_cv.txt")
    
    # Act
    form_page.input_fullname(fullname)
    form_page.input_email(email)
    form_page.select_role("qa")
    form_page.check_automation_interest()
    form_page.input_dob(dob)
    form_page.upload_cv(cv_path)
    form_page.click_submit()
    
    # Assert
    form_page.verify_submission_success("sample_cv.txt")

@pytest.mark.parametrize(
    "missing_field, expected_error",
    [
        ("fullname", "Full Name is required"),
        ("email", "Email is required"),
        ("role", "Please select a job role"),
        ("interests", "Please select at least one interest"),
        ("dob", "Date of Birth is required"),
        ("file", "Please upload your CV file"),
    ]
)
def test_form_submission_invalid(page: Page, base_url: str, missing_field: str, expected_error: str):
    form_page = FormPage(page)
    form_page.navigate_to_form(base_url)
    
    cv_path = os.path.abspath("data/sample_cv.txt")
    
    # Fill standard valid data first
    if missing_field != "fullname":
        form_page.input_fullname(fake.name())
    if missing_field != "email":
        form_page.input_email(fake.email())
    if missing_field != "role":
        form_page.select_role("qa")
    if missing_field != "interests":
        form_page.check_automation_interest()
    if missing_field != "dob":
        form_page.input_dob("1995-05-15")
    if missing_field != "file":
        form_page.upload_cv(cv_path)
        
    form_page.click_submit()
    
    # Assert
    form_page.verify_submission_failed(expected_error)
