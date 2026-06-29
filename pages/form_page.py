from pages.base_page import BasePage
from locators.form_locators import FormLocators
from utils.logger import logger

class FormPage(BasePage):
    """Page Object for the Form Page."""

    def navigate_to_form(self, base_url: str) -> None:
        """Navigates to the form page."""
        url = f"{base_url}/form.html"
        self.navigate(url)

    def input_fullname(self, name: str) -> None:
        """Inputs the full name."""
        self.fill(FormLocators.FULLNAME_INPUT, name)

    def input_email(self, email: str) -> None:
        """Inputs the email address."""
        self.fill(FormLocators.EMAIL_INPUT, email)

    def select_role(self, role_value: str) -> None:
        """Selects a job role from dropdown."""
        self.select_option(FormLocators.ROLE_SELECT, role_value)

    def check_automation_interest(self) -> None:
        """Checks the automation interest checkbox."""
        self.check(FormLocators.INTEREST_AUTOMATION_CHECKBOX)

    def check_manual_interest(self) -> None:
        """Checks the manual interest checkbox."""
        self.check(FormLocators.INTEREST_MANUAL_CHECKBOX)

    def input_dob(self, date_val: str) -> None:
        """Inputs the date of birth."""
        self.fill(FormLocators.DOB_INPUT, date_val)

    def upload_cv(self, file_path: str) -> None:
        """Uploads the CV file."""
        self.upload_file(FormLocators.FILE_INPUT, file_path)

    def click_submit(self) -> None:
        """Clicks the submit button."""
        self.click(FormLocators.SUBMIT_BUTTON)

    def verify_submission_success(self, file_name: str) -> None:
        """Verifies successful form submission."""
        logger.info(f"Verifying form submission success with file name: {file_name}")
        self.verify_element_text(
            FormLocators.SUCCESS_MESSAGE, 
            f"Form submitted successfully! Uploaded: {file_name}"
        )

    def verify_submission_failed(self, expected_error: str) -> None:
        """Verifies form submission error."""
        logger.info(f"Verifying form submission error: '{expected_error}'")
        self.verify_element_text(FormLocators.ERROR_MESSAGE, expected_error)
