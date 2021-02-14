from django.conf.urls import url
from .views import (
    MusicianListView, MusicianView, AlbumListView, AlbumView,
    TryView
)

urlpatterns = [
    url(r'^api/try/$', TryView.as_view()),

    url(r'^api/musicians/$', MusicianListView.as_view()),
    url(r'^api/musicians/(?P<pk>\d+)/$', MusicianView.as_view()),
    url(r'^api/albums/$', AlbumListView.as_view()),
    url(r'^api/albums/(?P<pk>\d+)/$', AlbumView.as_view()),
]