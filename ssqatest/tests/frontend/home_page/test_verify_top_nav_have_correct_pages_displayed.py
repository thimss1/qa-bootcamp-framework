import time

import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestTopNavMenu:
    """
    Test class to verify the functionality of the top navigation menu.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.account = MyAccountSignedOut(self.driver)
        request.cls.cart = CartPage(self.driver)

        yield

    @pytest.mark.tcid73
    @pytest.mark.ecomfe21
    def test_top_nav_displayed_right_page(self, setup):
        """
        Test to verify that the top navigation menu displays the correct pages.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_top_nav_displayed_right_page")

        menus = ['Home', 'Cart', 'Checkout', 'My account', 'Sample Page']
        self.homepage.go_to_home_page()
        time.sleep(20)
        page_menu = self.header.get_all_menu_item_text()

        # Assert that the top nav menu displayed the correct pages
        for i in range(len(menus)):
            assert page_menu[i] == menus[i], 'top nav displayed wrong menus'

    @pytest.mark.ecomfe22
    def test_top_nav_menu_opens_right_page(self, setup):
        """
        Test to verify that the top navigation menu opens the correct pages.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test:  test_top_nav_menu_opens_right_page")

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        displayed_heading = self.homepage.get_displayed_heading()
        assert displayed_heading == 'Shop', "Home menu does not open home page"

        self.cart.go_to_cart_page()
        cart_header = self.cart.get_cart_page_header()
        assert cart_header == 'Cart', "Cart menu does not open cart page"

        self.checkout.go_to_checkout_page()
        checkout_header = self.checkout.get_checkout_header()
        assert checkout_header == 'Checkout', "Checkout menu does not open checkout page"

        self.account.go_to_my_account()
        account_header = self.account.get_account_heading()
        assert account_header == 'My account', "My account menu does not open my account page"
