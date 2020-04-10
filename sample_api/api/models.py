from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length = 256)

class Article(models.Model):
    slug = models.SlugField(null = False, blank = False)
    title = models.CharField(max_length = 256)
    description = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField('Tag')
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    favourited = models.BooleanField()
    favouriteContent = models.IntegerField(default = 0)
    