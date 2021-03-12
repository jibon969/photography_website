from django.shortcuts import render
from .models import About


# Create your views here.
def about(request):
    queryset = About.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, 'abouts/abouts.html', context)