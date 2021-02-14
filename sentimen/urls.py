from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^api/historylist/$', HistoryMyList.as_view()),

    url(r'^api/history/$', HistoryListView.as_view()),
    url(r'^api/history/(?P<pk>\d+)/$', HistoryView.as_view()),
    url(r'^api/sentimen/$', SentimenListView.as_view()),
    url(r'^api/sentimen/(?P<pk>\d+)/$', SentimenView.as_view()),
]