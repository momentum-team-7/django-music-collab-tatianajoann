from django import forms
from .models import Album, Artist

'''Django documentation on forms can be found here https://docs.djangoproject.com/en/3.1/topics/forms/'''

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title']

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['first_name']