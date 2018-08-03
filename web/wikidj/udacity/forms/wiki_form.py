__author__ = 'Administrator'
from django import forms
from udacity.models import WikiContent


class WikiForm(forms.ModelForm):
    class Meta:
        model = WikiContent
        fields = ('content',)
        widgets = {'content': forms.Textarea(attrs={'cols':100, 'rows':15, 'value':'Put your text here'})}
