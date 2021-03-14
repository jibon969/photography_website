from django.db import models
from embed_video.fields import EmbedVideoField


# Create table for youtube video link
class YoutubeVideo(models.Model):
    title = models.CharField(max_length=120)
    video = EmbedVideoField()  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

