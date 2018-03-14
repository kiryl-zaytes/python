from django.db import models

from ..validators import title_is_text


class TitleAbstract(models.Model):
    # art_title = models.CharField(max_length=30, validators=[title_is_text])
    art_title = models.CharField(max_length=30)

    class Meta:
        abstract = True