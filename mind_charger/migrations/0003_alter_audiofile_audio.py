# Generated by Django 4.2.4 on 2024-07-22 10:30

from django.db import migrations, models
import mind_charger.models


class Migration(migrations.Migration):

    dependencies = [
        ("mind_charger", "0002_remove_audiofile_title_audiofile_button_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="audiofile",
            name="audio",
            field=models.FileField(upload_to=mind_charger.models.upload_location),
        ),
    ]
