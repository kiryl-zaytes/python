from django.conf.urls import patterns, url

from .views import ArtCreateView
from .views import ArtDetailView
from .views.face import ArtUpdateView, ArtListView, ArtChoice

urlpatterns = patterns('',

    url(r'^arts/(?P<slug>\w+)', ArtDetailView.as_view() , name='arts'),
    url(r'^add', ArtCreateView.as_view(), name='add_art'),
    url(r'^update/(?P<slug>\w+)', ArtUpdateView.as_view(), name='update_art'),
    url(r'^search', ArtListView.as_view(), name='search_art'),
    url(r'^choice', ArtChoice.as_view(), name='chose_art'),

    )

