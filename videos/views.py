from django.shortcuts import render
from .models import YoutubeVideo


# Create your views here.
def youtube_video(request):
    video = YoutubeVideo.objects.all()
    context = {
        'video': video
    }
    return render(request, 'videos/videos.html', context)