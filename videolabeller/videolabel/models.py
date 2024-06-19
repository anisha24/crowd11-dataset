from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=True, null=True)
    last_used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-last_used']

class Video(models.Model):
    video_name = models.CharField(max_length=100)
    label = models.ForeignKey(Label, on_delete=models.CASCADE, null=True, related_name='videos')