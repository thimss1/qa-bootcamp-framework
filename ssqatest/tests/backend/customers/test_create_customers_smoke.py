
import pytest
import logging as logger
from ssqatest.src.utilities.genericUtilities import generate_random_email_and_password
from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.dao.customers_dao import CustomersDAO
from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
# from ssqatest.src.utilities.requestsUtility import RequestsUtility


@pytest.fixture(scope='function')
def create_user_email_password_only():
    """
       Function to create a user with email and password only.
       return:
        email
        password
        api response

    """

    rand_info = generate_random_email_and_password()

    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomersAPIHelper()
    cust_api_info = cust_obj.call_create_customer(email=email, password=password)

    data = {"email": email, "password": password, "api_response": cust_api_info}

    return data


@pytest.mark.customers
@pytest.mark.ecombe1
@pytest.mark.tcid29
def test_create_customer_only_email_password():
    """
     Test case to create a new customer with email and password only.
    """

    logger.info("TEST: Create new customer with email and password only.")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomersAPIHelper()
    cust_api_info = cust_obj.call_create_customer(email=email, password=password)

    # verify email and first name in the response
    assert cust_api_info['email'] == email, f"Create customer api return wrong email. Email: {email}"
    assert cust_api_info['first_name'] == '', f"Create customer api returned value for first_name" \
                                              f"but it should be empty. "

    # verify customer is created in database
    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']
    assert id_in_api == id_in_db, f'Create customer response "id" not same as "ID" in database.' \
                                  f'Email: {email}'


@pytest.mark.customers
@pytest.mark.ecombe6
@pytest.mark.tcid47
def test_create_customer_fail_for_existing_email():
    """
        Test case to verify that creating a customer with an existing email fails with the correct error message.
    """

    # get existing email from db
    cust_dao = CustomersDAO()

    existing_cust = cust_dao.get_random_customer_from_db()
    existing_email = existing_cust[0]['user_email']

    cust_obj = CustomersAPIHelper()
    cust_api_info = cust_obj.call_create_customer(email=existing_email, password="Password1", expected_status_code=400)

    assert cust_api_info['code'] == 'registration-error-email-exists', f"Create customer with" \
       f"existing user error 'code' is not correct. Expected: 'registration-error-email-exists', " \
        f"Actual: {cust_api_info['code']}"

    assert cust_api_info['message'] == 'An account is already registered with your email address. <a href="#" class="showlogin">Please log in.</a>', \
        f"Create customer with existing user error 'message' is not correct. " \
        f"Expected: 'An account is already registered with your email address. Please log in.', " \
        f"Actual: '{cust_api_info['message']}'"


@pytest.mark.customers
@pytest.mark.ecombe3
@pytest.mark.tcid32
def test_create_customer_fail_when_no_password_is_provided():
    """
        Test case to verify that creating a customer without providing a password fails with the correct error message.
    """

    rand_info = generate_random_email_and_password()
    email = rand_info['email']

    payload = {"email": email}

    woo_api_utility = WooAPIUtility()
    response_json = woo_api_utility.post('customers', params=payload, expected_status_code=400)

    expected_response = {'code': 'rest_missing_callback_param', 'message': 'Missing parameter(s): password', 'data': {'status': 400, 'params': ['password']}}
    assert response_json == expected_response, f"Got unexpected error creating user without password." \
                                               f"Expected response: {expected_response}." \
                                               f"Actual response: {response_json}"


@pytest.mark.customers
@pytest.mark.ecombe4
@pytest.mark.tcid45
def test_create_customer_names_should_be_empty_string_if_not_provided():
    """
    Alternate tc name:
        Verify create customer with only email and password has names as empty string
    """

    logger.info("TEST: Verify create customer with only email and password has names as empty string")

    rand_info = generate_random_email_and_password()
    email = rand_info['email']
    password = rand_info['password']

    # make the call
    cust_obj = CustomersAPIHelper()
    cust_api_info = cust_obj.call_create_customer(email=email, password=password)

    assert cust_api_info['first_name'] == '', f"Creating user without providing name expected to create first_name='' but it was first_name={cust_api_info['first_name']}"
    assert cust_api_info['last_name'] == '', f"Creating user without providing name expected to create last_name='' but it was first_name={cust_api_info['last_name']}"


@pytest.mark.customers
@pytest.mark.ecombe5
@pytest.mark.tcid46
def test_user_name_is_autogenerated_based_on_email(create_user_email_password_only):
    """
    Alternate tc name:
        Verify 'username' is autogenerated based on email

    Test case to verify a username is autogenerated based on email.
    Args:
        create_user_email_password_only

    """

    logger.info("TEST: Verify 'username' is autogenerated based on email")

    api_username = create_user_email_password_only['api_response']['username']
    email = create_user_email_password_only['email']
    expected_username = email.split('@')[0]
    assert api_username == expected_username, f"Creating user with only email and password should've created user name based on email." \
                                              f"Expected username: {expected_username}, Actual username: {api_username}"
