from rest_framework import serializers

from api.models import Post

__author__ = 'Ashraful'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at')
