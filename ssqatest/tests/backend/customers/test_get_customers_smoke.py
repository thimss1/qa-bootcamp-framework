
import logging as logger
import random

import pytest
from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.dao.customers_dao import CustomersDAO


pytestmark = [pytest.mark.beregression, pytest.mark.besmoke, pytest.mark.customers_api]


@pytest.mark.ecombe2
@pytest.mark.tcid30
@pytest.mark.ecombe2
def test_get_all_customers():
    """
       Test to verify the functionality of retrieving a list of all customers.
    """
    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_list_customers()

    assert rs_api, f"Response of list all customers is empty."


@pytest.mark.ecombe98
def test_get_all_customer_by_id():
    """
       Test to verify the functionality of retrieving a customer by ID.
    """
    cust_dao = CustomersDAO()

    existing_cust = cust_dao.get_random_customer_from_db()
    cust_id = existing_cust[0]['ID']

    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_get_customer(cust_id)

    assert rs_api['id'] == cust_id, f"get customer by id failed.expected{cust_id} but returned {rs_api['id']}"


@pytest.mark.ecombe7
def test_get_all_customer_non_exits_or_invalid_id():
    """
       Test to verify the handling of retrieving a customer using a non-existent or invalid ID.
    """
    cust_id = random.randint(20000,67700)

    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_get_customer(cust_id,expected_status_code=404)

    assert rs_api['message'] == "Invalid resource ID.", f"Response of get customer by invalid id returned wrong message."

