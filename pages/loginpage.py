class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_text_box_name='username'
        self.password_text_box_name='pwd'
        self.loginbutton_text_box_id='loginButton'

    def enter_user_name(self):
        self.driver.find_element_by_name(self.username_text_box_name).send_keys("admin")
    def enter_pass_word(self):
        self.driver.find_element_by_name(self.password_text_box_name).send_keys("manager")
    def enter_login_button(self):
        self.driver.find_element_by_id(self.loginbutton_text_box_id).click()
