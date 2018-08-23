from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import ExchangeRate


class ExchangeRateSerializer(serializers.ModelSerializer):
    """Serializer for exchange rate."""
    class Meta:
        model = ExchangeRate
        fields = ('currency', 'date', 'exchange_rate')
        validators = [
            UniqueTogetherValidator(
                queryset=ExchangeRate.objects.all(),
                fields=('currency', 'date')
            )
        ]
