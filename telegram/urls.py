from django.urls import include, path

from telegram import api
from . import views

urlpatterns = [
    path('api/', api.sample_api, name='sample_api'),
    path('my_form/', views.my_form_view, name='my_form_view'),
]
