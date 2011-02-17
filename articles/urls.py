from django.conf.urls.defaults import *
from django.views.generic.dates import DateDetailView, DayArchiveView,  \
	MonthArchiveView, YearArchiveView, ArchiveIndexView
from articles.views import ArticleDateView
from articles.models import Article


def get_patterns(info_dict, basename):
	urlpatterns = patterns('',
		url(
			r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[\w-]+)/$',
			type(
				'ArticleDateView', (ArticleDateView,), info_dict,
			).as_view(**dict(slug_field='slug')),
			name='%s_detail' % basename
		),
		url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
			type(
				'ArticleDayArchiveView', (DayArchiveView,), info_dict,
			).as_view(),
			name='%s_day' % basename
		),
		url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
			type(
				'ArticleMonthArchiveView', (MonthArchiveView,), info_dict,
			).as_view(),
			name='%s_month' % basename
		),
		url(r'^(?P<year>\d{4})/$',
			type(
				'ArticleYearArchiveView', (YearArchiveView,), info_dict,
			).as_view(),
			name='%s_year' % basename
		),
		url(r'^/?$',
			type(
				'ArticleArchiveIndexView', (ArchiveIndexView,), info_dict,
			).as_view(),
			name='%s_index' % basename
		),
	)
	return urlpatterns


base_info_dict = {
	'queryset': Article.objects.filter(published=True),
	'date_field': 'pub_date',
}
urlpatterns = get_patterns(base_info_dict, 'article')
