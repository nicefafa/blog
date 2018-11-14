#!/usr/bin/python3
# -*-coding:utf-8 -*-



from django.urls import path
from . import views

urlpatterns = [
    path('update_comment',views.update_comment,name="update_comment")
]