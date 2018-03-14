# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Art'
        db.create_table('gallery_art', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('art_title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('artist', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('published_by', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('art_title2', self.gf('django.db.models.fields.CharField')(max_length=33)),
        ))
        db.send_create_signal('gallery', ['Art'])


    def backwards(self, orm):
        # Deleting model 'Art'
        db.delete_table('gallery_art')


    models = {
        'gallery.art': {
            'Meta': {'object_name': 'Art'},
            'art_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'art_title2': ('django.db.models.fields.CharField', [], {'max_length': '33'}),
            'artist': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_by': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['gallery']