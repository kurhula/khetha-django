from django.contrib import admin
from django.urls import path

urlpatterns: list = [path("admin/", admin.site.urls)]
