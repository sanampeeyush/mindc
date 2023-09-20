from django.contrib import admin
from . import models
# Register your models here.

class WiFiCredentialAdmin(admin.ModelAdmin):
    list_display = ('ssid', 'pwd', 'mac')

admin.site.register(models.SSIDData, WiFiCredentialAdmin)