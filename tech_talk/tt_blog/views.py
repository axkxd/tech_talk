from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PhotoForm


def home(request):
    return HttpResponse("Hello, Django!")


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PhotoForm()
    return render(request, 'tt_blog/upload_photo.html', {'form': form})