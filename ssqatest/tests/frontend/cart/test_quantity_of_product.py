import pytest
import logging as logger
import time
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.Header import Header


@pytest.mark.usefixtures("init_driver")
class TestCartQuantity:
    """
    Test class for verifying cart quantity functionality.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.tcid169
    @pytest.mark.ecomfe101
    def test_change_quantity(self, setup):
        """
        Test to verify changing the quantity of a product in the cart.

        Args:
            setup:  setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()

        initial_quantity = self.cart.get_product_quantity()
        assert initial_quantity == '1', f"Expected cart qty '1' but found '{initial_quantity}'."

        self.cart.input_product_quantity(7)
        new_quantity = self.cart.get_product_quantity()

        assert new_quantity == '7', f"Expected cart qty '7' after updating it, " \
                                        f"but found '{new_quantity}'."


@pytest.mark.usefixtures("init_driver")
class TestCartQuantityTwo:
    """
    Another test class for verifying cart quantity functionality.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.ecomfe83
    def test_correct_subtotal_displayed_after_product_quantity_decreased(self, setup):
        """
        Test to verify that the correct subtotal is displayed after decreasing the product quantity.

        Args:
            setup:  setup object.
        """
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        price = self.cart.get_product_price()
        self.cart.input_product_quantity(3)
        self.cart.click_upadete_cart()
        time.sleep(5)
        subtotal_before = self.cart.get_cart_subtotal()
        self.cart.input_product_quantity(1)
        self.cart.click_upadete_cart()
        time.sleep(5)
        subtotal_after = self.cart.get_cart_subtotal()
        assert subtotal_after == price, "subtotal not decrease after decreasing quantity"


@pytest.mark.usefixtures("init_driver")
class TestCartQuantityThree:
    """
        Another test class for verifying cart quantity functionality.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.ecomfe84
    def test_correct_subtotal_column_updates_with_quantity_change(self, setup):
        """
        Test to verify that the subtotal value updates as the quantity of a product changes.

        Args:
            setup:  setup object.
        """
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        subtotal__column_before = self.cart.get_column_subtotal()
        self.cart.input_product_quantity(3)
        self.cart.click_upadete_cart()
        time.sleep(5)
        subtotal__column_after = self.cart.get_column_subtotal()
        assert subtotal__column_after == subtotal__column_before * 3, " subtotal column does not update with quantity change"


@pytest.mark.usefixtures("init_driver")
class TestCartQuantityFour:
    """
        Another test class for verifying cart quantity functionality.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.ecomfe72
    def test_quantity_of_two_product(self, setup):
        """
        Test to verify changing the quantity of two products in the cart.

        Args:
            setup:  setup object.
        """

        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.homepage.click_second_add_to_cart_button()
        self.header.wait_until_cart_item_count(2)

        self.cart.go_to_cart_page()
        self.cart.input_product_quantity(2)
        self.cart.input_product_quantity_second_item(3)

        quantity1 = self.cart.get_product_quantity()
        quantity2 = self.cart.get_product_quantity_second_item()

        assert int(quantity1) == 2, "Quantity of an item is not correct when there is two items in cart"
        assert int(quantity2) == 3, "Quantity of an item is not correct when there is two items in cart"


@pytest.mark.usefixtures("init_driver")
class TestCartQuantityFive:
    """
           Another test class for verifying cart quantity functionality.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.cart = CartPage(self.driver)
        request.cls.header = Header(self.driver)
        yield

    @pytest.mark.ecomfe82
    def test_correct_subtotal_displayed_after_product_quantity_increased(self, setup):
        """
        Test to verify that the correct subtotal is displayed after increasing the product quantity.

        Args:
            setup:  setup object.
        """
        self.homepage.go_to_home_page()
        self.homepage.click_first_add_to_cart_button()
        self.header.wait_until_cart_item_count(1)

        self.cart.go_to_cart_page()
        price = self.cart.get_product_price()
        subtotal_before = self.cart.get_cart_subtotal()
        self.cart.input_product_quantity(3)
        self.cart.click_upadete_cart()
        time.sleep(5)
        subtotal_after = self.cart.get_cart_subtotal()
        assert subtotal_after == price * 3, "subtotal not increased after increasing quantity"
        assert subtotal_after == subtotal_before * 3, "subtotal not increased after increasing quantity"