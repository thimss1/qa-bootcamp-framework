

from selenium.webdriver.common.by import By

class HeaderLocators:

    CART_RIGHT_HEADER = (By.ID, 'site-header-cart')
    CART_ITEM_COUNT = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')
    MENU_ITEMS = (By.CSS_SELECTOR, 'div.menu ul.nav-menu li')
    MENU = (By.CSS_SELECTOR, 'ul.nav-menu li')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input#woocommerce-product-search-field-0')