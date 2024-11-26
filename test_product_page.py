from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)

    product_page.open()

    product_name = product_page.get_product_name()
    product_price = product_page.get_price()

    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_about_added_product(product_name)
    product_page.should_busket_price_equals_to_product_price(product_price)

