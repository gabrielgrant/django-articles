# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'ArticleImage.display_image'
        db.alter_column('articles_articleimage', 'display_image', self.gf('static_filtered_images.fields.FilteredImageField')(no_old_src_field=True, max_length=200))

        # Changing field 'ArticleImage.image'
        db.alter_column('articles_articleimage', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=200))


    def backwards(self, orm):
        
        # Changing field 'ArticleImage.display_image'
        db.alter_column('articles_articleimage', 'display_image', self.gf('static_filtered_images.fields.FilteredImageField')(no_old_src_field=True, max_length=100))

        # Changing field 'ArticleImage.image'
        db.alter_column('articles_articleimage', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))


    models = {
        'articles.article': {
            'Meta': {'object_name': 'Article'},
            'blurb': ('django.db.models.fields.TextField', [], {}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'articles.articleimage': {
            'Meta': {'object_name': 'ArticleImage'},
            '_old_image_source_for_display_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'article': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['articles.Article']"}),
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'display_image': ('static_filtered_images.fields.FilteredImageField', [], {'no_old_src_field': 'True', 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['articles']
