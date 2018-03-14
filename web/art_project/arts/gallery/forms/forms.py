
from django import forms

from ..models import Art
from ..validators import title_is_text


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['art_title'].validators.append(title_is_text)


class ArtOrderForm(forms.Form):

    slug = forms.ChoiceField('Art')
    cost = forms.FloatField()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slug'].choices = [(x.art_title, x.cost) for x in Art.objects.all()]


    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Art.objects.get(slug=slug).cost > 3:
            raise forms.ValidationError(u'Cost is greater than expected!')
        return slug