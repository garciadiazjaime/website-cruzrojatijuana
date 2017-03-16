# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campana'
        db.create_table(u'donativos_campana', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('big_image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'donativos', ['Campana'])

        # Adding model 'Categoria'
        db.create_table(u'donativos_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('css_class', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'donativos', ['Categoria'])

        # Adding model 'Logros'
        db.create_table(u'donativos_logros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text_sp', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('text_en', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('link_sp', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
            ('link_en', self.gf('django.db.models.fields.URLField')(max_length=400, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['donativos.Categoria'])),
        ))
        db.send_create_signal(u'donativos', ['Logros'])

        # Adding model 'Image'
        db.create_table(u'donativos_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('alt', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'donativos', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Campana'
        db.delete_table(u'donativos_campana')

        # Deleting model 'Categoria'
        db.delete_table(u'donativos_categoria')

        # Deleting model 'Logros'
        db.delete_table(u'donativos_logros')

        # Deleting model 'Image'
        db.delete_table(u'donativos_image')


    models = {
        u'donativos.campana': {
            'Meta': {'object_name': 'Campana'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'big_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'donativos.categoria': {
            'Meta': {'object_name': 'Categoria'},
            'css_class': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'donativos.image': {
            'Meta': {'object_name': 'Image'},
            'alt': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'donativos.logros': {
            'Meta': {'object_name': 'Logros'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['donativos.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_en': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'link_sp': ('django.db.models.fields.URLField', [], {'max_length': '400', 'null': 'True', 'blank': 'True'}),
            'text_en': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'text_sp': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['donativos']