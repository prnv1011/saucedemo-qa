from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.checkout_first_name = page.get_by_placeholder('First Name')
        self.checkout_last_name = page.get_by_placeholder('Last Name')
        self.checkout_zipcode = page.get_by_placeholder('Zip/Postal Code')
        self.continue_btn = page.locator("#continue")
        self.finish_btn = page.locator("#finish")
        self.order_confirmation = page.locator(".complete-header").filter(has_text="Thank you for your order!")

    def checkout_details(self):
        self.checkout_first_name.fill("Pranav")
        self.checkout_last_name.fill("Patil")
        self.checkout_zipcode.fill("123456")

    def click_continue_btn(self):
        self.continue_btn.click()

    def click_finish_btn(self):
        self.finish_btn.click()

    def verify_order_confirmation(self):
        expect(self.order_confirmation).to_be_visible()