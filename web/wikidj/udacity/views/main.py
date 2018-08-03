import datetime
from django.http import HttpResponseRedirect
from udacity.forms.wiki_form import WikiForm

__author__ = 'Administrator'
from django.shortcuts import render
from django.views.generic.base import View
from udacity.logic.wiki_manager import WikiManager


class Wiki(View):
    template = 'udacity/wiki_main_page.html'

    def get(self, request, edit_url=''):
        is_auth = request.user.is_authenticated()
        content = WikiManager.get_content_by_url(edit_url)
        if edit_url == '' or content:
            return render(request, self.template, {'is_auth': is_auth, 'content': content})
        else:
            return HttpResponseRedirect('/udacity/_edit/{0}'.format(edit_url), {'content': content, 'url': edit_url})


class Edit(View):
    template = 'udacity/wiki_main_page.html'

    def get(self, request, edit_url=''):
        content_to_edit = WikiManager.get_content_by_url(edit_url)
        form = WikiForm(initial={'content': content_to_edit})
        return render(request, Edit.template, {'form': form})

    def post(self, request, edit_url=None):
        if edit_url == 'wiki':
            edit_url = ''
        instance_for_update = WikiManager.get_wiki_obj(edit_url)
        if instance_for_update:
            form = WikiForm(request.POST, instance=instance_for_update)
        else:
            form = WikiForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.url = edit_url
            obj.content_author = request.user
            obj.date_time = datetime.datetime.today()
            obj.save()
            return HttpResponseRedirect('/udacity/wiki/{0}'.format(edit_url))

