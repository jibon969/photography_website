from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.youtube_video, name='video'),
]