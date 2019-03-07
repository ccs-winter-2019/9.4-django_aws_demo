from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import DamageReport
from .forms import DamageReportForm


class DamageReportList(ListView):
    model = DamageReport


class CreateDamageReport(CreateView):
    model = DamageReport
    form_class = DamageReportForm
    success_url = reverse_lazy('phone:report_list')
