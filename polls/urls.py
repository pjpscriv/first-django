from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',                        views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$',         views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote,             name='vote')



    # url(r'^$', views.index, name='index'),
    # url(r'^detail/(?P<question_id>[0-9]+)/',  views.detail,  name="detail"),
    # url(r'^results/(?P<question_id>[0-9]+)/', views.results, name="results"),
    # url(r'^vote/(?P<question_id>[0-9]+)/',    views.vote,    name="vote")
]
