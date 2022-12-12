from django import forms
from .models import ApplicationForm


class AppForm(forms.ModelForm):
	class Meta:
		model = ApplicationForm
		fields = ['name', 'phone', 'choice', 'call_time']