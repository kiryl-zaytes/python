from django.contrib.auth.models import AnonymousUser, AbstractBaseUser
from django.db import models
from django.core.validators import RegexValidator


class User(AbstractBaseUser):
    class Meta:
        app_label = 'udacity'

    user_name = models.CharField(
        max_length=15, blank=False, unique=True,
        validators=[
            RegexValidator('^[a-z0-9_-]{3,16}$',
                           message='Invalid user name')
        ]
    )

    user_password = models.CharField(
        max_length=20, blank=False,
        validators=[
            RegexValidator('^[a-z0-9_-]{6,18}$')
        ]
    )
    user_email = models.EmailField(blank=True)

    def __str__(self):
        return ''.join([
            self.user_name,
            self.user_email
        ])