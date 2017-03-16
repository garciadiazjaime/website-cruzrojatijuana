# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Section'
        db.create_table(u'data_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title_sp', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('slug_sp', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('slug_en', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('in_main_menu', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_footer', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'data', ['Section'])

        # Adding model 'Data_DB'
        db.create_table(u'data_data_db', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('text_sp', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data.Section'])),
        ))
        db.send_create_signal(u'data', ['Data_DB'])

        # Adding model 'TransparenciaMenu'
        db.create_table(u'data_transparenciamenu', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('href_sp', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('title_sp', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('href_en', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('title_en', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'data', ['TransparenciaMenu'])


    def backwards(self, orm):
        # Deleting model 'Section'
        db.delete_table(u'data_section')

        # Deleting model 'Data_DB'
        db.delete_table(u'data_data_db')

        # Deleting model 'TransparenciaMenu'
        db.delete_table(u'data_transparenciamenu')


    models = {
        u'data.data_db': {
            'Meta': {'object_name': 'Data_DB'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['data.Section']"}),
            'text_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'text_sp': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        u'data.section': {
            'Meta': {'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_footer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_main_menu': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug_en': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'slug_sp': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'title_sp': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'data.transparenciamenu': {
            'Meta': {'object_name': 'TransparenciaMenu'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'href_en': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'href_sp': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'title_sp': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['data']