import time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
import pytest
from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    # Điều hướng đến trang login
    login_page.goto()
    # Gọi hàm login
    login_page.login("Admin", "admin123")
    time.sleep(5)
   
    # Kiểm tra xem đã đăng nhập thành công chưa
    assert login_page.logo().is_visible(timeout=5000)






  