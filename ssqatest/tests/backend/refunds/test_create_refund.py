import pytest
import logging as logger
from ssqatest.src.api_helpers.refunds_hellper import RefundsHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers


@pytest.mark.ecombe120
def test_create_refund_with_unsupported_payment_gateway():
    """
       Test to verify the handling of creating a refund with an unsupported payment gateway.
    """
    ref_obj = RefundsHelper()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']
    total = order_json['total']

    data ={
          "amount": f"{total}",
          "line_items": [
            {
              "id": "111",
              "refund_total": total,
              "refund_tax": [
                {
                  "id":"222",
                  "refund_total": 0
                }
              ]
            }
        ]
        }
    payload = dict(data)
    new_ref = ref_obj.call_create_refund(order_id,payload)
    assert new_ref['message'] == "The payment gateway for this order does not support automatic refunds.", f"create refund returned invalid message"


@pytest.mark.ecombe121
def test_create_refund_invalid_amount():
    """
     Test to verify the handling of creating a refund with an invalid amount.
     """
    ref_obj = RefundsHelper()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']

    data = {
        "amount": "10000",
        "line_items": [
            {
                "id": "111",
                "refund_total": 1000,
                "refund_tax": [
                    {
                        "id": "222",
                        "refund_total": 0
                    }
                ]
            }
        ]
    }
    payload = dict(data)
    new_ref = ref_obj.call_create_refund(order_id, payload)
    assert new_ref['message'] == "Invalid refund amount.", f"returned invalid message"


@pytest.mark.ecombe122
def test_create_refund_invalid_amount_type():
    """
       Test to verify the handling of creating a refund with an invalid amount type.
    """
    ref_obj = RefundsHelper()
    generic_order_helper = GenericOrderHelpers()
    order_json = generic_order_helper.create_order()
    order_id = order_json['id']

    data = {
        "amount": 1000,
        "line_items": [
            {
                "id": "111",
                "refund_total": 1000,
                "refund_tax": [
                    {
                        "id": "222",
                        "refund_total": 0
                    }
                ]
            }
        ]
    }
    payload = dict(data)
    new_ref = ref_obj.call_create_refund(order_id, payload)
    assert new_ref['message'] == "amount is not of type string.", f"returned invalid message"

