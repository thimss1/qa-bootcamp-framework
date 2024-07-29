
import logging as logger
from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators
from ssqatest.src.configs.MainConfigs import MainConfigs


class CartPage(CartPageLocators):

    endpoint = '/cart'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        base_url = MainConfigs.get_base_url()
        cart_url = base_url + self.endpoint
        self.driver.get(cart_url)

    def verify_cart_page_url(self):
        self.sl.wait_until_url_contains('/cart/')

    def get_all_product_names_in_cart(self):

        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        # import pdb; pdb.set_trace()
        return product_names

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def apply_coupon(self, coupon_code, expect_success=True):
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        if expect_success:
            displayed_notice = self.get_displayed_message()
            assert displayed_notice == 'Coupon code applied successfully.', \
                f"Applied coupon '{coupon_code}' but did not get successful messages."

    def get_displayed_message(self):
        txt = self.sl.wait_and_get_text(self.CART_PAGE_SUCCESS_MESSAGE)
        return txt

    def get_displayed_error(self):
        return self.sl.wait_and_get_text(self.ERROR_BOX)

    def click_on_proceed_to_checkout(self):
        self.sl.wait_and_click(self.PROCEED_TO_CHECKOUT_BTN)

    def get_total_label_from_bottom_table(self):
        return self.sl.wait_and_get_text(self.BOTTOM_TABLE_TOTAL_LABEL)

    def get_subtotal_label_from_bottom_table(self):
        return self.sl.wait_and_get_text(self.BOTTOM_TABLE_SUBTOTAL_LABEL)

    def get_label_for_proceed_to_checkout_button(self):
        return self.sl.wait_and_get_text(self.PROCEED_TO_CHECKOUT_BTN)

    def get_update_cart_button(self):
        btn = self.sl.wait_and_get_elements(self.UPDATE_BTN)
        assert len(btn) == 1, f"1 element expected for 'update cart' button but found {len(btn)}"
        return btn[0]

    def input_product_quantity(self, new_value):
        qty_elements = self.sl.wait_and_get_elements(self.PRODUCT_QUANTITY)
        first_product_qty_elem = qty_elements[0]
        first_product_qty_elem.clear()
        first_product_qty_elem.send_keys(str(new_value))

    def input_product_quantity_second_item(self, new_value):
        qty_elements = self.sl.wait_and_get_elements(self.PRODUCT_QUANTITY)
        first_product_qty_elem = qty_elements[1]
        first_product_qty_elem.clear()
        first_product_qty_elem.send_keys(str(new_value))

    def get_product_quantity(self):
        qty_elements = self.sl.wait_and_get_elements(self.PRODUCT_QUANTITY)
        first_product_qty_elem = qty_elements[0]
        return first_product_qty_elem.get_attribute('value')

    def click_upadete_cart(self):
        self.sl.wait_and_click(self.UPDATE_BTN)

    def get_product_quantity_second_item(self):
        qty_elements = self.sl.wait_and_get_elements(self.PRODUCT_QUANTITY)
        first_product_qty_elem = qty_elements[1]
        return first_product_qty_elem.get_attribute('value')

    def get_product_image(self):
        return self.sl.wait_and_get_elements(self.IMAGE)

    def get_cart_page_header(self):
        return self.sl.wait_and_get_text(self.CART_HEADER)

    def get_top_table_header_subtotal(self):
        return self.sl.wait_and_get_text(self.TOP_TABLE_HEADER_SUBTOTAL_LABEL)

    def get_success_message(self):
        return self.sl.wait_and_get_text(self.MESSAGE_BOX)

    def get_failure_message(self):
        return self.sl.wait_and_get_text(self.MESSAGE_BOX)

    def click_remove_item_button(self, nth_item=1):
        logger.info(f"Removing item number {nth_item} from cart")
        all_btns = self.sl.wait_until_elements_are_visible(self.REMOVE_ITEM_BUTTON)
        all_btns[int(nth_item) - 1].click()

    def get_cart_total(self):
        total_price = self.sl.wait_and_get_text(self.CART_TOTAL)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_cart_total_after_coupon(self):
        total_price = self.sl.wait_and_get_text(self.CART_TOTAL_COUPON)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_cart_total_after_coupon_expired(self):
        total_price = self.sl.wait_and_get_text(self.CART_TOTAL_COUPON_EXPIRED)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_shipping_label_from_bottom_table(self):
        return self.sl.wait_and_get_text(self.BOTTOM_TABLE_SHIPPING_LABEL)

    def get_shipping_element_from_bottom_table(self):
        return self.sl.wait_until_element_is_visible(self.BOTTOM_TABLE_SHIPPING_LABEL)

    def get_free_shipping_element_from_bottom_table(self):
        return self.sl.wait_until_element_is_visible(self.BOTTOM_TABLE_SHIPPING_FREE)

    def get_cart_heading(self):
        return self.sl.wait_and_get_text(self.CART_HEADING_LABEL)

    def get_cart_totl_label(self):
        return self.sl.wait_and_get_text(self.BOTTOM_CART_TOTAL_LABEL)

    def get_remove_coupon_button(self):
        return self.sl.wait_and_get_text(self.BOTTOM_COUPON_REMOVE_LABEL)

    def click_remove_coupon_button(self):
        return self.sl.wait_and_click(self.BOTTOM_COUPON_REMOVE_LABEL)

    def get_remove_coupon_success_message(self):
        return self.sl.wait_and_get_text(self.MESSAGE_BOX)

    def get_cart_column_header(self):
        return self.sl.wait_and_get_elements(self.CART_COLUMN_HEAD)

    def get_product_price(self):
        total_price = self.sl.wait_and_get_text(self.PRODUCT_PRICE)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_product_prices(self):
        return self.sl.wait_and_get_elements(self.PRODUCT_PRICEES)

    def get_cart_subtotal(self):
        total_price = self.sl.wait_and_get_text(self.PRODUCT_SUBTOTAL)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_column_subtotals(self):
        return self.sl.wait_and_get_elements(self.PRODUCT_SUBTOTALS_COLUMN)

    def get_column_subtotal(self):
        total_price = self.sl.wait_and_get_text(self.PRODUCT_SUBTOTAL_COLUMN)
        amount_only = total_price.replace('$', '')
        return float(amount_only)

    def get_shipping_flat_rate(self):
        return self.sl.wait_and_get_text(self.FLAT_RATE)

    def get__shipping_flat_rate_price(self):
        return self.sl.wait_and_get_text(self.FLAT_RATE_PRICE)

    def get_shipping_to_element(self):
        return self.sl.wait_until_element_is_visible(self.SHIPPING_TO)

    def get_change_address_lable(self):
        return self.sl.wait_and_get_text(self.CHANE_ADDRESS)

    def click_change_address(self):
         self.sl.wait_and_click(self.CHANE_ADDRESS)

    def get_address_form(self):
        return self.sl.wait_until_element_is_visible(self.ADDRESS_FORM)
















