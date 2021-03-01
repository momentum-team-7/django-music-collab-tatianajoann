from django.shortcuts import render
from .models import Album
# Create your views here.


def index(request):
    return render(request, '../templates/index.html')
