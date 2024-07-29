
from ssqatest.src.dao.orders_dao import OrdersDAO
from ssqatest.src.dao.products_dao import ProductsDAO
from ssqatest.src.api_helpers.OrdersAPIHelper import OrdersAPIHelper

import json
import os

class GenericOrderHelpers:

    def __init__(self):
        self.product_dao = ProductsDAO()
        self.order_api_helper = OrdersAPIHelper()
        self.cur_file_dir = os.path.dirname(os.path.realpath(__file__))

    def create_order(self, additional_args=None, expected_status_code=201):
        """

        * Coupon: to add coupon add "coupon_lines" field to "additional_args"
            Example: "coupon_lines": [{"code": "<MY COUPON CODE>"}]
        :param product_ids:
        :param customer_id:
        :param coupon_code:
        :param additional_args: Must be a dictionary.
            Example:
                order_payload_addition = {
                                    "line_items": [{"product_id": < some product id >, "quantity": 1}],
                                    "coupon_lines": [{"code": < some coupon code >}],
                                    "shipping_lines": [{"method_id": "flat_rate", "method_title": "Flat Rate", "total": "0.00"}]
                                }
        :return:
        """

        # read the 'create order' payload template from file
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as f:
            order_payload = json.load(f)

        # update the payload (template from file) with the additional arguments passed
        if additional_args:
            assert isinstance(additional_args, dict), f"Parameter 'additional_args' must be a dictionary but found {type(additional_args)}"
            order_payload.update(additional_args)

        # if additional_args (passed in argument) does not have line items then add line items to the payload
        if additional_args and "line_items" not in additional_args.keys():
            rand_product = self.product_dao.get_random_product_from_db(qty=1)
            rand_product_id = rand_product[0]['ID']
            order_payload["line_items"] = [{"product_id": rand_product_id, "quantity": 1}]

        rs_api = self.order_api_helper.call_create_order(payload=order_payload, expected_status_code=expected_status_code)

        return rs_api

    def create_order_for_downloadable_product(self, additional_args=None, expected_status_code=201):
        payload_template = os.path.join(self.cur_file_dir, '..', 'data', 'create_order_payload.json')
        with open(payload_template) as f:
            order_payload = json.load(f)

        # update the payload (template from file) with the additional arguments passed
        if additional_args:
            assert isinstance(additional_args,
                              dict), f"Parameter 'additional_args' must be a dictionary but found {type(additional_args)}"
            order_payload.update(additional_args)

        # if additional_args (passed in argument) does not have line items then add line items to the payload
        if additional_args and "line_items" not in additional_args.keys():
            product_rs = ProductsDAO().get_random_products_that_are_downloadable(qty=1)
            downloadable_product_id = product_rs[0]['ID']
            # downloadable_product_name = product_rs[0]['post_name']
            order_payload["line_items"] = [{"product_id": downloadable_product_id, "quantity": 1}]

        rs_api = self.order_api_helper.call_create_order(payload=order_payload,
                                                         expected_status_code=expected_status_code)

        return rs_api

    @staticmethod
    def verify_order_is_created(order_json, exp_cust_id, exp_products):
        """

        :param order_json:
        :param exp_cust_id:
        :param exp_products: list of dictionaries. Example: [{'product_id': product_id}]

        :return:
        """
        orders_dao = OrdersDAO()

        # verify response
        assert order_json, f"Create order response is empty."
        assert order_json['customer_id'] == exp_cust_id, f"Create order with given custoemr id returned" \
                                                         f"bad customer id.Expected customer_id={exp_cust_id} but got '{order_json['customer_id']}'"

        assert len(order_json['line_items']) == len(exp_products), f"Expected only {len(exp_products)} item in order but " \
                                                                   f"found '{len(order_json['line_items'])}'" \
                                                                   f"Order id: {order_json['id']}."

        # verify db
        order_id = order_json['id']
        line_info = orders_dao.get_order_lines_by_order_id(order_id)
        assert line_info, f"Create order, line item not found in DB. Order id: {order_id}"

        line_items = [i for i in line_info if i['order_item_type'] == 'line_item']
        assert len(line_items) == len(exp_products), f"Expected {len(exp_products)} line item but found {len(line_items)}. Order id: {order_id}"

        # get list of product ids in the response
        api_product_ids = [i['product_id'] for i in order_json['line_items']]

        for product in exp_products:
            assert product['product_id'] in api_product_ids, f"Create order does not have at least 1 expected product in DB." \
                                                             f"Product id: {product['product_id']}. Order id: {order_id}"


