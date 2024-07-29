
from ssqatest.src.pages.locators.MyAccountSignedOutLocators import MyAccountSignedOutLocators
from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ssqatest.src.configs.MainConfigs import MainConfigs
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocators):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)


    def go_to_my_account(self):
        base_url = MainConfigs.get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")

        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.debug("Clicking 'login' button.")
        self.sl.wait_and_click(self.LOGIN_BTN)

    def wait_until_error_is_displayed(self, exp_err):
        self.sl.wait_until_element_contains_text(self.ERRORS_UL, exp_err)

    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.debug("Clicking 'Register' button.")
        self.sl.wait_and_click(self.REGISTER_BTN)

    def get_login_pw_lable(self):
        return self.sl.wait_and_get_text(self.LOGIN_PW_LABEL)

    def get_login_username_lable(self):
        return self.sl.wait_and_get_text(self.LOGIN_UN_LABEL)

    def get_login_form_heading(self):
        return self.sl.wait_and_get_text(self.LOGIN_HEADING)

    def get_register_form_heading(self):
        return self.sl.wait_and_get_text(self.REGISTER_HEADING)

    def get_register_form_email_label(self):
        return self.sl.wait_and_get_text(self.REGISTER_EMAIL_LABEL)

    def get_account_heading(self):
        return self.sl.wait_and_get_text(self.ACCOUNT_HEADING)

    def login_user(self, username, password):
        self.input_login_username(username=username)
        self.input_login_password(password=password)
        self.click_login_button()





