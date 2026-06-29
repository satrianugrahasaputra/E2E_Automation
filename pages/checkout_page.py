from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from utils.logger import logger

class CheckoutPage(BasePage):
    """Page Object for managing the Checkout and E-Commerce Catalog flows."""

    def navigate_to_shop(self, base_url: str) -> None:
        """Navigates to the shop homepage."""
        self.navigate(f"{base_url}/index.html")

    def add_product_1_to_cart(self) -> None:
        """Adds the first item in the catalog to the cart."""
        self.click(CheckoutLocators.ADD_TO_CART_PRODUCT_1)

    def verify_cart_badge(self, expected_value: str) -> None:
        """Verifies the number shown on the cart badge."""
        logger.info(f"Verifying cart badge has value: {expected_value}")
        self.verify_element_text(CheckoutLocators.CART_BADGE, expected_value)

    def click_cart(self) -> None:
        """Navigates to the cart page by clicking the cart button."""
        self.click(CheckoutLocators.CART_BUTTON)

    def verify_cart_total(self, expected_total: str) -> None:
        """Verifies total cost of items in the cart."""
        logger.info(f"Verifying cart total is: {expected_total}")
        self.verify_element_text(CheckoutLocators.CART_TOTAL, expected_total)

    def click_proceed_to_checkout(self) -> None:
        """Clicks the proceed to checkout button on the cart page."""
        self.click(CheckoutLocators.PROCEED_TO_CHECKOUT_BUTTON)

    def fill_shipping_details(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fills out the shipping details form."""
        self.fill(CheckoutLocators.FIRST_NAME_INPUT, first_name)
        self.fill(CheckoutLocators.LAST_NAME_INPUT, last_name)
        self.fill(CheckoutLocators.POSTAL_CODE_INPUT, postal_code)

    def click_finish_checkout(self) -> None:
        """Clicks the finish checkout submit button."""
        self.click(CheckoutLocators.FINISH_BUTTON)

    def verify_checkout_success(self) -> None:
        """Verifies successful checkout completion message."""
        logger.info("Verifying checkout order successful completion message")
        self.verify_element_text(CheckoutLocators.SUCCESS_TITLE, "Thank you for your order!")
        self.verify_element_text(
            CheckoutLocators.SUCCESS_MESSAGE, 
            "Your order has been placed successfully and will be shipped soon."
        )
