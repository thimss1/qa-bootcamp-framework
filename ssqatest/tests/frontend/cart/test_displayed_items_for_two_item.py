import time

import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestCartPageSix:
    """
        Test class for verifying displayed items on the Cart page when there are two items.
    """
    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()

        yield

    @pytest.mark.ecomfe74
    def test_correct_subtotal_column_displayed_for_two_item(self, setup):
        """
        Test to verify that the correct 'subtotal column value' is displayed for two items in the cart.

        Args:
            setup:  setup object.
        """
        price = self.cart.get_product_prices()
        prices = []
        for i in range(len(price)):
            prices.append(price[i].text)

        subtotal = self.cart.get_column_subtotals()
        subtotals = []
        for i in range(len(subtotal)):
            subtotals.append(subtotal[i].text)
        assert prices[0] == subtotals[0], 'correct subtotal not displayed'
        assert prices[1] == subtotals[1], 'correct subtotal not displayed'

    @pytest.mark.ecomfe92
    def test_correct_total_displayed_for_two_item(self, setup):
        """
        Test to verify that the correct 'total' value is displayed for two items in the cart.

        Args:
            setup:  setup object.
        """
        price = self.cart.get_product_prices()
        prices = []
        for i in range(len(price)):
            prices.append(price[i].text)
        floatp = []
        for j in range(len(prices)):
            amount_only = prices[j].replace('$', '')
            floatp.append(float(amount_only))
        total = self.cart.get_cart_total()

        assert total == floatp[0] + floatp[1], "correct total not displayed for two items."

    @pytest.mark.ecomfe80
    def test_correct_subtotal_displayed_for_two_item(self, setup):
        """
        Test to verify that the correct 'subtotal cart value' is displayed for two items in the cart.

        Args:
            setup:  setup object.
        """
        price = self.cart.get_product_prices()
        prices = []
        for i in range(len(price)):
            prices.append(price[i].text)
        floatp = []
        for j in range(len(prices)):
            amount_only = prices[j].replace('$', '')
            floatp.append(float(amount_only))

        subtotal = self.cart.get_cart_subtotal()
        assert subtotal == floatp[0] + floatp[1], 'correct subtotal not displayed'

    @pytest.mark.ecomfe70
    def test_correct_price_displayed_for_two_item(self, setup):
        """
        Test to verify that the correct 'price' is displayed for two items in the cart.

        Args:
            setup:  setup object.
        """
        price = self.cart.get_product_prices()
        prices = []
        for i in range(len(price)):
            prices.append(price[i].text)

        assert prices[0] == '$11.25', 'correct price not displayed'
        assert prices[1] == '$66.44', 'correct price not displayed'




