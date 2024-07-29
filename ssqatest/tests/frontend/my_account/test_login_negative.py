import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut

pytestmark = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.my_account]


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:
    """
    Set of negative tests to verify the login functionality with non-existing users.
    """

    @pytest.mark.tcid12
    @pytest.mark.ecomfe9
    @pytest.mark.smoke
    def test_login_none_existing_user(self):
        """
        Test to verify the login functionality with a non-existing user.
        """

        print("*******")
        print("TEST LOGIN NON EXISTING")
        print("*******")
        my_account = MyAccountSignedOut(self.driver)
        my_account.go_to_my_account()
        my_account.input_login_username('adfjladkf')
        my_account.input_login_password('adfadfadf')
        my_account.click_login_button()

        # verify error message
        # expected_err = 'Unknown username. Check again or try your email address.'
        expected_err = 'Error: The username adfjladkf is not registered on this site. If you are unsure of your username, try your email address instead.'
        # expected_err = 'ERROR: Invalid username. Lost your password?'
        my_account.wait_until_error_is_displayed(expected_err)