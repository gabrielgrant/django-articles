from datetime import date

from django.db import models


class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique_for_date='pub_date')
	blurb = models.TextField()
	body = models.TextField(blank=True)
	pub_date = models.DateField('date published', default=date.today)
	published = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.title

def img_location(instance, filename):
	return 'article_images/article_%d/%s'%(instance.story.id, filename)

class ArticleImage(models.Model):
	article = models.ForeignKey('Article', related_name='images')
	credit = models.CharField(max_length=200, blank=True)
	caption = models.TextField(blank=True)
	image = models.ImageField(upload_to=img_location)

def get_permalink_dict(article):
	return {
		'year': article.pub_date.strftime("%Y").lower(),
		'month':article.pub_date.strftime("%b").lower(),
		'day':article.pub_date.strftime("%d").lower(),
		'slug': article.slug,
	}
