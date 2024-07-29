
from selenium.webdriver.common.by import By

class MyAccountSignedOutLocators:

    LOGIN_USER_NAME = (By.ID, 'username')
    LOGIN_PASSWORD = (By.ID, 'password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[value="Log in"]')

    ERRORS_UL = (By.CSS_SELECTOR, 'ul.woocommerce-error')

    REGISTER_EMAIL = (By.ID, 'reg_email')
    REGISTER_PASSWORD = (By.ID, 'reg_password')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[value="Register"]')

    LOGIN_PW_LABEL = (By.CSS_SELECTOR, 'label[for="password"]')
    LOGIN_UN_LABEL = (By.CSS_SELECTOR, 'label[for="username"]')
    LOGIN_HEADING = (By.CSS_SELECTOR, 'div.u-column1.col-1 h2')

    REGISTER_HEADING = (By.CSS_SELECTOR, 'div.u-column2.col-2 h2')
    REGISTER_EMAIL_LABEL = (By.CSS_SELECTOR, 'label[for="reg_email"]')
    ACCOUNT_HEADING = (By.CSS_SELECTOR, 'header.entry-header h1')