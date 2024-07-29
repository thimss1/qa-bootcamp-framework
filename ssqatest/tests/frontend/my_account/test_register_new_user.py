
import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.utilities.genericUtilities import generate_random_email_and_password


pytestmark = [pytest.mark.fe, pytest.mark.regression, pytest.mark.smoke, pytest.mark.my_account]


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:
    """
    Test class to verify the registration of a new user.
     """

    @pytest.mark.tcid13
    @pytest.mark.ecomfe10
    def test_register_valid_new_user(self):
        """
        Test to verify register of a valid new user.

        Args:
            setup: A setup object.
        """
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)

        my_account_o.go_to_my_account()

        rand_email = generate_random_email_and_password()
        my_account_o.input_register_email(rand_email["email"])
        my_account_o.input_register_password('1234abc11!!')
        my_account_o.click_register_button()

        # verify user is registered
        my_account_i.verify_user_is_signed_in()