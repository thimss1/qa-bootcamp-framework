#
#
# import pytest
# import logging as logger
# from ssqatest.src.utilities.wooAPIUtility import WooAPIUtility
#
#
# @pytest.mark.healthcheck
# def test_healthcheck():
#     logger.info("Just running healthcheck by calling system status endpoint.")
#     logger.info("URL: /wp-json/wc/v3/system_status")
#     rs_api = WooAPIUtility().get("system_status")
#     assert rs_api, "The site might not be up or not healthy. FAILED HEALTH CHECK"
