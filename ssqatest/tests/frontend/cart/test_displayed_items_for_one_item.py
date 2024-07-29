import pytest
import logging as logger
import time
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestDisplayedItemsCartPage:
    """
       Test class for verifying displayed items on the Cart page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)
        yield

    @pytest.mark.tcid155
    @pytest.mark.ecomfe87
    def test_cart_totals_section_shipping_label_displayed(self, setup):
        """
        Test to verify that the cart totals section has the 'shipping' label displayed.

        Args:
            setup:  setup object.
        """
        logger.info(f"Running Test: test_cart_totals_section_shipping_label_displayed")

        self.cart.go_to_cart_page()
        shipping_label = self.cart.get_shipping_label_from_bottom_table()

        # Assert that the cart subtotals section has 'shipping' label
        assert shipping_label == 'Shipping', "Cart totals section does not have 'shipping' label."

    @pytest.mark.tcid129
    @pytest.mark.ecomfe59
    def test_empty_cart_header_displayed(self, setup):
        """
        Test to verify that the header with text 'Cart' is displayed on the empty cart page.

        Args:
            setup:  setup object.
        """
        self.homepage.go_to_home_page()
        self.cart.go_to_cart_page()

        # Assert that the header with text 'Cart' is displayed
        empty_cart_header = self.cart.get_cart_page_header()
        assert empty_cart_header == 'Cart', "Header with text 'Cart' is not displayed in empty cart page."

    @pytest.mark.tcid130
    @pytest.mark.ecomfe60
    def test_cart_heading_displayed_cart_page_with_item(self, setup):
        """
        Test to verify that the cart page has the 'Cart' heading when there is an item in the cart.

        Args:
            setup:  setup object.
        """
        logger.info(f"Running Test: test_cart_heading_displayed_cart_page_with_item")

        self.cart.go_to_cart_page()
        shipping_label = self.cart.get_cart_heading()

        # Assert that the cart page has cart heading
        assert shipping_label == 'Cart', 'Cart pge does not have cart heading ith item in it'

    @pytest.mark.tcid147
    @pytest.mark.ecomfe77
    def test_cart_total_is_displayed(self, setup):
        """
            Test to verify that the cart total is displayed in the cart subtotals section.

            Args:
                setup:  setup object.
         """

        logger.info(f"Running Test: test_cart_total_is_displayed")

        self.cart.go_to_cart_page()
        cart_total_label = self.cart.get_cart_totl_label()

        # Assert that the cart subtotals section has 'cart total' label
        assert cart_total_label == 'Cart totals', "Cart totals section does not have cart totals label."


@pytest.mark.usefixtures("init_driver")
class TestDisplayedItemsCartPageTwo:
    """
    Another test class for verifying displayed items on the Cart page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)
        self.cart.go_to_cart_page()

        yield

    @pytest.mark.ecomfe91
    def test_correct_total_displayed_for_one_item(self, setup):
        """
        Test to verify that the correct total is displayed for one item in the cart.

        Args:
            setup:  setup object.
        """
        price = self.cart.get_product_price()
        total = self.cart.get_cart_total()

        assert price == total, "correct total not displayed for one item"

    @pytest.mark.ecomfe73
    def test_correct_subtotal_column_displayed_for_one_item(self, setup):
        """
        Test to verify that the correct subtotal column is displayed for one item in the cart.

        Args:
            setup:  setup object.

        """

        price = self.cart.get_product_price()
        subtotal = self.cart.get_column_subtotal()

        assert price == subtotal, "correct subtotal colum is not displayed for one item"

    @pytest.mark.ecomfe71
    def test_quantity_of_one_product_displayed(self, setup):
        """
        Test to verify that the displayed quantity  of an item is  correct when there is one item in cart.

        Args:
            setup:  setup object.

        """
        self.cart.input_product_quantity(2)
        quantity = self.cart.get_product_quantity()

        assert int(quantity) == 2, "Quantity of an item is not correct when there is one item in cart"

    @pytest.mark.tcid161
    @pytest.mark.ecomfe93
    def test_checkout_button_label(self, setup):
        """
        Test to verify that the 'Proceed to checkout' button label is displayed.

        Args:
            setup:  setup object.

        """

        checkout_button_text = self.cart.get_label_for_proceed_to_checkout_button()
        assert checkout_button_text == 'Proceed to checkout', "'Proceed to checkout' button label is incorrect."

    @pytest.mark.tcid148
    @pytest.mark.ecomfe78
    def test_cart_subtotals_section_subtotal_label_displayed(self, setup):

        """
        Test to verify that the subtotal section has 'subtotal'  label  displayed.

        Args:
            setup:  setup object.

        """
        logger.info(f"Running Test: test_cart_subtotal_label_displayed")

        subtotal_label = self.cart.get_subtotal_label_from_bottom_table()

        # Assert that the cart subtotals section has 'Subtotal' label
        assert subtotal_label == 'Subtotal', "Cart subtotals section does not have 'Subtotal' label."

    @pytest.mark.tcid158
    @pytest.mark.ecomfe90
    def test_cart_subtotals_section_total_label(self, setup):
        """
            Test to verify that the subtotal section has 'total'  label  displayed.

            Args:
                setup:  setup object.

        """
        logger.info(f"Running Test: test_cart_subtotals_total_label")

        total_label = self.cart.get_total_label_from_bottom_table()

        assert total_label == 'Total', "Subtotals section does not have 'Total' label."


