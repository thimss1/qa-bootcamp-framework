import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestLoginForm:
    """
    Set of tests to verify the login form functionality on the My Account page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.signout = MyAccountSignedOut(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid6
    @pytest.mark.ecomfe103
    def test_my_account_page_has_login_form(self, setup):
        """
        Test to verify that the My Account page has a login form.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_my_account_page_has_login_form")
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()

        Login_label = self.signout.get_login_form_heading()

        # Assert that my account page has login form
        assert Login_label == 'Login', "my account page does nto have a login form"

    @pytest.mark.tcid8
    @pytest.mark.ecomfe105
    def test_login_username_label(self, setup):
        """
        Test to verify the label for the login username field on the My Account page.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_login_username_label")
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()

        login_username = self.signout.get_login_username_lable()

        # Assert that login username label is correct
        assert login_username == 'Username or email address *', "my account page login username label is not correct"

    @pytest.mark.tcid9
    @pytest.mark.ecomfe106
    def test_login_password_label(self, setup):
        """
        Test to verify the label for the login password field on the My Account page.

        Args:
            setup: A setup object
        """

        logger.info(f"Running Test: test_login_password_label")
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()

        login_password = self.signout.get_login_pw_lable()

        # Assert that login password label is correct
        assert login_password == 'Password *', "my account page login password label is not correct"

