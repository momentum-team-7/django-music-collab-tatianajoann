from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist
# Create your views here.

# def index(request):
#     albums = Albums.objects.all()
#     return render(request, 'index.html', {'albums': albums})


def homepage(request):
    albums = Album.objects.all()
    return render(request, 'homepage.html', {'albums': albums})


def artist(request):
    artists = Artist.objects.all()
    return render(request, 'artist.html', {'artists': artists})

def albums(request):
    albums = Album.objects.all()
    return render(request, 'albums.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_detail.html', {'artist': artist})