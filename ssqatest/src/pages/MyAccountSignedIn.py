
from ssqatest.src.pages.locators.MyAccountSignedInLocators import MyAccountSignedInLocators
from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended


class MyAccountSignedIn(MyAccountSignedInLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_user_is_signed_in(self):
        self.sl.wait_until_element_is_visible(self.LEFT_NAV_LOGOUT_BTN)

    def get_left_nav_elm(self):
        return self.sl.wait_and_get_elements(self.LEFT_NAV_ELM)

    def get_download_label_account_page(self):
        return self.sl.wait_and_get_text(self.DOWNLOAD_LABEL)

    def get_order_label_account_page(self):
        return self.sl.wait_and_get_text(self.DOWNLOAD_ORDER)

    def click_on_downloads_tab(self):
        self.sl.wait_and_click(self.DOWNLOAD_LABEL)

    def click_download_link(self):
        self.sl.wait_and_click(self.DOWNLOAD_PRODUCT)