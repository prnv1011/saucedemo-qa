
class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.fleece_jacket_ATC = page.locator('[name="add-to-cart-sauce-labs-fleece-jacket"]')
        self.backpack_ATC = page.locator('[name="add-to-cart-sauce-labs-backpack"]')
        self.cart_btn = page.locator(".shopping_cart_link")

    def click_fleece_jacket_atc(self):
        self.fleece_jacket_ATC.click()

    def click_backpack_atc(self):
        self.backpack_ATC.click()

    def click_checkout_btn(self):
        self.cart_btn.click()


