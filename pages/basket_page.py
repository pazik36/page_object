from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_busket_be_empty_message(self):
        busket_message = self.browser.find_element(*BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text
        assert "Your basket is empty" in busket_message, "Busket is not emapty"

    def should_busket_form_be_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_FORM),'Basket is not empty'