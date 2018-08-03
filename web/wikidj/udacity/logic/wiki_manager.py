__author__ = 'Administrator'

from udacity.models.wiki import WikiContent
from django.db import models


class WikiManager(models.Manager):
    @classmethod
    def get_content_by_url(cls, url):
        try:
            wiki_row = WikiContent.objects.get(url=url)
            return wiki_row.content
        except WikiContent.DoesNotExist:
            return ''

    @classmethod
    def get_wiki_obj(cls, url):
        try:
            wiki_row = WikiContent.objects.get(url=url)
            return wiki_row
        except WikiContent.DoesNotExist:
            return ''