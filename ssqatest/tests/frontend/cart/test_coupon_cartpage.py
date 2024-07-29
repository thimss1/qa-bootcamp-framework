
import pytest
import time

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.configs.MainConfigs import MainConfigs
import logging as logger
from ssqatest.src.generic_helpers.generic_coupon_helper import GenericCouponHelper


@pytest.mark.usefixtures("init_driver")
class TestCartCoupon:
    """
    A class for testing an x% coupon and verify it is applied correctly.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid44
    @pytest.mark.ecomfe53
    def test_apply_50_percent_cart_coupon(self, setup):
        """
               Test case for applying a 50% coupon code on cart items.

               Args:
                   setup: A setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        original_cart_total = self.cart.get_cart_total()

        config = MainConfigs()
        coupon_code = config.get_coupon_code('50')
        self.cart.apply_coupon(coupon_code)
        # Assert that the cart total is discounted by 50% after applying the coupon
        time.sleep(2)
        discounted_cart_total = self.cart.get_cart_total_after_coupon()
        expected_discounted_total = round(original_cart_total / 2, 2)
        assert discounted_cart_total == expected_discounted_total, f"Cart total is not discounted by 50% after applying the coupon. "


@pytest.mark.usefixtures("init_driver")
class TestCartCouponTwo:
    """
        A class for testing invalid  coupons.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid66
    @pytest.mark.ecomfe58
    def test_expired_coupon_message(self, setup):
        """
        Test case for verifying the display of an expired coupon message when expired coupon is applied.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_expired_coupon_message")
        coupon_helper = GenericCouponHelper()
        expired_coupon = coupon_helper.create_coupon(expired=True)

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        original_cart_total = self.cart.get_cart_total()

        self.cart.apply_coupon(expired_coupon, expect_success=False)
        discounted_cart_total_expired = self.cart.get_cart_total_after_coupon_expired()

        assert original_cart_total == discounted_cart_total_expired, 'Expired coupon assertion error'

    @pytest.mark.tcid121
    @pytest.mark.ecomfe55
    def test_invalid_coupon_applied_failure_message_displayed(self, setup):
        """
        Test case for verifying the display of a failure message when an invalid coupon is applied.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_invalid_coupon_applied_failure_message_displayed")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        coupon_code = "invalidcode"
        self.cart.apply_coupon(coupon_code, expect_success=False)
        time.sleep(2)

        # Assert that the failure message is displayed after applying the coupon
        success_message = self.cart.get_displayed_error()

        assert success_message == 'Coupon "invalidcode" does not exist!', "failure message is not displayed after applying coupon."


@pytest.mark.usefixtures("init_driver")
class TestCartCouponThree:
    """
     A class for testing remove coupon button.
     """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        config = MainConfigs()
        coupon_code = config.get_coupon_code('50')
        self.cart.apply_coupon(coupon_code)
        time.sleep(2)

        yield

    @pytest.mark.tcid122
    @pytest.mark.ecomfe56
    def test_remove_coupon_button_displayed(self, setup):
        """
        Test case for verifying the display of the remove coupon button.

        Args:
            setup: A setup object.
        """

        remove_button = self.cart.get_remove_coupon_button()

        # Assert that the remove coupon button is displayed
        assert remove_button == '[Remove]', "Remove coupon button is not displayed"

    @pytest.mark.tcid76
    @pytest.mark.ecomfe57
    def test_remove_coupon_button_work(self, setup):
        """
        Test case for verifying the functionality of the remove coupon button.

        Args:
            setup: A setup object.
        """

        self.cart.click_remove_coupon_button()
        time.sleep(2)
        success_message = self.cart.get_remove_coupon_success_message()

        # Assert that the remove coupon button works
        assert success_message == 'Coupon has been removed.', "Remove coupon button does not work"


@pytest.mark.usefixtures("init_driver")
class TestCartCouponFour:
    """
    A class for testing valid coupons.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.ecomfe54
    def test_coupon_applied_success_message_displayed(self, setup):
        """
        Test case for verifying the display of a success message after applying a coupon.

        Args:
            setup: A setup object
        """

        logger.info(f"Running Test: test_coupon_applied_success_message_displayed")
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()

        config = MainConfigs()
        coupon_code = config.get_coupon_code('50')

        self.cart.apply_coupon(coupon_code, expect_success=False)

        # Assert that the success message is displayed after applying the coupon
        success_message = self.cart.get_success_message()
        assert success_message == 'Coupon code applied successfully.', "Success message is not displayed after applying coupon."
