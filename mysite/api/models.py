from django.db import models
from django.utils import timezone

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=120,blank=True,null=True)

    def __str__(self):
        return self.title
