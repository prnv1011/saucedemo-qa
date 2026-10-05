import config.settings
from pages import inventory_page
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.open()
    username=config.settings.USERNAME
    password=config.settings.PASSWORD
    login_page.login(username,password)
    login_page.verify_login_success()

    inventory_page = InventoryPage(page)
    inventory_page.click_backpack_atc()
    inventory_page.click_checkout_btn()

    cart_page = CartPage(page)
    cart_page.verify_backpack_visibility()
    cart_page.click_checkout_btn()

    checkout_page = CheckoutPage(page)
    checkout_page.checkout_details()
    checkout_page.click_continue_btn()
    checkout_page.click_finish_btn()
    checkout_page.verify_order_confirmation()