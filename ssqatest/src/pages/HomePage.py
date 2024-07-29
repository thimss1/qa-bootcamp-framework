

from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ssqatest.src.configs.MainConfigs import MainConfigs
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        home_url = MainConfigs.get_base_url()
        self.driver.get(home_url)

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)

    def click_second_add_to_cart_button(self):
        all_add_to_cart = self.sl.wait_and_get_elements(self.ADD_TO_CART_BTN)
        all_add_to_cart[1].click()

    def click_third_add_to_cart_button(self):
        all_add_to_cart = self.sl.wait_and_get_elements(self.ADD_TO_CART_BTN)
        all_add_to_cart[2].click()

    def click_download_product_btn(self):
        self.sl.wait_and_click(self.ADD_TO_CART_DOWNLOAD_BTN)

    def get_all_product_elements(self):
        return self.sl.wait_and_get_elements(self.PRODUCT)

    def get_displayed_heading(self):
        return self.sl.wait_and_get_text(self.PAGE_HEADING)
    def get_no_product_message(self):
        return self.sl.wait_and_get_text(self.NO_PRODUCT_MESSAGE)

    def get_search_result_success_message(self):
        return self.sl.wait_and_get_text(self.SEARCH_MESSAGE)

    def get_view_button_first_product(self):
        return self.sl.wait_and_get_text(self.VIEW_BUTTON)

    def click_first_product(self):
        return self.sl.wait_and_click(self.ADD_TO_CART_BTN)

    def get_firts_product_name(self):
        return self.sl.wait_and_get_text(self.PRODUCT_NAME)

    def get_displayed_company_name(self):
        return self.sl.wait_and_get_text(self.DEMO_ECOM_STORE)

    def get_woocommerce_link_from_footer(self):
        return self.sl.wait_and_get_text(self.WOOCOMERCE_LINK_FOOTER)

    def get_sorting_dropdown_top_page(self):
        return self.sl.wait_and_get_text(self.DROPDOWN_TOP)

    def get_sorting_dropdown_bottom_page(self):
        return self.sl.wait_and_get_text(self.DROPDOWN_BOTTOM)

    def get_product_name(self):
        return self.sl.wait_until_element_is_visible(self.PRODUCT_NAME)

    def get_product_name_text(self):
        return self.sl.wait_and_get_text(self.PRODUCT_NAME)

    def get_product_price(self):
        return self.sl.wait_until_element_is_visible(self.PRODUCT_PRICE)

    def get_sale_before_price(self):
        return self.sl.wait_until_element_is_visible(self.PRODUCT_PRICE_PRICE)

    def get_sale_badge_label(self):
        return self.sl.wait_and_get_text(self.SALE_BADGE)

    def get_sale_badge(self):
        return self.sl.wait_until_element_is_visible(self.SALE_BADGE)

    def get_add_to_cart_button(self):
        return self.sl.wait_until_element_is_visible(self.ADD_TO_CART_BTN)

    def get_x_z_result(self):
        return self.sl.wait_and_get_text(self.X_Z_OF_Y_RESULTS)


