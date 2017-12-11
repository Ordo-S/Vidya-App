from django.conf.urls import url

from . import views


urlpatterns = [
 	url(r'^$', views.index, name='index'),
 	url(r'^games/$', views.GamesListView.as_view(), name='games'),
 	url(r'^game/(?P<pk>\d+)$', views.GameDetailView.as_view(), name='game-detail'),
 	url(r'^signup/$', views.signup, name='signup'),
 	url(r'^game/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
 	#url(r'^search/$', views.SerachListView, name='search')
 	url(r'^publisher/$', PublisherListView.as_view(), name='publisher')
 	
]