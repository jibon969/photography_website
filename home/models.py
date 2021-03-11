from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField
# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-update"]
