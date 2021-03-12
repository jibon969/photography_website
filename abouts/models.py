from django.db import models

# Create your models here.


class About(models.Model):
    title = models.CharField(max_length=120)
    aboutMe = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title