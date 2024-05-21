from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('home_page/', views.Home.as_view(),  name='home'),
    path('shop_page/', views.Shop.as_view(),  name='shop'),
    path('contacts/', views.Contacts.as_view(),  name='contacts'),
]   