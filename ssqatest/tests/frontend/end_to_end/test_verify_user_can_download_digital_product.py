import os
import time

import pytest
from ssqatest.src.configs.MainConfigs import MainConfigs
from ssqatest.src.utilities.genericUtilities import generate_random_string
from ssqatest.src.api_helpers.CustomersAPIHelper import CustomersAPIHelper
from ssqatest.src.generic_helpers.generic_order_helpers import GenericOrderHelpers
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.OrderReceivedPage import OrderReceivedPage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn


@pytest.mark.usefixtures("init_driver")
class TestDownloadItem:

    @pytest.fixture(scope='function')
    def setup(self, request):
        tempdir = self.download_location
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.orderReceive = OrderReceivedPage(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.my_account = MyAccountSignedOut(self.driver)
        request.cls.my_account_in = MyAccountSignedIn(self.driver)

        generic_order_helper = GenericOrderHelpers()
        customer_helper = CustomersAPIHelper()
        password = generate_random_string(6)
        cust_info = customer_helper.call_create_customer(password=password)
        customer_id = cust_info['id']
        email = cust_info['email']

        coupon_code = MainConfigs.get_coupon_code('FREE_COUPON')
        order_payload_addition = {
            "coupon_lines": [{"code": coupon_code}],
            "customer_id": customer_id,
        }
        generic_order_helper.create_order_for_downloadable_product(additional_args=order_payload_addition)

        info = {'email': email,
                'password': password,
                'tempdir': tempdir}
        return info

    @pytest.mark.tcid233
    @pytest.mark.ecomfe153
    def test_download_product(self, setup):
        email = setup['email']
        password = setup['password']
        name = 'single.jpg'
        tempdir = setup['tempdir']

        self.homepage.go_to_home_page()
        self.my_account.go_to_my_account()
        self.my_account.login_user(email, password)
        self.my_account.go_to_my_account()
        self.my_account_in.click_on_downloads_tab()
        self.my_account_in.click_download_link()

        downloaded_data_path = os.path.join(tempdir, f'{name}')
        time.sleep(20)
        timeout = time.time() + 20
        while time.time() < timeout:
            assert os.path.isfile(downloaded_data_path), 'file is not downloaded'




















