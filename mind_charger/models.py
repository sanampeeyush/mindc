from django.db import models
import os


def upload_location(self, _):
    return f"audio_files/{self.date.strftime('%d-%m-%Y')}-{self.button_id}.mp3"


class AudioFile(models.Model):
    date = models.DateField()
    button_id = models.CharField(
        choices=[
            ("01", "01"),
            ("02", "02"),
            ("03", "03"),
            ("04", "04"),
            ("05", "05"),
            ("06", "06"),
            ("07", "07"),
            ("08", "08"),
            ("09", "09"),
            ("10", "10"),
        ],
        max_length=2,
        default="01",
    )
    audio = models.FileField(upload_to=upload_location)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.date)}-{self.button_id}"

    def delete(self, *args, **kwargs):
        if self.audio:
            if os.path.isfile(self.audio.path):
                os.remove(self.audio.path)
        super(AudioFile, self).delete(*args, **kwargs)
