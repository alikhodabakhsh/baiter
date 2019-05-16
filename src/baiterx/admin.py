from django.contrib import admin

from .models import Item
from accounts.models import User


class CurrencyAdAdmin(admin.ModelAdmin):
    list_display = ['username', 'name_currency', 'category']
    list_filter = ['category']
    class Meta:
        model = Item

admin.site.register(Item, CurrencyAdAdmin)

