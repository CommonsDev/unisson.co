# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProjectCategory'
        db.create_table(u'project_projectcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'project', ['ProjectCategory'])

        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='project', to=orm['project.ProjectCategory'])),
        ))
        db.send_create_signal(u'project', ['Project'])


    def backwards(self, orm):
        # Deleting model 'ProjectCategory'
        db.delete_table(u'project_projectcategory')

        # Deleting model 'Project'
        db.delete_table(u'project_project')


    models = {
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project'", 'to': u"orm['project.ProjectCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'project.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['project']