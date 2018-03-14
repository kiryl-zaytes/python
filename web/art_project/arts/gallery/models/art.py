from django.db import models
from django.core.urlresolvers import reverse

from ..models.core_models import TitleAbstract


class Art(TitleAbstract):
    class Meta:
        app_label = 'gallery'

    artist = models.CharField(max_length=50)
    published_by = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    # preview_image = models.ImageField(width_field=500, height_field=500, upload_to='')
    # full_size_image = models.ImageField(width_field=1920, height_field=1080, upload_to='')
    slug = models.SlugField(unique=True)
    cost = models.FloatField()


    def get_absolute_url(self):
        return reverse("arts", kwargs={"slug": self.slug})
