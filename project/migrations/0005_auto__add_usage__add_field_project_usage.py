# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Usage'
        db.create_table(u'project_usage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'project', ['Usage'])

        # Adding field 'Project.usage'
        db.add_column(u'project_project', 'usage',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Usage'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Usage'
        db.delete_table(u'project_usage')

        # Deleting field 'Project.usage'
        db.delete_column(u'project_project', 'usage_id')


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
            'baseline': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project'", 'to': u"orm['project.ProjectCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'positionpractice': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['project.Positionpractice']", 'symmetrical': 'False'}),
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