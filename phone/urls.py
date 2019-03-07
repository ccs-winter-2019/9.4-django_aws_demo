from django.contrib import admin
from django.urls import path

from . import views

app_name = 'phone'

urlpatterns = [
    path('', views.DamageReportList.as_view(), name='report_list'),
    path('create/', views.CreateDamageReport.as_view(), name='report_create'),
]