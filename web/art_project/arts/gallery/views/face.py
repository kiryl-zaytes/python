from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView, ListView, View, TemplateView

from ..forms import ArtOrderForm

from ..models.art import Art
from ..forms import ArtForm


class ArtActionMixin(object):
    @property
    def action(self):
        msg = "{0} is missing action.".format(self.__class__)
        raise NotImplementedError(msg)

    def form_valid(self, form):
        msg = "Art {0}!".format(self.action)
        messages.info(self.request, msg)
        return super().form_valid(form)


class ArtDetailView(DetailView):
    model = Art
    slug_field = 'slug'


class ArtListView(ListView):
    model = Art

    def get_queryset(self):
        query_set = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            return query_set.filter(art_title__contains=q)
        return query_set


class ArtCreateView(ArtActionMixin, CreateView):
    model = Art
    action = 'created'
    form_class = ArtForm


class ArtUpdateView(ArtActionMixin, UpdateView):
    model = Art
    action = 'updated'
    form_class = ArtForm


class ArtChoice(View):
    template = 'gallery/art_choice_form.html'
    form = ArtOrderForm()

    def get(self, request):
        return render(request,ArtChoice.template, {'form':self.form})
