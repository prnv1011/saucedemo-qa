from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page
        self.cart_backpack = page.locator(".inventory_item_name").filter(has_text="Sauce Labs Backpack")
        self.cart_fleece_jacket = page.locator(".inventory_item_name").filter(has_text="Sauce Labs Fleece Jacket")
        self.checkout_btn = page.locator("#checkout")

    def verify_backpack_visibility(self):
        expect(self.cart_backpack).to_be_visible()

    def verify_fleece_jacket_visibility(self):
        expect(self.cart_fleece_jacket).to_be_visible()

    def click_checkout_btn(self):
        self.checkout_btn.click()