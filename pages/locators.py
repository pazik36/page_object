from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p")
    BUSKECT_PRICE = (By.CSS_SELECTOR, "div.alert-info .alertinner strong")