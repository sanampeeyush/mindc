from django.db import models

class SSIDData(models.Model):
    ssid = models.CharField(max_length=255, unique=True)
    pwd = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)

    def __str__(self):
        return self.mac