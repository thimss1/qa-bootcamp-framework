import time

import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestHomePage:
    """
    Test class  to verify  displayed items on  home page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.account = MyAccountSignedOut(self.driver)

        yield

    @pytest.mark.ecomfe24
    def test_each_product_name_displayed(self, setup):
        """
        Test to verify that each product name is displayed on the home page.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        products = self.homepage.get_all_product_elements()
        for i in products:
            name = self.homepage.get_product_name()
            assert name.is_displayed(), "Product name is not displayed."

    @pytest.mark.ecomfe25
    def test_each_product_price_displayed(self, setup):
        """
        Test to verify that each product price is displayed on the home page.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        products = self.homepage.get_all_product_elements()
        for i in products:
            price = self.homepage.get_product_price()
            assert price.is_displayed(), "Product price is not displayed."

    @pytest.mark.ecomfe26
    def test_sale_badge_displayed(self, setup):
        """
        Test to verify that the sale badge is displayed for products that are on sale.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        products = self.homepage.get_all_product_elements()
        for i in products:
            if self.homepage.get_sale_before_price():
                sale_badge = self.homepage.get_sale_badge()
                assert sale_badge.is_displayed(),"sale badge not displayed"

    @pytest.mark.ecomfe27
    def test_each_product_add_to_cart_button_displayed(self, setup):
        """
        Test to verify that each product's add to cart button is displayed.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        products = self.homepage.get_all_product_elements()
        for i in products:
            btn = self.homepage.get_add_to_cart_button()
            assert btn.is_displayed(), "Product add button is not displayed."

    @pytest.mark.ecomfe32
    def test_sale_item_has_two_prices(self, setup):
        """
        Test to verify that products that are on sale have two prices displayed.

        Args:
            setup: A setup object
        """
        self.homepage.go_to_home_page()
        products = self.homepage.get_all_product_elements()
        for i in products:
            if self.homepage.get_sale_before_price():
                sale_price = self.homepage.get_product_price()
                assert sale_price.is_displayed(), "item on sale does nto have two prices"








