from django.contrib import admin
from currency_api import models

admin.site.register(models.UserCurrency)
admin.site.register(models.CurrencyFormat)
