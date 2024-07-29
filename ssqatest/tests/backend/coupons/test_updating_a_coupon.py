from ssqatest.src.api_helpers.CouponsAPIHelper import CouponsAPIHelper
from ssqatest.src.utilities.genericUtilities import generate_random_coupon_code, generate_random_string
import random
import pytest


@pytest.mark.coupon
@pytest.mark.ecombe79
@pytest.mark.tcid216
def test_update_coupon_data():
    """
        Test case to verify the functionality of updating a coupon code.
    """

    pct_off = str(random.randint(10, 90)) + ".00"
    coupon_code = generate_random_coupon_code(sufix="code", length=5)
    new_coup_code = generate_random_coupon_code(sufix='supers',length=4)

    # get the helper object
    coupon_helper = CouponsAPIHelper()
    # prepare data and call api
    payload = dict()
    payload['code'] = coupon_code
    payload['amount'] = pct_off
    payload['discount_type'] = 'percent'
    rs_coupon = coupon_helper.call_create_coupon(payload=payload)
    coupon_id = rs_coupon['id']

    data = {
        "code": new_coup_code,
           }
    payload = dict(data)
    updated_coup = coupon_helper.call_update_coupon(coupon_id,payload)
    assert updated_coup['code'] == data['code'].lower(), f"Update  coupon code to random string did not have " \
                                                   f"correct code in response. Expected: {data['code'].lower()} Actual: {updated_coup['code']}"

