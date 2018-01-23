from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^film/favorite/$', views.favorite1, name='favorite'),
    url(r'^director/$', views.director, name='director'),
    url(r'^director/favorite/$', views.favorite2, name='favorite'),
    url(r'^film/$', views.director, name='film'),
    url(r'^publisher/$', views.publisher, name='publisher'),
    url(r'^publisher/favorite/$', views.favorite3, name='favorite'),

]