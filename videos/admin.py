from django.contrib import admin
from .models import YoutubeVideo


# Here Register Youtube Video models
class YoutubeVideoAdmin(admin.ModelAdmin):

    list_display = ['title',  'video', 'timestamp']

    class Meta:
        model: YoutubeVideo


admin.site.register(YoutubeVideo, YoutubeVideoAdmin)