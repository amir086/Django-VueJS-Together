from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

from api.models import Post
from api.serializers import PostSerializer


def index(request):
    return render(request, 'index.html')


class PostListView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
