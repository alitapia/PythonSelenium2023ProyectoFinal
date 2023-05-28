from src.page_objects.home_page import HomePage
from src.page_objects.search_page import SearchPage


def test_search(web_drivers):
    expected_value = "Samsung Galaxy Tab 10.1"
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("galaxy")
    search_page = SearchPage(*web_drivers)
    search_page.open()
    actual_value = search_page.get_product_name()
    assert expected_value == actual_value.text
