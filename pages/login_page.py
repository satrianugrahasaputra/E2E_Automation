from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from utils.logger import logger

class LoginPage(BasePage):
    """Page Object for the Login Page supporting SauceDemo, Jateng OTS, and local mock app."""

    def navigate_to_login(self, base_url: str) -> None:
        """Navigates to the login page."""
        if "saucedemo.com" in base_url or "jateng.pro" in base_url:
            url = base_url
        else:
            url = f"{base_url}/login.html"
        self.navigate(url)

    def _is_sauce(self) -> bool:
        return "saucedemo.com" in self.page.url

    def _is_jateng(self) -> bool:
        return "jateng.pro" in self.page.url

    def input_username(self, username: str) -> None:
        """Inputs the username."""
        if self._is_sauce():
            selector = LoginLocators.SAUCE_USERNAME_INPUT
        elif self._is_jateng():
            selector = LoginLocators.JATENG_USERNAME_INPUT
        else:
            selector = LoginLocators.USERNAME_INPUT
        self.fill(selector, username)

    def input_password(self, password: str) -> None:
        """Inputs the password."""
        if self._is_sauce():
            selector = LoginLocators.SAUCE_PASSWORD_INPUT
        elif self._is_jateng():
            selector = LoginLocators.JATENG_PASSWORD_INPUT
        else:
            selector = LoginLocators.PASSWORD_INPUT
        self.fill(selector, password)

    def click_login(self) -> None:
        """Clicks the login button."""
        if self._is_sauce():
            selector = LoginLocators.SAUCE_LOGIN_BUTTON
        elif self._is_jateng():
            selector = LoginLocators.JATENG_LOGIN_BUTTON
        else:
            selector = LoginLocators.LOGIN_BUTTON
        self.click(selector)

    def verify_login_success(self) -> None:
        """Asserts that login was successful."""
        logger.info("Verifying login success")
        if self._is_sauce():
            self.verify_url("https://www.saucedemo.com/inventory.html")
        elif self._is_jateng():
            # In Jateng OTS, a successful login will redirect away from the login page (e.g. to /admin/dashboard)
            # We can check that the URL contains the dashboard path or is not /login anymore
            # Since we do not know the exact success URL, we can verify it doesn't end with /login
            logger.info("Jateng OTS: Verifying redirected away from login URL")
            self.page.wait_for_url("**/admin/dashboard**", timeout=5000)
        else:
            self.verify_element_text(LoginLocators.SUCCESS_MESSAGE, "Login successful!")

    def verify_login_failed(self, expected_error: str) -> None:
        """Asserts that login failed with correct error."""
        logger.info(f"Verifying login error message: '{expected_error}'")
        if self._is_sauce():
            if "incorrect" in expected_error or "match" in expected_error:
                expected_error = "Epic sadface: Username and password do not match any user in this service"
            elif "required" in expected_error:
                if "Username" in expected_error:
                    expected_error = "Epic sadface: Username is required"
                else:
                    expected_error = "Epic sadface: Password is required"
            self.verify_element_text(LoginLocators.SAUCE_ERROR_MESSAGE, expected_error)
        elif self._is_jateng():
            # If checking for missing fields in HTML5, the browser prevents form submit (required attribute).
            # If the submit button was actually clicked and a backend error occurred, it is shown in #errorBox.
            # Let's verify that the expected_error text is inside #errorBox (or if it's an HTML5 validation popup,
            # we handle/log it). Let's do a simple check.
            self.verify_element_text(LoginLocators.JATENG_ERROR_MESSAGE, expected_error)
        else:
            self.verify_element_text(LoginLocators.ERROR_MESSAGE, expected_error)
