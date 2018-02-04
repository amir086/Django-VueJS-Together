from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(verbose_name='Post Body')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title
