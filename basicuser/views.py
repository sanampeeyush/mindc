from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models
# Create your views here.

from .forms import SSIDDataForm

def create_ssid_data(request):
    if request.method == 'POST':
        form = SSIDDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to a success page after form submission
    else:
        form = SSIDDataForm()
    return render(request, 'basicuser/create_ssid_data.html', {'form': form})

def wifi_credential_by_mac(request, mac):
    try:
        wifi_credential = models.SSIDData.objects.get(mac=mac)
        data = {
            'ssid': wifi_credential.ssid,
            'pwd': wifi_credential.pwd,
            'mac': wifi_credential.mac,
        }
        return JsonResponse(data, status=200)
    except models.SSIDData.DoesNotExist:
        # Handle the case where the specified MAC address is not found
        return JsonResponse({}, status=404)