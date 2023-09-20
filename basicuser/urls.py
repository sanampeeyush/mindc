from django.urls import path
from . import views

urlpatterns = [
    path('creds/<str:mac>', views.wifi_credential_by_mac, name='fetch_ssid'), 
    path('create/', views.create_ssid_data, name='create-ssid-data'),
    path('update/<str:mac>/', views.update_ssid_data_by_mac, name='update-ssid-data-by-mac'),
    path('update/', views.update_ssid_data_by_mac_form_view, name='update-ssid-data-by-mac-form-view'),
]