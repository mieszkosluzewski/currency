"""
Module with settings for feed_parser.
"""

CURRENCY_LIST = (
    'USD',
    'JPY',
    'BGN',
    'CZK',
    'DKK',
    'EEK',
    'GBP',
    'HUF',
    'PLN',
    'RON',
    'SEK',
    'CHF',
    'ISK',
    'NOK',
    'HRK',
    'RUB',
    'TRY',
    'AUD',
    'BRL',
    'CAD',
    'CNY',
    'HKD',
    'IDR',
    'INR',
    'KRW',
    'MXN',
    'MYR',
    'NZD',
    'PHP',
    'SGD',
    'THB',
    'ZAR',
)


#  TODO: use urllib, or something.

FEED_URL_PREFIX = 'https://www.ecb.europa.eu/rss/fxref-'
"""Prefix for rss endpoint."""
FEED_URL_SUFFIX = '.html'
"""Suffix for rss endpoint."""
SERVER_URL = 'http://127.0.0.1:8000/add_exchange_rate/'
"""Endpoint for currency adding."""
