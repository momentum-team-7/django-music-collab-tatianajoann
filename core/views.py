from django.shortcuts import render, get_object_or_404
from .models import Album
from .models import Artist
from .forms import AlbumForm, ArtistForm
from django.http import HttpResponseRedirect
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

def add_album(request,):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm()
    return render(request, 'add_album.html', {'form': form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
    return render(request, 'add_artist.html', {'form': form})


def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'edit_artist.html', {'form': form, 'artist': artist})

def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'edit_album.html', {'form': form, 'album': album})


def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/')


def delete_album(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    album.delete()
    return HttpResponseRedirect('/')