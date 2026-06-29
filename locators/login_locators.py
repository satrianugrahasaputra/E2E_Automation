class LoginLocators:
    # Local site selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-btn"
    ERROR_MESSAGE = "#error-msg"
    SUCCESS_MESSAGE = "#success-msg"

    # SauceDemo selectors
    SAUCE_USERNAME_INPUT = "#user-name"
    SAUCE_PASSWORD_INPUT = "#password"
    SAUCE_LOGIN_BUTTON = "#login-button"
    SAUCE_ERROR_MESSAGE = "[data-test='error']"

    # Jateng OTS selectors
    JATENG_USERNAME_INPUT = "[name='username']"
    JATENG_PASSWORD_INPUT = "[name='password']"
    JATENG_LOGIN_BUTTON = "#submitBtn"
    JATENG_ERROR_MESSAGE = "#errorBox"
