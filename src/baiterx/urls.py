from django.conf.urls import url

from .views import (
        CurrencyAdListView, 
        CurrencyAdDetailSlugView, 
        
        )
app_name = 'baiterx'
urlpatterns = [
    url(r'^$', CurrencyAdListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$',CurrencyAdDetailSlugView.as_view(), name='detail'),
]
