# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from pastebin.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Snippet, SnippetAdmin)