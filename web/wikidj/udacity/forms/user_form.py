__author__ = 'Administrator'

from django import forms
from udacity.models import User


class UserForm(forms.ModelForm):
    password_check = forms.CharField(max_length=20, widget=forms.PasswordInput())

    class Meta:
        model = User
        widgets = {'user_password': forms.PasswordInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'user_name',
            'user_email',
            'user_password',
            'password_check'
        ]

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        pas_act = cleaned_data.get('user_password')
        pas_exp = cleaned_data.get('password_check')
        if pas_act != pas_exp:
            raise forms.ValidationError('Password fields are different!')
        return self.cleaned_data
