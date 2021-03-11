from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import UploadFileForm
from django.contrib import messages
from django.db.models import Q


# Create your views here.
def home(request):
    photo_queryset = Photo.objects.all()
    search = request.GET.get('q')
    if search:
        photo_queryset = photo_queryset.filter(
            Q(title__icontains=search)
        )
    context = {
        'photo_queryset': photo_queryset
    }
    return render(request, 'home/index.html', context)


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Post successfully created ')
            return redirect('home')
    else:
        form = UploadFileForm()
        messages.add_message(request, messages.DEBUG, 'Please again create post ')
    return render(request, 'home/form.html', {'form': form})


def file_details(request, id):
    detail = get_object_or_404(Photo, id=id)
    context = {
        'object': detail
    }
    return render(request, 'home/details.html', context)


def file_update(request, id):
    obj = get_object_or_404(Photo, pk=id)
    form = UploadFileForm(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS, 'Post successfully Update ')
        return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'home/form.html', {"form": form})


def file_delete(request, id):
    obj = Photo.objects.filter(pk=id)
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Post successfully created ')
    return redirect('home')


