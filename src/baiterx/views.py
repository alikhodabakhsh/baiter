# from django.views import ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render, get_object_or_404, redirect

from analytics.mixins import ObjectViewedMixin


from .models import CurrencyAd


class CurrencyAdFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return CurrencyAd.objects.all().featured()


class CurrencyAdFeaturedDetailView(ObjectViewedMixin, DetailView):
    queryset = CurrencyAd.objects.all().featured()
    template_name = "products/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Product.objects.featured()


class UserCurrencyAdHistoryView(LoginRequiredMixin, ListView):
    template_name = "products/user-history.html"
    def get_context_data(self, *args, **kwargs):
        context = super(UserCurrencyAdHistoryView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        views = request.user.objectviewed_set.by_model(CurrencyAd, model_queryset=False)
        return views



class CurrencyAdListView(ListView):
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_context_data(self, *args, **kwargs):
        context = super(CurrencyAdListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return CurrencyAd.objects.all()


def CurrencyAd_list_view(request):
    queryset = CurrencyAd.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)



class CurrencyAdDetailSlugView(ObjectViewedMixin, DetailView):
    queryset = CurrencyAd.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CurrencyAdDetailSlugView, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = CurrencyAd.objects.get(slug=slug, active=True)
        except CurrencyAd.DoesNotExist:
            raise Http404("Not found..")
        except CurrencyAd.MultipleObjectsReturned:
            qs = CurrencyAd.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance

import os
from wsgiref.util import FileWrapper # this used in django
from mimetypes import guess_type

from django.conf import settings
#from orders.models import ProductPurchase



class CurrencyAdDetailView(ObjectViewedMixin, DetailView):
    #queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CurrencyAdDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = CurrencyAd.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Currency doesn't exist")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def CurrencyAd_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk, featured=True) #id
    # instance = get_object_or_404(Product, pk=pk, featured=True)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404("Product doesn't exist")
    # except:
    #     print("huh?")

    instance = CurrencyAd.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Currency doesn't exist")
    #print(instance)
    # qs  = Product.objects.filter(id=pk)

    # #print(qs)
    # if qs.exists() and qs.count() == 1: # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist")

    context = {
        'object': instance
    }
    return render(request, "products/detail.html", context)
