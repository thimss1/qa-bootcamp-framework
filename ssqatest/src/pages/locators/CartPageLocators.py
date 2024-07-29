
from selenium.webdriver.common.by import By


class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    REMOVE_ITEM_BUTTON = (By.CSS_SELECTOR, 'a.remove')
    COUPON_FIELD = (By.ID, 'coupon_code')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    CART_HEADER = (By.CSS_SELECTOR, 'h1[class=entry-title]')
    SUB_TOTAL_TOP_TABLE_HEADER = (By.CSS_SELECTOR, 'form.woocommerce-cart-form table th.product-subtotal')
    TOP_TABLE_HEADER_SUBTOTAL_LABEL = (By.CSS_SELECTOR, 'form.woocommerce-cart-form table th.product-subtotal')
    BOTTOM_TABLE_TOTAL_LABEL = (By.CSS_SELECTOR, 'div.cart_totals table.shop_table.shop_table_responsive tr.order-total th')
    BOTTOM_TABLE_SUBTOTAL_LABEL = (By.CSS_SELECTOR, 'div.cart_totals table.shop_table.shop_table_responsive tr.cart-subtotal th')
    BOTTOM_TABLE_SHIPPING_LABEL = (By.CSS_SELECTOR, 'div.cart_totals table.shop_table.shop_table_responsive tr.woocommerce-shipping-totals.shipping th')
    CART_HEADING_LABEL = (By.CSS_SELECTOR, 'header.entry-header h1')
    BOTTOM_CART_TOTAL_LABEL = (By.CSS_SELECTOR, 'div.cart_totals h2')
    BOTTOM_COUPON_REMOVE_LABEL = (By.CSS_SELECTOR, 'a.woocommerce-remove-coupon')

    CART_PAGE_SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.woocommerce-notices-wrapper div.woocommerce-message')
    ERROR_BOX = (By.CSS_SELECTOR, 'div.woocommerce-notices-wrapper ul.woocommerce-error')
    MESSAGE_BOX = (By.CSS_SELECTOR, 'div.woocommerce-notices-wrapper')
    IMAGE = (By.CSS_SELECTOR, 'img.attachment-woocommerce_thumbnail.size-woocommerce_thumbnail')
    PROCEED_TO_CHECKOUT_BTN = (By.CSS_SELECTOR, 'a.checkout-button.button.alt.wc-forward')
    QUANTITY_ARROW = (By.CSS_SELECTOR, '#quantity_64c8981017429')
    CART_TOTAL_COUPON = (By.CSS_SELECTOR, 'div.cart_totals tr.cart-discount td[data-title="Coupon: code50"] span.woocommerce-Price-amount.amount')
    CART_TOTAL_COUPON_EXPIRED = (By.CSS_SELECTOR, 'div.cart_totals tr.cart-discount span.woocommerce-Price-amount.amount')
    CART_TOTAL = (By.CSS_SELECTOR, 'div.cart_totals tr.order-total td[data-title="Total"] span.woocommerce-Price-amount.amount')
    UPDATE_BTN = (By.CSS_SELECTOR, 'button[name="update_cart"]')
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, 'td.product-quantity div.quantity input.input-text.qty.text')
    CART_COLUMN_HEAD = (By.CSS_SELECTOR, 'table.shop_table thead tr th')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'span.woocommerce-Price-amount')
    PRODUCT_SUBTOTAL = (By.CSS_SELECTOR, 'tr.cart-subtotal span.woocommerce-Price-amount')
    PRODUCT_SUBTOTAL_COLUMN = (By.CSS_SELECTOR, 'td.product-subtotal span.woocommerce-Price-amount')
    FLAT_RATE = (By.CSS_SELECTOR, 'label[for="shipping_method_0_flat_rate2"]')
    FLAT_RATE_PRICE = (By.CSS_SELECTOR, 'label[for="shipping_method_0_flat_rate2"] span.woocommerce-Price-amount')
    SHIPPING_TO = (By.CSS_SELECTOR,'p.woocommerce-shipping-destination')
    CHANE_ADDRESS = (By.CSS_SELECTOR,'form.woocommerce-shipping-calculator a.shipping-calculator-button')
    ADDRESS_FORM = (By.CSS_SELECTOR,'section.shipping-calculator-form')
    PRODUCT_PRICEES = (By.CSS_SELECTOR,'tr.woocommerce-cart-form__cart-item td.product-price')
    PRODUCT_SUBTOTALS_COLUMN = (By.CSS_SELECTOR,'tr.woocommerce-cart-form__cart-item td.product-subtotal')
    BOTTOM_TABLE_SHIPPING_FREE = (By.CSS_SELECTOR, 'div.cart_totals table.shop_table tr.woocommerce-shipping-totals.shipping ul.woocommerce-shipping-methods label[for="shipping_method_0_free_shipping1"]')



