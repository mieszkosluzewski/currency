import feedparser
import logging

import requests

import settings


logger = logging.getLogger(__name__)


def get_url(currency):
    """
    Build url for rss.

    :param str currency:

    :rtype: str
    :return: url
    """
    return f'{settings.FEED_URL_PREFIX}{currency.lower()}{settings.FEED_URL_SUFFIX}'


def get_feed_data(url):
    """
    Get data from rss endpoint.

    :param str url: rss endpoint url

    :rtype: list
    :return: exchange rate data
    """
    feed = feedparser.parse(url)
    if feed.status == 404:
        logging.warning(f'Can\'t get data from provided url: {url}')
        return []

    entries = feed.entries
    try:
        result = [
            {
                'currency': entry.cb_targetcurrency,
                'exchange_rate': float(entry.cb_exchangerate.split('\n')[0]),
                'date': entry.updated
            }
            for entry in entries
        ]
    except KeyError:
        logging.warning(f'Data from rss channel at url: {url} has wrong format.')
        return []
    return result


def send_data(data):
    """
    Make requests to api for create exchange rates.

    :param dict data: dict containing data for single exchange rate

    :rtype: bool
    :return: status (True if data was added, False elsewhere).
    """
    try:
        response = requests.api.post(url=settings.SERVER_URL, data=data)
    except requests.exceptions.ConnectionError:
        logging.error(f'Can\'t connect with server at url:{settings.SERVER_URL}')
        return False
    if response.status_code == 201:
        return True
    if response.status_code == 404:
        logging.error(f'Not Found, check server url: {settings.SERVER_URL}')
    if response.status_code == 400:
        logging.info('exchange rate with this date and currency exists, or data are invalid.')

    # TODO: Add add authentication error, when authentication will be provided.
    return False


def main():
    """Iterating through url's, fetching data and send it to server."""
    for currency in settings.CURRENCY_LIST:
        url = get_url(currency)
        data = get_feed_data(url)
        for rate in data:
            send_data(rate)


if __name__ == '__main__':
    main()