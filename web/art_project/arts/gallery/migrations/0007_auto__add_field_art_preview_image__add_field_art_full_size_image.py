# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Art.preview_image'
        db.add_column('gallery_art', 'preview_image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 3, 18, 0, 0), max_length=100),
                      keep_default=False)

        # Adding field 'Art.full_size_image'
        db.add_column('gallery_art', 'full_size_image',
                      self.gf('django.db.models.fields.files.ImageField')(default=datetime.datetime(2014, 3, 18, 0, 0), max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Art.preview_image'
        db.delete_column('gallery_art', 'preview_image')

        # Deleting field 'Art.full_size_image'
        db.delete_column('gallery_art', 'full_size_image')


    models = {
        'gallery.art': {
            'Meta': {'object_name': 'Art'},
            'art_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'full_size_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'preview_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'published_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True'})
        }
    }

    complete_apps = ['gallery']