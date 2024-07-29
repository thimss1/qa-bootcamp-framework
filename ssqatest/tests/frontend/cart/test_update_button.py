import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestCartUpdateButton:
    """
    Test class to verify the functionality of the 'Update Cart' button.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid145
    @pytest.mark.ecomfe75
    def test_update_cart_button_disabled(self, setup):
        """
        Test to verify that the 'Update Cart' button is disabled initially.

        Args:
            setup: A setup object.
        """
        logger.info(f"Running Test: test_update_cart_button_disabled")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        update_cart_button = self.cart.get_update_cart_button()
        assert update_cart_button.is_enabled() == False, "'Update Cart' button is not disabled."

    @pytest.mark.tcid146
    @pytest.mark.ecomfe76
    def test_update_cart_button_enabled(self, setup):
        """
        Test to verify that the 'Update Cart' button is enabled after changing the cart quantity.

        Args:
            setup: A setup object.
        """
        logger.info(f"Running Test: test_update_cart_button_enabled")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        # Assert that the button is initially disabled
        self.cart.go_to_cart_page()
        update_cart_button = self.cart.get_update_cart_button()
        assert not update_cart_button.is_enabled(), "'Update Cart' button is not disabled initially."

        # Increase the cart quantity
        self.cart.input_product_quantity(2)

        # Assert that the button is now enabled
        assert update_cart_button.is_enabled(), "'Update Cart' button is still disabled after changing quantity."
