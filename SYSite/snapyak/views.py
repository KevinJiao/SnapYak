from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from snapyak.models import Image

def home(request):
    return HttpResponse("put images here")

class ListImageView(ListView):
    model=Image 
    template_name='image_list.html'

def ImageList(request):
    context_dict={'list':Image.objects.all()}
    return render(request, 'images.html', context_dict)
