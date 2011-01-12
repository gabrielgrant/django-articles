from articles.models import Article, ArticleImage
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditor
from html_field.forms.widget_helper import make_toolbar_config

def article_admin_form(article_model):
	base_allow_tags = ['a','h2','em','strong','ol','ul']
	class ArticleAdminForm(forms.ModelForm):
		class Meta:
			model = article_model
			widgets = {
				'blurb': CKEditor(
					ckeditor_config=dict(width='750',
						**make_toolbar_config(
							allow_tags=base_allow_tags,
						)
					)
				),
				'body': CKEditor(
					ckeditor_config=dict(width='750',
						**make_toolbar_config(
							allow_tags=base_allow_tags + ['img'],
						)
					)
				)
			}
	return ArticleAdminForm

def article_admin(article_model):
	class ArticleAdmin(admin.ModelAdmin):
		form = article_admin_form(article_model)
		prepopulated_fields = {"slug": ("title",)}
	
	return ArticleAdmin

admin.site.register(Article, article_admin(Article))
admin.site.register(ArticleImage)


