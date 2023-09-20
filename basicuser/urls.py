from django.urls import path
from . import views

urlpatterns = [
    path('creds/<str:mac>', views.wifi_credential_by_mac, name='fetch_ssid'), 
    path('create/', views.create_ssid_data, name='create-ssid-data'),    
]