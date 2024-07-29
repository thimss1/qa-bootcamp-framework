

from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.generic_helpers.generic_customer_helpers import GenericCustomerHelpers
import logging as logger
import pytest


@pytest.fixture(scope='function')
def create_customer():
    """
       function to create a customer using the CustomersAPIHelper class.
       Returns a dictionary containing the customer ID and the CustomersAPIHelper object.
    """

    customers_helper = CustomersAPIHelper()
    rs_api = customers_helper.call_create_customer()
    assert rs_api, f"Response of list all customers is empty."
    customer_id = rs_api['id']

    return {'customer_id': customer_id, 'customers_helper': customers_helper}


@pytest.mark.customers
@pytest.mark.ecombe8
@pytest.mark.tcid187
def test_delete_a_customer_with_force_flag(create_customer):
    """
    Alternate tc name:
        Verify deleting existing customer with force=True flag works
    Test case to verify delete customer with force flag
    Args:
        create_customer
    """

    logger.info("Running test: Verify deleting existing customer with force=True flag works")

    customer_id = create_customer['customer_id']
    customers_helper = create_customer['customers_helper']

    # delete the customer
    params = {'force': True}
    rs_delete = customers_helper.call_delete_customer(customer_id, params=params)
    assert rs_delete['id'] == customer_id, f"Delete customer api response has wrong customer id. " \
                                           f"Expected: {customer_id}. Actual: {rs_delete['id']}"

    # call get customer and verify customer does not exist
    rs_get = customers_helper.call_get_customer(customer_id, expected_status_code=404)
    assert rs_get['code'] == 'woocommerce_rest_invalid_id', f"After deleing a customer, the get customer call response has bad 'code'." \
                                                            f"Expected: 'woocommerce_rest_invalid_id', Actual: '{rs_get['code']}'"
    assert rs_get['message'] == 'Invalid resource ID.', f"After deleing a customer, the get customer call response has bad 'message'." \
                                                            f"Expected: 'Invalid resource ID.', Actual: '{rs_get['message']}'"
    assert rs_get['data']['status'] == 404, f"After deleing a customer, the get customer call response has bad 'status code'." \
                                                               f"Expected: 404, Actual: '{rs_get['data']['status']}'"


@pytest.mark.customers
@pytest.mark.ecombe9
@pytest.mark.tcid188
def test_delete_a_customer_without_force_flag(create_customer):
    """
    Alternate tc name:
        Verify deleting existing customer without 'force' flag fails
    Test case to verify the handling of delete customer without force flag
    Args:
        create_customer
    """

    logger.info("Running test: Verify deleting existing customer without 'force' flag fails")

    customer_id = create_customer['customer_id']
    customers_helper = create_customer['customers_helper']

    rs_delete = customers_helper.call_delete_customer(customer_id, params={'force': False}, expected_status_code=501)

    assert rs_delete['code'] == 'woocommerce_rest_trash_not_supported', f"Delete customer without 'force' flag, response has bad 'code'." \
                                                            f"Expected: 'woocommerce_rest_trash_not_supported', Actual: '{rs_delete['code']}'"
    assert rs_delete['message'] == 'Customers do not support trashing.', f"Delete customer without 'force' flag, response has bad 'message'." \
                                                        f"Expected: 'Customers do not support trashing.', Actual: '{rs_delete['message']}'"
    assert rs_delete['data']['status'] == 501, f"Delete customer without 'force' flag, response has bad 'status code'." \
                                               f"Expected: 501, Actual: '{rs_delete['data']['status']}'"


@pytest.mark.customers
@pytest.mark.ecombe10
@pytest.mark.tcid189
def test_delete_a_none_existing_customer(create_customer):
    """

    Alternate tc name:
        Verify deleting non-existing customer responds with correct message
    Test case to Verify deleting non-existing customer responds with correct message
    Args:
        create_customer
    """

    logger.info("Running test: Verify deleting non-existing customer responds with correct message")

    # to get a customer that does not exist, get the max customer id and make the call for id bigger than that
    # it is possible customers are being created by other methods so not good idea to just increase the max id by 1.
    # to be safe lets increase it by 100 or more. Even 100 can be small for example if load test is running

    generic_cust_helper = GenericCustomerHelpers()
    max_cust_id = generic_cust_helper.get_max_customer_id()
    none_exiting_cust_id = max_cust_id + 100

    # make the delete call and verify response
    customers_api_helper = CustomersAPIHelper()
    params = {'force': True}
    rs_delete = customers_api_helper.call_delete_customer(customer_id=none_exiting_cust_id, params=params, expected_status_code=400)

    assert rs_delete['code'] == 'woocommerce_rest_invalid_id', f"Delete customer with none existing customer id responded with bad 'code'." \
                                                               f"Expected: 'woocommerce_rest_invalid_id', Actual: '{rs_delete['code']}'"
    assert rs_delete['message'] == 'Invalid resource id.', f"Delete customer with none existing customer id responded with bad 'message'." \
                                                           f"Expected: 'Invalid resource id.', Actual: '{rs_delete['message']}'"
    assert rs_delete['data']['status'] == 400, f"Delete customer with none existing customer id responded with bad 'status code'." \
                                               f"Expected: 400, Actual: '{rs_delete['data']['status']}'"
