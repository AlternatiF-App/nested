from django.shortcuts import render
from rest_framework.response import Response

from .serializers import *
from rest_framework import generics

class HistoryListView(generics.ListCreateAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, request):
        datahistory = {
            "tweet_id": request.data['tweet_id'],
            "tweet_text": request.data['tweet_text'],
            "history_sentimen": [
                {
                    "positif": request.data['positif'],
                    "negatif": request.data['negatif'],
                    "netral": request.data['netral']
                }
            ]
        }

        serializer = self.serializer_class(data=datahistory, many=True)
        serializer.is_valid()
        return Response(responseData)

class HistoryView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

class SentimenListView(generics.ListCreateAPIView):
    queryset = Sentiment.objects.all()
    serializer_class = SentimenSerializer(many=True)

class SentimenView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SentimenSerializer
    queryset = Sentiment.objects.all()