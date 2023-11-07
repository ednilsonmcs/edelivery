from django.urls import include, path

from telegram import api
from . import views

urlpatterns = [
    path('api/', api.order_api, name='order_api'),
    path('order/', views.order_view, name='order_view'),
]
