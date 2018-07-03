from django.shortcuts import render, redirect
from apps.uploadfile.form import UploadForm
from apps.uploadfile.models import Fileupload


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("upload_file")
    else:
        form = UploadForm()

    return render(request, 'upload.html', {'form': form})

