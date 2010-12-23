from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, DetailView
from django.utils.decorators import classonlymethod
from django.utils.html import strip_tags
from inline_edit.views import ConditionalDispatchView

def strip_link(text):
	return strip_tags(text).strip()

def is_link(text):
	stripped_text = strip_link(text)
	return stripped_text and not (' ' in stripped_text)

class ArticleView(ConditionalDispatchView):
	"""
	Dispatches a DetailView or a RedirectView, if the Article body is a link
	
	If 'model' is passed into the 'as_view' method, only published articles
	are used. So:
	
	ArticleView().as_view(model=Event)
	
	Is equivalent to:
	
	ArticleView().as_view(queryset=Event.objects.filter(published=True))
	
	To override this behaviour if you actually want all the objects
	(regardless of published status), do:
	
	ArticleView().as_view(queryset=NewsArticle.objects.all())
	
	Of course, further filtering of the queryset is also possible:
	
	ArticleView().as_view(queryset=NewsArticle.objects.filter(
		published=True, category__name="Art News"
	))
	"""
	template_name_suffix = '_article'
	
	@classonlymethod
	def as_view(cls, **kwargs):
		# what happens with CBG views when model is passed as a kwarg,
		# but queryset is set as a property on the view?
		if 'model' in kwargs and 'queryset' not in kwargs:
			kwargs['queryset'] = kwargs['model'].objects.filter(published=True)
		return super(ArticleView, cls).as_view(**kwargs)

	class Meta:
		class true_view_class(RedirectView, DetailView):
			def get_redirect_url(self, **kwargs):
				model = self.get_queryset().model
				article = get_object_or_404(model, pk=kwargs['pk'])
				return strip_link(article.body)
				
		false_view_class = DetailView
		@staticmethod
		def condition_func_factory(true_model, false_model):
			model = false_model
			def condition_func(request, *args, **kwargs):
				article = get_object_or_404(model, pk=kwargs['pk'])
				return is_link(article.body)
			return condition_func
