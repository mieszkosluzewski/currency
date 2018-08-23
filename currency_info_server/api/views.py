from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from api.models import ExchangeRate
from api.serializers import ExchangeRateSerializer


class AddExchangeRateView(generics.CreateAPIView):
    """View for creating new exchange rate."""
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer


class ExchangeRateView(generics.RetrieveUpdateDestroyAPIView):
    """View for operations on single exchange rate (get, update, delete)."""
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer


class ExchangeRateListView(generics.ListAPIView):
    """View for all exchange rates."""
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned exchange rates list to a given currency,
        by filtering against a `currency` query parameter in the URL.
        """
        queryset = ExchangeRate.objects.all()
        currency = self.request.query_params.get('currency', None)
        if currency is not None:
            queryset = queryset.filter(currency=currency)
        return queryset

