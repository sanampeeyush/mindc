from django import forms
from .models import SSIDData

class SSIDDataForm(forms.ModelForm):
    class Meta:
        model = SSIDData
        fields = ['ssid', 'pwd', 'mac']

class MacForm(forms.Form):
    mac = forms.CharField(label='MAC Address', max_length=17)