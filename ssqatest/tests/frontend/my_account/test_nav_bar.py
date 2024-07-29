import time

import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestLeftNav:
    """
    Set of tests to verify the left navigation functionality on the My Account page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.signout = MyAccountSignedOut(self.driver)
        request.cls.signin = MyAccountSignedIn(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()
        email = 'testuser@gmail.com'
        pw = '123uesr123test'
        self.signout.input_login_username(email)
        self.signout.input_login_password(pw)
        self.signout.click_login_button()
        yield

    @pytest.mark.tcid6
    @pytest.mark.ecomfe14
    def test_left_nav_has_six_elements(self, setup):
        """
        Test to verify that the left navigation on the My Account page has six elements.

        Args:
            setup: A setup object
        """

        logger.info(f"Running Test: test_left_nav_has_six_elements")
        nav_items = self.signin.get_left_nav_elm()

        assert len(nav_items) == 6, 'the left nav element does not have six elements'

    @pytest.mark.tcid8
    @pytest.mark.ecomfe15
    def test_left_nav_has_download_label(self, setup):
        """
        Test to verify the label for the "Downloads" element in the left navigation.

        Args:
            setup: A setup object
        """

        logger.info(f"test_left_nav_has_download_label")
        download = self.signin.get_download_label_account_page()

        assert download == 'Downloads',"download label not found"

    @pytest.mark.tcid9
    @pytest.mark.ecomfe16
    def test_left_nav_has_order_label(self, setup):
        """
        Test to verify the label for the "Orders" element in the left navigation.

        Args:
            setup: A setup object
        """

        logger.info(f"test_left_nav_has_order_label")
        download = self.signin.get_order_label_account_page()

        assert download == 'Orders', "orders label not found"

