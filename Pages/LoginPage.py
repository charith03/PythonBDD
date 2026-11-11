import random

from Locators.LoginPage_Locotors import LoginAndInventory
from Test_Data.LoginCredentials import LoginCreds
from Test_Data.Urls import SiteURL


class LoginInventory:
    def __init__(self, page):

        self.page = page
        self.Username = page.locator(LoginAndInventory.username)
        self.password = page.locator(LoginAndInventory.password)
        self.loginBtn = page.locator(LoginAndInventory.loginButton)
        self.products = page.locator(LoginAndInventory.ProductNames)
        self.productPrices = page.locator(LoginAndInventory.ProductPrices)
        self.cartButtons = page.locator(LoginAndInventory.AddToCart)
        self.CartBtn = page.locator(LoginAndInventory.cart)
        self.checkoutBtn = page.locator(LoginAndInventory.checkout)
        self.Fname = page.locator(LoginAndInventory.first_name)
        self.Lname = page.locator(LoginAndInventory.last_name)
        self.postalCode = page.locator(LoginAndInventory.postal_code)
        self.continueBtn = page.locator(LoginAndInventory.conutinue_checkout)
        self.finishBtn = page.locator(LoginAndInventory.finish_checkout)
        self.backHomeBtn = page.locator(LoginAndInventory.back_home)

    def loginPage(self):

        self.page.goto(SiteURL.BASE_URL)
        self.Username.fill(LoginCreds.user)
        self.password.fill(LoginCreds.password)
        self.loginBtn.click()

    def verify_inventory(self):
        count = self.products.count()
        print(f"Total Products: {count}")
        for i in range(count):
            product_name = self.products.nth(i)
            product_price = self.productPrices.nth(i)
            add_cart = self.cartButtons.nth(i)
            assert product_name.is_visible()
            assert product_price.is_visible()
            assert add_cart.is_visible()
        print("Inventory Validation Completed")

    def add_random_products(self):
        count = self.cartButtons.count()
        random_indexes = random.sample(
            range(count),
            3
        )
        for i in random_indexes:
            product = self.products.nth(i).inner_text()
            print(f"Adding Product: {product}")
            self.cartButtons.nth(i).click()
        self.CartBtn.click()
        print(f"Added products indexes: " f"{random_indexes}")

    def checkout(self):
        self.checkoutBtn.click()
        self.Fname.fill("Charith")
        self.Lname.fill("Bandi")
        self.postalCode.fill("521139")
        self.continueBtn.click()
        print("Checkout information entered")

    def finish_order(self):
        self.finishBtn.click()
        print("Checkout Finished")

    def back_to_home(self):
        self.backHomeBtn.click()
        print("Back To Inventory Page")