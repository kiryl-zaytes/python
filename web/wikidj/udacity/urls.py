__author__ = 'Administrator'
from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from udacity.views.auth import Success
from udacity.views.main import Wiki
from udacity.views.main import Edit
from udacity.views.auth import SignOut
from udacity.views.auth import Registration
from udacity.views.auth import SignIn

urlpatterns = patterns('',
                       url(r'^success', Success.as_view(), name='user-added'),
                       url(r'^login', SignIn.as_view(), name='user-login'),
                       url(r'^wiki$', Wiki.as_view(), name='wiki'),
                       url(r'^logout', SignOut.as_view(), name='user-logout'),
                       url(r'^signup', Registration.as_view(), name='reg-user'),
                       url(r'^_edit/(?P<edit_url>([A-Za-z0-9_-]+/?)*)$', login_required(Edit.as_view()), name='edit-content'),
                       url(r'^wiki/(?P<edit_url>([A-Za-z0-9_-]+/?)*)$', Wiki.as_view(), name='wiki-dyn'),
)
