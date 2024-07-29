import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestCartProductImage:
    """
    Test class for verifying product images displayed in the cart.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid136
    @pytest.mark.ecomfe66
    def test_product_image_displayed_1_item_in_cart(self, setup):
        """
        Test to verify that the product image is displayed for 1 item in the cart.

        Args:
            setup:  setup object.
        """

        logger.info(f"Running Test: test_product_image_displayed")
        self.homepage.go_to_home_page()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()

        product_image = self.cart.get_product_image()
        img_elem = product_image[0]

        # Assert that the product image is displayed
        assert img_elem.is_displayed(), "Product image is not displayed."
        img_src = img_elem.get_attribute('src')
        assert img_src.endswith('.jpg'), "The product image link does not have expected extension. "

    @pytest.mark.ecomfe67
    def test_image_displayed_for_two_items(self, setup):

        """
        Test to verify that the product images are displayed for 2 items in the cart.

        Args:
            setup:  setup object.
        """
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()

        product_image = self.cart.get_product_image()
        img_elem = product_image[0]
        img_two = product_image[1]

        # Assert that the product image is displayed
        assert img_elem.is_displayed(), "Product image  is not displayed."
        assert img_two.is_displayed(), "Product image is not displayed."


