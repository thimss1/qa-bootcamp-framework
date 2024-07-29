import time

import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestRemoveOneCartItem:
    """
    Test class to verify the removal of  item from the cart.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid132
    @pytest.mark.ecomfe62
    def test_remove_one_item_from_cart(self, setup):
        """
        Test to verify the removal of one item from the cart.

        Args:
            setup: A setup object.
        """
        logger.info(f"Running Test: test_remove_one_item_from_cart")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        self.cart.click_remove_item_button()
        time.sleep(10)
        # Assert that one item is removed from cart when the 'X' button is clicked
        self.header.wait_until_cart_item_count(0)
        cart_item_count = self.header.get_cart_item_count()
        assert int(cart_item_count) == 0, "Item is not removed from cart when the 'X' button is clicked."

    @pytest.mark.tcid133
    @pytest.mark.ecomfe63
    def test_remove_item_from_cart_when_2_items_in_cart(self, setup):
        """
        Test to verify the removal of an item from the cart when there are 2 items in the cart.

        Args:
            setup: A setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()
        self.cart.click_remove_item_button()

        # Assert that the item is removed from cart when the 'X' button is clicked
        self.header.wait_until_cart_item_count(1)
        cart_item_count = self.header.get_cart_item_count()

        assert int(cart_item_count) == 1, "Item is not removed from cart when the 'X' button is clicked."


@pytest.mark.usefixtures("init_driver")
class TestRemoveOneCartItemTwo:
    """
    Another test class to verify the removal  item from the cart.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)

        yield

    @pytest.mark.ecomfe64
    def test_remove_item_from_cart_with_multiple_quantity(self, setup):
        """
        Test to verify the removal of an item with multiple quantities from the cart.

        Args:
            setup: A setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        self.cart.input_product_quantity(3)
        self.cart.click_remove_item_button()

        self.header.wait_until_cart_item_count(0)
        cart_item_count = self.header.get_cart_item_count()

        assert int(cart_item_count) == 0, "Item with multiple quantity not removed"

    @pytest.mark.ecomfe65
    def test_remove_multiple_items_from_cart(self, setup):
        """
        Test to verify the removal of multiple items from the cart.

        Args:
            setup: A setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()
        self.cart.click_remove_item_button()
        time.sleep(10)
        self.cart.click_remove_item_button()

        self.header.wait_until_cart_item_count(0)
        cart_item_count = self.header.get_cart_item_count()

        assert int(cart_item_count) == 0, "Multiple items are not removed from cart when the 'X' button is clicked."


@pytest.mark.usefixtures("init_driver")
class TestRemoveOneCartItemThree:
    """
    Another test class to verify the removal  item from the cart.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)

        yield

    @pytest.mark.ecomfe81
    def test_correct_subtotal_displayed_after_product_removed(self, setup):
        """
        Test to verify that the correct subtotal is displayed after removing a product.

        Args:
            setup: A setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()
        price = self.cart.get_product_prices()
        prices = []
        for i in range(len(price)):
            prices.append(price[i].text)
        floatp = []
        for j in range(len(prices)):
            amount_only = prices[j].replace('$', '')
            floatp.append(float(amount_only))
        subtotal_before = self.cart.get_cart_subtotal()
        self.cart.click_remove_item_button()
        time.sleep(20)
        subtotal_after = self.cart.get_cart_subtotal()
        assert subtotal_after == subtotal_before - floatp[0], "correct subtotal not displayed after product removed"