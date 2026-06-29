from faker import Faker
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

fake = Faker()

def test_checkout_flow_complete(page: Page, base_url: str):
    # 1. Login Step
    login_page = LoginPage(page)
    login_page.navigate_to_login(base_url)
    login_page.input_username("standard_user")
    login_page.input_password("secret_sauce")
    login_page.click_login()
    
    # 2. Add product to cart
    checkout_page = CheckoutPage(page)
    # The login redirect will send the user to index.html automatically,
    # but we can verify or explicitly load it. Let's verify badge.
    checkout_page.verify_cart_badge("0")
    checkout_page.add_product_1_to_cart()
    checkout_page.verify_cart_badge("1")
    
    # 3. Proceed to Cart
    checkout_page.click_cart()
    checkout_page.verify_cart_total("$49.99")
    checkout_page.click_proceed_to_checkout()
    
    # 4. Fill shipping details and Checkout
    first_name = fake.first_name()
    last_name = fake.last_name()
    postal_code = fake.postcode()
    
    checkout_page.fill_shipping_details(first_name, last_name, postal_code)
    checkout_page.click_finish_checkout()
    
    # 5. Verify Checkout Completed
    checkout_page.verify_checkout_success()
