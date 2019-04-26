from django.contrib import admin

from .models import CurrencyAd, Category
from accounts.models import User


class CurrencyAdAdmin(admin.ModelAdmin):
    list_display = ['username', 'name_currency', 'category']
    list_filter = ['category']
    class Meta:
        model = CurrencyAd

admin.site.register(CurrencyAd, CurrencyAdAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['status',]
    
    class Meta:
        model = User

admin.site.register(Category, CategoryAdmin)
