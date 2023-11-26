from django.urls import path
from .views import*

app_name = 'balance'

urlpatterns = [
    path('', home, name='home'),
    path('balance/<str:username>/', show_balance, name='show_balance'),
    path('external-page/', external_page, name='external_page'),
]