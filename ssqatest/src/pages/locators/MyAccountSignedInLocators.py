
from selenium.webdriver.common.by import By


class MyAccountSignedInLocators:

    LEFT_NAV_LOGOUT_BTN = (By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link--customer-logout')
    LEFT_NAV_ELM = (By.CSS_SELECTOR,'div.woocommerce nav.woocommerce-MyAccount-navigation ul li')
    DOWNLOAD_LABEL = (By.CSS_SELECTOR,'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--downloads a')
    DOWNLOAD_PRODUCT = (By.CSS_SELECTOR, 'td.download-file a')
    DOWNLOAD_ORDER = (By.CSS_SELECTOR,'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--orders a')