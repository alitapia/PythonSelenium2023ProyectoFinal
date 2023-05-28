
from src.page_objects.register_page import RegisterPage


def test_success_register(web_drivers):
    expected_msg = "Your Account Has Been Created!"
    register_page = RegisterPage(*web_drivers)
    register_page.open()
    register_page.register_user("Testatr", "Test", "test@qaminds.com", "123456789", "testpass")
    actual_msg = register_page.get_success_message()
    assert expected_msg == actual_msg, f"Success message should be{expected_msg}"
