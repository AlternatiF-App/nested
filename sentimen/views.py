from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from rest_framework import generics, status

class HistoryMyList(generics.ListCreateAPIView):
    serializer_class = HistorySer
    queryset = History.objects.all()

class HistoryListView(generics.GenericAPIView):
    serializer_class = HistorySerializer

    def post(self, request):
        serializer_class = self.serializer_class(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

class HistoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySerializer
    queryset = Sentiment.objects.all()

class SentimenListView(generics.ListCreateAPIView):
    queryset = Sentiment.objects.all()
    serializer_class = SentimenSerializer(many=True)

class SentimenView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SentimenSerializer
    queryset = Sentiment.objects.all()