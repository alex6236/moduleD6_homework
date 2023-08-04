# from django import views
from django.urls import path
from mail.views import SubscriberView      #subscribe

app_name = 'mail'
urlpatterns = [
   # path('subscribe/', subscribe, name='subscribe'),
   path('subscribe/', SubscriberView.as_view(), name='subscribe'),
]
