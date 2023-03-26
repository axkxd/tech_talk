from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import PhotoForm
from .models import Photo


def home(request):
    return HttpResponse("tech talk - я читаю!")


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            return HttpResponseRedirect(reverse('photo_detail', args=[photo.id]))
    else:
        form = PhotoForm()
    return render(request, 'tt_blog/upload_photo.html', {'form': form})


def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'tt_blog/photo_detail.html', {'photo': photo})