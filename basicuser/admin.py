from django.contrib import admin
from . import models
# Register your models here.

class WiFiCredentialAdmin(admin.ModelAdmin):
    list_display = ('mac', 'ssid', 'pwd')

admin.site.register(models.SSIDData, WiFiCredentialAdmin)