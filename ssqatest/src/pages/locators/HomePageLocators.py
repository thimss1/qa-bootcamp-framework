

from selenium.webdriver.common.by import By


class HomePageLocators:

    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'a.add_to_cart_button')
    PRODUCT = (By.CSS_SELECTOR, 'ul.products li.product')
    PAGE_HEADING = (By.CSS_SELECTOR, 'header.woocommerce-products-header h1.page-title')
    NO_PRODUCT_MESSAGE = (By.CSS_SELECTOR, 'main.site-main p.woocommerce-info')
    SEARCH_MESSAGE = (By.CSS_SELECTOR, 'h1.woocommerce-products-header__title.page-title')
    VIEW_BUTTON = (By.CSS_SELECTOR, 'a.added_to_cart.wc-forward')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    DEMO_ECOM_STORE = (By.CSS_SELECTOR, 'div.site-info')
    WOOCOMERCE_LINK_FOOTER = (By.CSS_SELECTOR, 'div.site-info a')
    DROPDOWN_TOP = (By.CSS_SELECTOR, 'form.woocommerce-ordering')
    DROPDOWN_BOTTOM = (By.CSS_SELECTOR, 'form.woocommerce-ordering')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.woocommerce-Price-amount')
    PRODUCT_PRICE_PRICE = (By.CSS_SELECTOR, 'span.price del')
    SALE_BADGE = (By.CSS_SELECTOR, 'span.onsale')
    X_Z_OF_Y_RESULTS = (By.CSS_SELECTOR, 'p.woocommerce-result-count')



