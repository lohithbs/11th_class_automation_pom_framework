import time
import os
from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.logoutpage import LogoutPage

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("http://localhost/login.do")
        driver.maximize_window()
        driver.implicitly_wait(30)
    def test_login(self,test_launch_browser):
        lp = LoginPage(driver)
        lp.enter_user_name()
        lp.enter_pass_word()
        lp.enter_login_button()
    # def test_login(self,test_launch_browser):
    #     driver.find_element_by_name("username").send_keys("admin")
    #     driver.find_element_by_name("pwd").send_keys("manager")
    #     driver.find_element_by_id("loginButton").click()
    def test_logout(self,test_launch_browser):
        lo=LogoutPage(driver)
        lo.click_on_logout_btn()

