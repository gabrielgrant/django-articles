from articles.models import Article, ArticleImage
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditor
from html_field.forms.widget_helper import make_toolbar_config

def article_admin_form(article_model, extra_blurb_tags=None, extra_body_tags=None):
	base_allow_tags = ['a','h2','em','strong','ol','ul', 'img']
	if extra_blurb_tags:
		blurb_tags = base_allow_tags + extra_blurb_tags
	else:
		blurb_tags = base_allow_tags
	if extra_blurb_tags:
		body_tags = base_allow_tags + extra_blurb_tags
	else:
		body_tags = base_allow_tags
	class ArticleAdminForm(forms.ModelForm):
		class Meta:
			model = article_model
			widgets = {
				'blurb': CKEditor(
					ckeditor_config=dict(width='750',
						**make_toolbar_config(
							allow_tags=blurb_tags,
						)
					)
				),
				'body': CKEditor(
					ckeditor_config=dict(width='750',
						**make_toolbar_config(
							allow_tags=body_tags,
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


