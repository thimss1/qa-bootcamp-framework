import logging as logger

import pytest
from ssqatest.src.generic_helpers.generic_product_helper import GenericProductHelper
from ssqatest.src.generic_helpers.generic_product_reviews_helper import GenericProductReviewsHelper
from ssqatest.src.utilities.genericUtilities import generate_random_string, generate_random_email_and_password


@pytest.fixture(scope="function")
def setup_teardown(request):
    request.cls.product_helper = GenericProductHelper()
    request.cls.product_review_helper = GenericProductReviewsHelper()
    request.cls.product = request.cls.product_helper.create_a_product()
    request.cls.rating_count_before = request.cls.product['rating_count']
    request.cls.product_id = request.cls.product['id']

    yield

    logger.info(f"Running teardown. Deleting product id: {request.cls.product_id}")
    request.cls.product_helper.delete_a_product(request.cls.product_id)


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.smoke
class TestProductsReviewsSmoke(object):
    """
       Test class for product reviews functionality.
    """

    @pytest.mark.status
    @pytest.mark.parametrize("review_status", [
        pytest.param('hold', marks=[pytest.mark.tcid205,pytest.mark.ecombe46]),
        pytest.param('spam', marks=[pytest.mark.tcid206,pytest.mark.ecombe47]),
        pytest.param('unspam', marks=[pytest.mark.tcid207,pytest.mark.ecombe48]),
        pytest.param('trash', marks=[pytest.mark.tcid208,pytest.mark.ecombe49]),
        pytest.param('untrash', marks=[pytest.mark.tcid209,pytest.mark.ecombe50])
    ])
    def test_verify_create_review_with_different_statuses(self, review_status):
        """
            Test to verify the creation of a review with different statuses.

            Args:
                review_status
        """
        logger.info("test_verify_create_review_with_different_statuses")

        review = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review="Automation review: " + generate_random_string(length=25),
            reviewer=f"{generate_random_string(length=5)} {generate_random_string(length=6)}",
            reviewer_email=generate_random_email_and_password()['email'],
            rating=5,
            status=review_status
        )

        review_retrieved = self.product_review_helper.get_product_review(review['id'])

        expected_status = 'hold' if review_status in ('untrash', 'unspam') else review_status
        assert review_retrieved['status'] == expected_status, f"Failed to create review with status = '{expected_status}'."

    @pytest.mark.tcid210
    @pytest.mark.ecombe51
    def test_verify_review_can_not_be_created_with_invalid_status(self):
        """
            Test to verify that a review cannot be created with an invalid status.

        """
        review = self.product_review_helper.create_product_review(
            product_id=self.product_id,
            review="Automation review: " + generate_random_string(length=25),
            reviewer=f"{generate_random_string(length=5)} {generate_random_string(length=6)}",
            reviewer_email=generate_random_email_and_password()['email'],
            rating=5,
            status=generate_random_string(length=5),
            expected_status_code=400
        )

        expected_response = {'code': 'rest_invalid_param',
                                'data': {'details': {
                                            'status': {'code': 'rest_not_in_enum',
                                                       'data': None,
                                                        'message': 'status is not one of approved, '
                                                        'hold, spam, unspam, trash, and '
                                                        'untrash.'}},
                                            'params': {'status': 'status is not one of approved, hold, spam, '
                                                       'unspam, trash, and untrash.'},
                                            'status': 400},
                                'message': 'Invalid parameter(s): status'}

        assert review == expected_response, f"Response of creating review with invalid 'status' did notmach expected."
