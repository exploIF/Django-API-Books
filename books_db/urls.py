from django.urls import path
from .views import db_insertion


urlpatterns = [
    path('', db_insertion, name='db_insertion')
]