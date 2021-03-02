from django.shortcuts import render
from .models import Album
from .models import Artist
# Create your views here.


def index(request):
    albums = Album.objects.all()
    return render(request, 'index.html', {'albums': albums})


def artist(request):
    artists = Artist.objects.all()
    return render(request, 'artist.html', {'artists': artists})