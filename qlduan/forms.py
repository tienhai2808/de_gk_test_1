from django import forms
from .models import DuAn

class DuAnForm(forms.ModelForm):
  class Meta:
    model = DuAn
    fields = '__all__'