from celery import chain
from django import forms
from apps.uploadfile.models import Fileupload
from apps.uploadfile.task import getname, generate_report,sendfile, deletefile


class UploadForm(forms.ModelForm):


    class Meta:
        model = Fileupload
        fields=['filename','docfile']


    def save(self, commit=True):
        file = super(UploadForm, self).save(commit=False)
        if commit:
            file.save()
        #Funcion que realiza actividades en cadena
        (getname.s(file.id) | generate_report.si() | sendfile.s())()




