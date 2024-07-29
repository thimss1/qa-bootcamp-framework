from selenium.webdriver import Keys
from ssqatest.src.selenium_extended.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators

class Header(HeaderLocators):

    expected_menu_items = ['Home', 'Cart', 'Checkout', 'My account', 'Sample Page']

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def click_on_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_RIGHT_HEADER)

    def wait_until_cart_item_count(self, count):
        expected_text = str(count) + ' item'
        self.sl.wait_until_element_contains_text(self.CART_ITEM_COUNT, expected_text)

    def get_cart_item_count(self):
        count_elem = self.sl.wait_and_get_elements(self.CART_ITEM_COUNT)
        text = count_elem[0].text
        count = text.split()[0]
        return count

    def get_all_menu_item_text(self):
        elms = self.sl.wait_and_get_elements(self.MENU_ITEMS)
        menu_text = [elm.text for elm in elms]
        return menu_text

    def assert_all_menu_items_displayed(self):
        displayed_menu_items = self.get_all_menu_item_text()
        for menu in self.expected_menu_items:
            if menu not in displayed_menu_items:
                raise Exception(f"Menu item '{menu}' is not displayed in the header.")
    def get_page_menus(self):
        return self.sl.wait_and_get_elements(self.MENU)

    def input_int_search_field(self, value):
        self.sl.wait_and_input_text(self.SEARCH_FIELD, text=value)

    def press_enter_on_search_field(self):
        self.sl.wait_and_input_text(self.SEARCH_FIELD, Keys.ENTER)

    def get_search_field(self):
        return self.sl.wait_and_get_elements(self.SEARCH_FIELD)
