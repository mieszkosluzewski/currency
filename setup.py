import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="currency exchange",
    version="0.0.1",
    author="Mieszko Służewski",
    author_email="mieszkosluzewski@gmail.com",
    description="Simple RSS parser and REST api with parsed data for currency exchange",
    license="",
    keywords="RSS, REST, currency, exchange",
    url="",
    packages=["currency_info_server", "feed_parser"],
    install_requires=[
        'Django>=2.1',
        'django-extensions>=2.1.0',
        'django-filter>=2.0.0',
        'djangorestframework>=3.8.2',
        'feedparser>=5.2.1',
        'pytest>=3.7.2',
        'requests>=2.19.1'
    ],
    long_description=read("README.md"),
)

