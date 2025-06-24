from django.contrib import admin
from .models import Currency, CurrencyBalance, Transaction, CurrencyHistory

class CurrencyHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('exchange_date',)


admin.site.register(Currency)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CurrencyHistory, CurrencyHistoryAdmin)
admin.site.register(CurrencyBalance, CurrencyHistoryAdmin)