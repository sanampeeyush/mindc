from django import forms
from .models import SSIDData

class SSIDDataForm(forms.ModelForm):
    class Meta:
        model = SSIDData
        fields = ['ssid', 'pwd', 'mac']