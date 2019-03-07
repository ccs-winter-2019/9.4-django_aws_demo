from django.forms import ModelForm

from .models import DamageReport


class DamageReportForm(ModelForm):
    class Meta:
        model = DamageReport
        fields = ('title', 'broken_phone', )
