from rest_framework import serializers
from currency_api import models

class CurrencyFormatSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CurrencyFormat

        fields = ('id', 'created_on', 'country_code', 'currency_code', 'currency_symbol', 
        'thousand_delimiter', 'cents_delimiter', 'currency_identificator', 'currency_identificator_position',
        'is_show_cents')

class CurrencyAmountSerializer(serializers.Serializer):
    country_code = serializers.CharField()
    currency_code = serializers.CharField()
    amount = serializers.DecimalField(max_digits=None, decimal_places=None)
