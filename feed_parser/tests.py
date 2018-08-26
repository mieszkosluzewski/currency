"""
Tests for feed parser.
"""
from feed_parser import settings
from feed_parser.parser import get_url


def test_get_url():
    """
    Given: currency
    When: call get_url
    Then: proper url is returned
    """

    assert get_url('USD') == settings.FEED_URL_PREFIX + 'usd' + settings.FEED_URL_SUFFIX


# TODO: add more tests
