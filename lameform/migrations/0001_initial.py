# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Main'
        db.create_table(u'lameform_main', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('family', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.TextField')()),
            ('edu', self.gf('django.db.models.fields.TextField')()),
            ('work', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('verify', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('code', self.gf('django.db.models.fields.TextField')()),
            ('server', self.gf('django.db.models.fields.TextField')()),
            ('arrived', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal(u'lameform', ['Main'])


    def backwards(self, orm):
        # Deleting model 'Main'
        db.delete_table(u'lameform_main')


    models = {
        u'lameform.main': {
            'Meta': {'ordering': "('family', 'name')", 'object_name': 'Main'},
            'arrived': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'edu': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'family': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.TextField', [], {}),
            'server': ('django.db.models.fields.TextField', [], {}),
            'verify': ('django.db.models.fields.SmallIntegerField', [], {}),
            'work': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['lameform']