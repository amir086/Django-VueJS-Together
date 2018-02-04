from django.urls import path

from api.views import PostListView

__author__ = 'Ashraful'

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list-view'),
]
