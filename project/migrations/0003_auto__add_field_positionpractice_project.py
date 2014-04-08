# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Positionpractice.project'
        db.add_column(u'project_positionpractice', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='pos_projet', to=orm['project.Project']),
                      keep_default=False)

        # Removing M2M table for field positionpractice on 'Project'
        db.delete_table(db.shorten_name(u'project_project_positionpractice'))


    def backwards(self, orm):
        # Deleting field 'Positionpractice.project'
        db.delete_column(u'project_positionpractice', 'project_id')

        # Adding M2M table for field positionpractice on 'Project'
        m2m_table_name = db.shorten_name(u'project_project_positionpractice')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False)),
            ('positionpractice', models.ForeignKey(orm[u'project.positionpractice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'positionpractice_id'])


    models = {
        u'project.positionpractice': {
            'Meta': {'object_name': 'Positionpractice'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'practice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pos_practice'", 'to': u"orm['project.Practice']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pos_projet'", 'to': u"orm['project.Project']"})
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
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': '()', 'max_length': '50', 'populate_from': 'None'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'project.projectcategory': {
            'Meta': {'object_name': 'ProjectCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['project']