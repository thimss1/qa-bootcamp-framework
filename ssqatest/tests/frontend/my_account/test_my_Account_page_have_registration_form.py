import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestRegisterForm:
    """
    Set of tests to verify the register form functionality on the My Account page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.signout = MyAccountSignedOut(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid7
    @pytest.mark.ecomfe104
    def test_my_account_page_has_register_form(self, setup):
        """
        Test to verify that the My Account page has a register form.

        Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_my_account_page_has_register_form")
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()

        Register_label = self.signout.get_register_form_heading()

        # Assert that my account page has register form
        assert Register_label == 'Register', "my account page does not have a registration form."

    @pytest.mark.tcid15
    @pytest.mark.ecomfe12
    def test_register_email_address_label(self, setup):
        """
        Test to verify the label for the email address field on the register form.

       Args:
            setup: A setup object
        """
        logger.info(f"Running Test: test_register_email_address_label")
        self.homepage.go_to_home_page()
        self.signout.go_to_my_account()

        Register_email = self.signout.get_register_form_email_label()

        assert Register_email == 'Email address *', "my account page register email label is not correct."

