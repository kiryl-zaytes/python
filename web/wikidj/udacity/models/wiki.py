__author__ = 'Administrator'
from django.db import models


class WikiContent(models.Model):
    class Meta:
        app_label = 'udacity'

    url = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    content_author = models.CharField(max_length=20)
    date_time = models.DateTimeField(auto_created=True)
