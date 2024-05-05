from django.db import models

class Video(models.Model):
    video_name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

class VideoLabel(models.Model):
    label = models.CharField(max_length=100)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['-last_used']