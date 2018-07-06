# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Snippet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LANGS = (
        ('python', 'Python'),
        ('javascript', 'Javascript'),
    )

    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=140)
    code = models.TextField()
    lang = models.CharField(max_length=40, choices=LANGS)

    def __unicode__(self):

        return u'{}'.format(self.title)


