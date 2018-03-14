# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Art.art_title2'
        db.delete_column('gallery_art', 'art_title2')


    def backwards(self, orm):
        # Adding field 'Art.art_title2'
        db.add_column('gallery_art', 'art_title2',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2014, 2, 27, 0, 0), max_length=33),
                      keep_default=False)


    models = {
        'gallery.art': {
            'Meta': {'object_name': 'Art'},
            'art_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['gallery']