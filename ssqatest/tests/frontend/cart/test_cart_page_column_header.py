import time
import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestCartPageColumnHeader:
    """
       A class for testing the column header of the cart page.

    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)

        yield

    @pytest.mark.ecomfe61
    def test_cart_page_column_header(self, setup):
        """
        Test case for verifying the column headers on the cart page.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_cart_page_column_header")
        column_headers = ['Remove item', 'Thumbnail image', 'Product', 'Price', 'Quantity', 'Subtotal']
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
        self.cart.go_to_cart_page()
        headers = self.cart.get_cart_column_header()
        ht = []
        for i in range(len(headers)):
            ht.append(headers[i].text)
        for i in range(len(ht)):
            assert ht[i] == column_headers[i], 'cart page column displayed wrong headers'
