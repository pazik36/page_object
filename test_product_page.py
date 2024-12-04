from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
                                   ,
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

def test_guest_can_add_product_to_basket(browser, link):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)

    product_page.open()

    product_name = product_page.get_product_name()
    product_price = product_page.get_price()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_about_added_product(product_name)
    product_page.should_busket_price_equals_to_product_price(product_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page = ProductPage(browser,link, 0)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link,0)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

    page=ProductPage(browser,link,0)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_success_message()