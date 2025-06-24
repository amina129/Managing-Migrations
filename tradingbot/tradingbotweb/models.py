from django.db import models
import requests
import json
from decimal import Decimal

class Currency(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    usd_value = models.DecimalField(max_digits=10, decimal_places=2, default=1.0)

class Transaction(models.Model):
    origin_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='origin_currency')
    destination_currency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='destination_currency')
    original_currency_value = models.DecimalField(max_digits=10, decimal_places=2)
    destination_currency_value = models.DecimalField(max_digits=10, decimal_places=2)
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    exchange_date = models.DateTimeField(auto_now_add=True)

class CurrencyHistory(models.Model):
    symbol = models.ForeignKey('Currency', on_delete=models.CASCADE)
    usd_value = models.DecimalField(max_digits=10, decimal_places=6, default=1.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.usd_value = self.get_value()
        super().save(*args, **kwargs)

    def get_value(self):
        api_url = f'https://economia.awesomeapi.com.br/last/{self.symbol.symbol}-USD'
        response = requests.get(api_url).content
        json_data = json.loads(response)
        usd_ask_value = json_data[f'{self.symbol.symbol}USD']['ask']
        decimal_value = Decimal(usd_ask_value)  # Use Decimal imported from decimal
        return decimal_value

