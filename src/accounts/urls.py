from django.conf.urls import url

from accounts import views
       
app_name = 'account'
urlpatterns = [
    url(r'^$', views.AccountHomeView.as_view(), name='home'),
    url(r'^details/$', views.UserDetailUpdateView.as_view(), name='user-update'),
    url(r'^email/confirm/(?P<key>[0-9A-Za-z]+)/$', 
            views.AccountEmailActivateView.as_view(), 
            name='email-activate'),
    url(r'^email/resend-activation/$', 
            views.AccountEmailActivateView.as_view(), 
            name='resend-activation'),
    url(r'^dashboard/$',views.Dashboard , name='dashboard'),
    url(r'^transactions/$',views.Transactions , name='transactions'),
    url(r'^transactions/details/$',views.TransactionDetails , name='transaction-details'),
    url(r'^profile/$',views.Profile , name='profile'),
    url(r'^kyc/application$',views.KycApplication , name='kyc-application'),
    url(r'^kyc/form$',views.KycForm , name='kyc-form'),
    url(r'^financial/$',views.Financial, name='financial'),
    url(r'^BankAccount/$',views.BankAccount, name='bank-account'),

]

# account/email/confirm/asdfads/ -> activation view