import time

from selenium import webdriver
def test_launch_browser():
    global driver
    driver=webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("http://localhost/login.do")
    driver.maximize_window()
    driver.implicitly_wait(30)
def test_login():
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("pwd").send_keys("manager")
    driver.find_element_by_id("loginButton").click()
def test_logout():
    time.sleep(5)
    driver.find_element_by_class_name("logout").click()
    time.sleep(3)
    driver.quit()
