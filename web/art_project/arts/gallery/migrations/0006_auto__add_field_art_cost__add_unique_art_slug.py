# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Art.cost'
        db.add_column('gallery_art', 'cost',
                      self.gf('django.db.models.fields.FloatField')(default=4),
                      keep_default=False)

        # Adding unique constraint on 'Art', fields ['slug']
        db.create_unique('gallery_art', ['slug'])


    def backwards(self, orm):
        # Removing unique constraint on 'Art', fields ['slug']
        db.delete_unique('gallery_art', ['slug'])

        # Deleting field 'Art.cost'
        db.delete_column('gallery_art', 'cost')


    models = {
        'gallery.art': {
            'Meta': {'object_name': 'Art'},
            'art_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cost': ('django.db.models.fields.FloatField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['gallery']