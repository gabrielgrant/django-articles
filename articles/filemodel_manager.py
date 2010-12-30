import ckeditor_filemodel_manager as manager

from articles.models import Article, ArticleImage

class ArticleManager(manager.ModelManager):
	image_set_fieldname = 'images'
	image_fieldname = 'image'

manager.site.register(Article, 'body', ArticleManager, use_ckeditor_formfield=True)
#)
