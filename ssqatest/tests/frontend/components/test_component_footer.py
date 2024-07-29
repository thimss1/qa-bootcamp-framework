import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestComponentFooter:
    """
    Test class to verify  the footer component.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.checkout = CheckoutPage(self.driver)
        request.cls.myacc = MyAccountSignedOut(self.driver)
        yield

    @pytest.mark.ecomfe50
    def test_demo_store_displayed_on_footer(self, setup):
        """
        Test to verify that the '© Demo eCom Store 2024 ' text is displayed on the footer.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_demo_store_displayed_on_footer")
        self.homepage.go_to_home_page()
        demo_ecom_store = self.homepage.get_displayed_company_name()
        assert demo_ecom_store == '© Demo eCom Store 2024\nBuilt with Storefront & WooCommerce.', 'page does not have © Demo eCom Store 2023 displayed'

    @pytest.mark.ecomfe51
    def test_footer_displayed_on_every_page(self,setup):
        """
        Test to verify that the footer is displayed on every page.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_footer_displayed_on_every_page")
        listx = [self.homepage.go_to_home_page,self.cart.go_to_cart_page,self.checkout.go_to_checkout_page,self.myacc.go_to_my_account]
        for i in listx:
            i()
            demo_ecom_store = self.homepage.get_displayed_company_name()
            assert demo_ecom_store == '© Demo eCom Store 2024\nBuilt with Storefront & WooCommerce.', 'page does not have © Demo eCom Store 2023 displayed'

    @pytest.mark.ecomfe52
    def test_footer_has_link_to_woocommerce(self, setup):
        """
        Test to verify that the footer has a link to WooCommerce.

        Args:
            setup: A setup object.
        """

        logger.info(f"Running Test: test_footer_has_link_to_woocommerce")
        listx = [self.homepage.go_to_home_page, self.cart.go_to_cart_page, self.checkout.go_to_checkout_page,
                 self.myacc.go_to_my_account]
        for i in listx:
            i()
            woocommerce = self.homepage.get_woocommerce_link_from_footer()
            assert woocommerce == 'Built with Storefront & WooCommerce', 'page does not have © Demo eCom Store 2023 displayed'

