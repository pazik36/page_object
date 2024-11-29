from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_added_product(self, expected_product_name: str):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        expected_message = f"{expected_product_name} был добавлен в вашу корзину."
        assert expected_message in success_message, f'Successfull message does not contain product name. Book name: {expected_product_name}, Message: {success_message}'
    
    def should_busket_price_equals_to_product_price(self, expected_product_price: str):
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKECT_PRICE).text
        assert expected_product_price in busket_price, f'Busket price is not correct.Bussket price: {busket_price}, Book price: {expected_product_price}'

    def get_price(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        except NoSuchElementException:
            return None
        
    def get_product_name(self)->str:
        try:
            return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        except NoSuchElementException:
            return None
        

          

    