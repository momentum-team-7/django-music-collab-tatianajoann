"""djangomusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.homepage, name='homepage'),
    path('albums', views.albums, name='albums'),
    path('artists', views.artist, name='artists'),
    path('albums/<int:pk>/', views.album_detail, name="album-detail"),
    path('artists/<int:pk>', views.artist_detail, name="artist-detail"),
    path('albums/new', views.add_album, name="add-album"),
    path('artists/new', views.add_artist, name="add-artist"),
    path('artists/<int:pk>/edit', views.edit_artist, name="edit-artist"),
    path('albums/<int:pk>/edit', views.edit_album, name="edit-album"),
    path('artists/<int:pk>/delete', views.delete_artist, name="delete-artist"),
    path('albums/<int:pk>/delete', views.delete_album, name="delete-album")

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
