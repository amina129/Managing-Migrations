from django.db import models

class Currency (models.Model):
    symbol     = models.CharField(max_length=10,primary_key=True)
    usd_value=models.DecimalField(max_digits=10, decimal_places=2, default=1.0 )
    
class Transaction(models.Model):
    origin_currency = models.ForeignKey('Currency',on_delete=models.CASCADE, related_name='origin_currency')
    destination_curency = models.ForeignKey('Currency', on_delete=models.CASCADE, related_name='destination_currency')
    original_currency_value= models.DecimalField(max_digits=10, decimal_places=2)
    destination_currency_value = models.DecimalField(max_digits=10, decimal_places=2)
    comission = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    exchange_date = models.DateTimeField(auto_now_add=True)
    
