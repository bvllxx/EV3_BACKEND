from django.contrib.auth.models import User
from django.db import models
from shop.models import Album

class Comment(models.Model):

    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
