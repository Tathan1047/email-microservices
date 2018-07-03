from django.conf.urls import url
from apps.uploadfile import views



urlpatterns = [
url(r'^uploadfile/$',views.upload_file, name="upload_file")
]
