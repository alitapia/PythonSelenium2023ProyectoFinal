from src.page_objects.checkout_page import CheckoutPage
from src.page_objects.home_page import HomePage
from src.page_objects.search_page import SearchPage


def test_no_product_validation(web_drivers):
    expected_value = "Samsung Galaxy Tab 10.1"
    expected_error_message = "Products marked with *** are not available in the desired quantity or not in stock!\n×"
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("galaxy")
    search_page = SearchPage(*web_drivers)
    search_page.open()
    search_page.add_to_cart()
    search_page.go_to_checkout()
    checkout_page = CheckoutPage(*web_drivers)
    checkout_page.open()
    actual_value = checkout_page.get_warning_message()
    assert expected_error_message == actual_value.text

