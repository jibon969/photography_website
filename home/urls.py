from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.upload_file, name='create'),
    path('delete/<int:id>/', views.file_delete, name='delete'),
    path('update/<int:id>/', views.file_update, name='update'),
    path('details/<int:id>/', views.file_details, name='details'),
]