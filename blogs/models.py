from django.db import models
from profiles.models import UserProfile
import uuid
import datetime

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    datetime = datetime.datetime.now()

    def __str__(self):
        return self.name


class Comment(models.Model):
    blog = models.ForeignKey(
        'Blog', null=True, blank=True, on_delete=models.SET_NULL)
    user_profile = models.ForeignKey(
        UserProfile, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='comments')
    comment_number = models.CharField(max_length=32, null=False, editable=False)
    description = models.TextField()
    datetime = datetime.datetime.now()

    def _generate_comment_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()
  
    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.comment_number:
            self.comment_number = self._generate_comment_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.comment_number
