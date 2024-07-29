from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.dao.customers_dao import CustomersDAO
from ssqatest.src.utilities import genericUtilities as gu
import pytest


@pytest.mark.customer
@pytest.mark.ecombe11
@pytest.mark.tcid214
def test_update_customer_data():
    """
    Test case to verify the functionality of updating customer data.
    """
    cust_helper = CustomersAPIHelper()
    cust_obj = CustomersDAO()
    first_name_length = 5
    last_name_length = 6
    first_name = gu.generate_random_string(first_name_length)
    last_name = gu.generate_random_string(last_name_length)
    rand_customer = cust_obj.get_random_customer_from_db()
    id_in_db = rand_customer[0]['ID']
    data = {
        "first_name": first_name,
        "last_name" :  last_name,
        "billing": {
            "first_name": first_name,
            "last_name": last_name,
        },
        "shipping": {
            "first_name": first_name,
            "last_name": last_name,
        }
           }
    payload = dict(data)
    updated_cust = cust_helper.call_update_customer(id_in_db,payload)
    assert updated_cust['first_name'] == data['first_name'], f"customer value did not update."


@pytest.mark.customer
@pytest.mark.ecombe12
@pytest.mark.tcid215
def test_update_customer_invalid_data():
    """
        Test case to verify the handling of updating customer data with invalid values.
    """

    cust_helper = CustomersAPIHelper()
    cust_obj = CustomersDAO()

    rand_customer = cust_obj.get_random_customer_from_db()
    id_in_db = rand_customer[0]['ID']
    data = {
         "first_name": "",
         "email": "invalid_email"
    }
    payload = dict(data)
    updated_cust = cust_helper.call_update_customer(id_in_db,payload,expected_status_code=400)
    assert updated_cust['message'] == "Invalid parameter(s): email", f"Api response body 'message' field not as expected. Expected 'Invalid parameter(s): email'. Actual {updated_cust['message']}."


