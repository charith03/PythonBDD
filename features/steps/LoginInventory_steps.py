from behave import given, when, then
from playwright.sync_api import expect

from Pages.LoginPage import LoginInventory

saucedemo_page = None


@given('I login to SauceDemo and verify inventory page')
def step_login(context):

    global saucedemo_page
    saucedemo_page = LoginInventory(context.page)
    saucedemo_page.loginPage()
    expect(context.page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("Login Successful")

@when('I verify inventory details')
def verify_inventory(context):
    saucedemo_page.verify_inventory()

@when('I add random products to cart')
def add_products(context):
    saucedemo_page.add_random_products()

@when('I enter checkout information')
def checkout(context):
    saucedemo_page.checkout()


@then('order should be placed successfully')
def order_success(context):
    saucedemo_page.finish_order()
    expect(context.page).to_have_url(
        "https://www.saucedemo.com/checkout-complete.html")
    print("Order placed successfully")

@then('I navigate back to inventory page')
def back_home(context):
    saucedemo_page.back_to_home()
    expect(context.page).to_have_url(
        "https://www.saucedemo.com/inventory.html")
    print("Returned to Inventory Page")