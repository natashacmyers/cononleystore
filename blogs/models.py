
from django.db import models
from profiles.models import UserProfile

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(
        'Blog', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='blogs')
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
