from django.contrib import admin

# Register your models here.
from apps.uploadfile.models import Fileupload

class AdminFileupload(admin.ModelAdmin):
    list_display = ['id', 'filename', 'docfile']

admin.site.register(Fileupload,AdminFileupload)