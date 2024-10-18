# -*- coding: utf-8 -*-

from django.urls import path
from .views import register, login, get_user_config, update_user_config

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('getfishConfig', get_user_config, name='get_user_config'),
    path('updatefishConfig', update_user_config, name='update_user_config'),
]

