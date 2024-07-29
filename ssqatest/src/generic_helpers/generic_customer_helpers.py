

from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper


class GenericCustomerHelpers:

    def __init__(self):
        self.customers_api_helper = CustomersAPIHelper()

    def get_max_customer_id(self):
        """
        Returns the highest customer id available.
        Calls list all customers endpoint sorting it by 'id' descending and gets the id of the first customer.
        :return:
        """

        params = {"orderby": 'id', "order": "desc"}
        all_customers = self.customers_api_helper.call_list_customers(payload=params)
        latest_customer = all_customers[0]
        max_customer_id = latest_customer['id']

        return max_customer_id