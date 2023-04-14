from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Tag(models.Model):
    title = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title

class Snippet(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag,related_name='snippets',on_delete=models.CASCADE)

    def __str__(self):
        return self.title
