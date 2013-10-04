# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Main.work'
        db.alter_column(u'lameform_main', 'work', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Main.work'
        db.alter_column(u'lameform_main', 'work', self.gf('django.db.models.fields.TextField')(default=''))

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
            'phone': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'server': ('django.db.models.fields.TextField', [], {}),
            'verify': ('django.db.models.fields.SmallIntegerField', [], {}),
            'work': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lameform']