from django.db import models


class ExchangeRate(models.Model):
    """
    Model for currency exchange rate.

    Exchange rate are related to EUR.
    """
    date = models.DateTimeField()
    currency = models.CharField(max_length=3)
    exchange_rate = models.FloatField()
