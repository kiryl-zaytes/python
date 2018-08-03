__author__ = 'Administrator'
from udacity.models.user import User
from django.db import models


class UserManager(models.Manager):

    @classmethod
    def register(cls, user):
        user.save()

    @classmethod
    def get_all(cls):
        return User.objects.all()