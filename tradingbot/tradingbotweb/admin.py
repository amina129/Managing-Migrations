from django.contrib import admin
from .models import Currency, CurrencyBalance, Transaction, CurrencyHistory,ExchangeGoal

class CurrencyHistoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class TransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('exchange_date',)


admin.site.register(Currency)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CurrencyHistory, CurrencyHistoryAdmin)
admin.site.register(CurrencyBalance, CurrencyHistoryAdmin)
admin.site.register(ExchangeGoal, CurrencyHistoryAdmin)