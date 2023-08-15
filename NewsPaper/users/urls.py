from django.urls import path
from .views import AccountsView, upgrade_me, SubscriberView

app_name = 'users'
urlpatterns = [
    path('profile/', AccountsView.as_view(), name='profile'),
    path('upgrade/', upgrade_me, name = 'upgrade'),
    
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
]

