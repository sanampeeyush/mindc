from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . import models
# Create your views here.

from .forms import SSIDDataForm, MacForm

def update_ssid_data_by_mac_form_view(request):
    form = MacForm()
    if request.method == 'POST':
        form = MacForm(request.POST)
        if form.is_valid():
            mac = form.cleaned_data.get('mac')
            return redirect('update-ssid-data-by-mac', mac = mac)
    return render(request, 'basicuser/create_ssid_data_using_mac.html',{'form': form,})

def update_ssid_data_by_mac(request, mac):
    ssid_data = get_object_or_404(models.SSIDData, mac=mac)
    
    if request.method == 'POST':
        form = SSIDDataForm(request.POST, instance=ssid_data)
        if form.is_valid():
            form.save()
            return redirect('home_page')  # Redirect to a success page after form submission
    else:
        form = SSIDDataForm(instance=ssid_data)
    
    return render(request, 'basicuser/update_ssid_data.html', {'form': form, 'ssid_data': ssid_data})

def create_ssid_data(request):
    if request.method == 'POST':
        form = SSIDDataForm(request.POST)
        if form.is_valid():
            mac_address = form.cleaned_data['mac']
            
            # Check if a record with the same MAC address already exists
            existing_record = models.SSIDData.objects.filter(mac=mac_address).first()
            if existing_record:
                # Handle the case where the MAC address already exists
                return render(request, 'duplicate_mac_error.html')
            
            # If no existing record found, save the new record
            form.save()
            return redirect('success')  # Redirect to a success page after form submission
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