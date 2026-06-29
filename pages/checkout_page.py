from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators
from utils.logger import logger

class CheckoutPage(BasePage):
    """Page Object for managing the Checkout and E-Commerce Catalog flows."""

    def _is_sauce(self) -> bool:
        return "saucedemo.com" in self.page.url

    def navigate_to_shop(self, base_url: str) -> None:
        """Navigates to the shop homepage."""
        if self._is_sauce():
            self.navigate(f"{base_url}/inventory.html")
        else:
            self.navigate(f"{base_url}/index.html")

    def add_product_1_to_cart(self) -> None:
        """Adds the first item in the catalog to the cart."""
        selector = CheckoutLocators.SAUCE_ADD_TO_CART_PRODUCT_1 if self._is_sauce() else CheckoutLocators.ADD_TO_CART_PRODUCT_1
        self.click(selector)

    def verify_cart_badge(self, expected_value: str) -> None:
        """Verifies the number shown on the cart badge."""
        logger.info(f"Verifying cart badge has value: {expected_value}")
        if self._is_sauce() and expected_value == "0":
            # In SauceDemo, badge element is hidden if 0
            if self.is_visible(CheckoutLocators.SAUCE_CART_BADGE, timeout=1000):
                self.verify_element_text(CheckoutLocators.SAUCE_CART_BADGE, expected_value)
        else:
            selector = CheckoutLocators.SAUCE_CART_BADGE if self._is_sauce() else CheckoutLocators.CART_BADGE
            self.verify_element_text(selector, expected_value)

    def click_cart(self) -> None:
        """Navigates to the cart page by clicking the cart button."""
        selector = CheckoutLocators.SAUCE_CART_BUTTON if self._is_sauce() else CheckoutLocators.CART_BUTTON
        self.click(selector)

    def verify_cart_total(self, expected_total: str) -> None:
        """Verifies total cost of items in the cart."""
        if self._is_sauce():
            # SauceDemo doesn't have a total on the cart page itself (it's verified later on step two)
            logger.info("SauceDemo: Cart total is verified on the overview page step")
            return
        logger.info(f"Verifying cart total is: {expected_total}")
        self.verify_element_text(CheckoutLocators.CART_TOTAL, expected_total)

    def click_proceed_to_checkout(self) -> None:
        """Clicks the proceed to checkout button on the cart page."""
        selector = CheckoutLocators.SAUCE_PROCEED_TO_CHECKOUT_BUTTON if self._is_sauce() else CheckoutLocators.PROCEED_TO_CHECKOUT_BUTTON
        self.click(selector)

    def fill_shipping_details(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fills out the shipping details form."""
        if self._is_sauce():
            self.fill(CheckoutLocators.SAUCE_FIRST_NAME_INPUT, first_name)
            self.fill(CheckoutLocators.SAUCE_LAST_NAME_INPUT, last_name)
            self.fill(CheckoutLocators.SAUCE_POSTAL_CODE_INPUT, postal_code)
            # Click Continue to proceed to overview step
            self.click(CheckoutLocators.SAUCE_CONTINUE_BUTTON)
            # Verify total overview matches backpack total ($29.99 + tax = $32.39)
            self.verify_element_text(CheckoutLocators.SAUCE_CART_TOTAL, "Total: $32.39")
        else:
            self.fill(CheckoutLocators.FIRST_NAME_INPUT, first_name)
            self.fill(CheckoutLocators.LAST_NAME_INPUT, last_name)
            self.fill(CheckoutLocators.POSTAL_CODE_INPUT, postal_code)

    def click_finish_checkout(self) -> None:
        """Clicks the finish checkout submit button."""
        selector = CheckoutLocators.SAUCE_FINISH_BUTTON if self._is_sauce() else CheckoutLocators.FINISH_BUTTON
        self.click(selector)

    def verify_checkout_success(self) -> None:
        """Verifies successful checkout completion message."""
        logger.info("Verifying checkout order successful completion message")
        if self._is_sauce():
            self.verify_element_text(CheckoutLocators.SAUCE_SUCCESS_TITLE, "Thank you for your order!")
            self.verify_element_text(
                CheckoutLocators.SAUCE_SUCCESS_MESSAGE, 
                "Your order has been dispatched, and will arrive just as fast as the pony can get there!"
            )
        else:
            self.verify_element_text(CheckoutLocators.SUCCESS_TITLE, "Thank you for your order!")
            self.verify_element_text(
                CheckoutLocators.SUCCESS_MESSAGE, 
                "Your order has been placed successfully and will be shipped soon."
            )