@pytest.mark.usefixtures("init_driver")
class TestDisplayedItemsCartPageThree:
    """
        Another test class for verifying displayed items on the Cart page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)
        self.homepage.go_to_home_page()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()

        yield

    @pytest.mark.ecomfe69
    def test_correct_price_displayed_for_one_item(self, setup):
        """
            Test to verify that the correct  price displayed for one item in a cart.

            Args:
                setup:  setup object.

        """
        price = self.cart.get_product_price()

        assert price == 66.44, "correct price not displayed for one item in cart"

    @pytest.mark.ecomfe79
    def test_correct_subtotal_displayed_for_one_item(self, setup):
        """
            Test to verify that the correct subtotal value is  displayed for one item in a cart.

            Args:
                setup:  setup object.

        """
        price = self.cart.get_product_price()
        subtotal = self.cart.get_cart_subtotal()

        assert price == subtotal, "subtotal displayed is wrong"

    @pytest.mark.ecomfe88
    def test_verify_flat_rate_radio_displayed(self, setup):
        """
            Test to verify that flat rate radio is displayed.

            Args:
                setup:  setup object.

        """
        flat_rate = self.cart.get_shipping_flat_rate()
        flat_rate_price = self.cart.get__shipping_flat_rate_price()

        assert flat_rate == 'Flat rate: $3.00', "flat rate label and price not displayed"

    @pytest.mark.ecomfe95
    def test_verify_free_shipping_displayed_for_total_price_more_than_fifty(self, setup):
        """
            Test to verify that free shipping label is displayed when the total price is more than 50.

            Args:
                setup:  setup object.

        """
        subtotal = self.cart.get_cart_subtotal()
        shipping = self.cart.get_free_shipping_element_from_bottom_table()

        assert subtotal > 50, "price less than 50"
        assert shipping.is_displayed(), "free shipping not displayed for total price less than 50"

    @pytest.mark.ecomfe96
    def test_verify_shipping_to_text_displayed(self, setup):
        """
            Test to verify that 'shipping to ' text is displayed .

            Args:
                setup:  setup object.

        """
        shipping_to = self.cart.get_shipping_to_element()

        assert shipping_to.is_displayed(), "shipping to label is not displayed"

    @pytest.mark.ecomfe97
    def test_verify_change_address_link_is_displayed_in_subtotal_section(self, setup):
        """
                Test to verify that the 'change address' link  is displayed in the subtotal section.

                Args:
                    setup:  setup object.

         """
        change_address = self.cart.get_change_address_lable()

        assert change_address == 'Change address', "change address button ot displayed"

    @pytest.mark.ecomfe98
    def test_verify_change_address_link__in_subtotal_section_opens_form(self, setup):
        """
        Test to verify that clicking the 'change address link ' opens a form to change the address.

        Args:
            setup:  setup object.

        """

        self.cart.click_change_address()
        address_form = self.cart.get_address_form()

        assert address_form.is_displayed(), "change address does not open form."
