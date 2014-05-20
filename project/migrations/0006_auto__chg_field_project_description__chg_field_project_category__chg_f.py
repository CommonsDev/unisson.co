# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.description'
        db.alter_column(u'project_project', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Project.category'
        db.alter_column(u'project_project', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['project.ProjectCategory']))

        # Changing field 'Project.baseline'
        db.alter_column(u'project_project', 'baseline', self.gf('django.db.models.fields.CharField')(max_length=180, null=True))

    def backwards(self, orm):

        # Changing field 'Project.description'
        db.alter_column(u'project_project', 'description', self.gf('django.db.models.fields.TextField')(default=0))

        # Changing field 'Project.category'
        db.alter_column(u'project_project', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['project.ProjectCategory']))

        # Changing field 'Project.baseline'
        db.alter_column(u'project_project', 'baseline', self.gf('django.db.models.fields.CharField')(default=0, max_length=180))

    models = {
        u'project.positionpractice': {
            'Meta': {'object_name': 'Positionpractice'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Practice']"})
        },
        u'project.practice': {
            'Meta': {'object_name': 'Practice'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'example': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interest': ('django.db.models.fields.TextField', [], {}),
            'practice': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'baseline': ('django.db.models.fields.CharField', [], {'max_length': '180', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'project'", 'null': 'True', 'to': u"orm['project.ProjectCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'positionpractice': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['project.Positionpractice']", 'null': 'True', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'usage': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Usage']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'project.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'project.usage': {
            'Meta': {'object_name': 'Usage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['project']