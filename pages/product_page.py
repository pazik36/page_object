from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_message_about_added_book(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text

        assert book_name in success_message, f'Successfull message does not contain book name. Book name: {book_name}, Message: {success_message}'
    
    def should_busket_price_equals_to_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        busket_price = self.browser.find_element(*ProductPageLocators.BUSKECT_PRICE).text

        assert book_price in busket_price, f'Busket price is not correct.Bussket price: {busket_price}, Book price: {book_price}'
        
    