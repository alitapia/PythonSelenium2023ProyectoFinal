from src.page_objects.home_page import HomePage
from src.page_objects.product_page import ProductPage
from src.page_objects.search_page import SearchPage


def test_get_product_price(web_drivers):
    expected_price = "$241.99"
    expected_product = "Samsung Galaxy Tab 10.1"
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("galaxy")
    search_page = SearchPage(*web_drivers)
    search_page.get_product_name().click()
    product_page = ProductPage(*web_drivers)
    actual_product = product_page.get_product_name()
    assert expected_product == actual_product.text
    actual_price = product_page.get_price()
    assert expected_price == actual_price, f"Product price should be {expected_price}"



