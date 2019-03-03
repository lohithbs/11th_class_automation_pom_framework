class LogoutPage:
    def __init__(self,driver):
        self.driver=driver
        self.logout_btn_class="logout"
    def click_on_logout_btn(self):
        self.driver.find_element_by_class_name(self.logout_btn_class).click()
