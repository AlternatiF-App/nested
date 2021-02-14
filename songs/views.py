from django.shortcuts import render
from .serializers import *
from rest_framework import generics


class MusicianListView(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class MusicianView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MusicianSerializer
    queryset = Musician.objects.all()

class TryView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = TrySerializer

class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer(many=True)

class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()