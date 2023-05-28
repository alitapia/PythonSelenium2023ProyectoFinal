from src.page_objects.home_page import HomePage


def test_search(web_drivers):
    home_page = HomePage(*web_drivers)
    home_page.open()
    home_page.search("Iphone")


def test_home_page_menus(web_drivers):
    expected_top_menu_options = ["My Account", "Wish List (0)", "Shopping Cart", "Checkout"]
    home_page = HomePage(*web_drivers)
    home_page.open()
    actual_top_menu_options = home_page.get_top_menu_options()
    for menu_option in expected_top_menu_options:
        assert menu_option in actual_top_menu_options, f"Home top menu options should include {menu_option}"
