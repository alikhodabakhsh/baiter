from django.conf.urls import url

from .views import (
        ItemListView, 
        ItemDetailSlugView, 
        )
        
app_name = 'baiterx'
urlpatterns = [
    url(r'^$', ItemListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$',ItemDetailSlugView.as_view(), name='detail'),
]
