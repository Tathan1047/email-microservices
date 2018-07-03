
from celery import current_app
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from Django_Celery.settings import ADMIN_EMAIL
from apps.uploadfile.models import Fileupload
from xlrd import open_workbook
import xlsxwriter

app = current_app

@app.task()
def test_uploadfile():
    print ("I am uploading file")

@app.task()
def getname (upload_id):
    f=Fileupload.objects.get(pk=upload_id)#obtener objeto Fileupload que tiene mi archivo
    header =(
        'id',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined'
    )

    workbook = open_workbook(f.docfile.path)
    print (workbook)
    sheet = workbook.sheet_by_index(0)

    for index,row in enumerate(sheet.get_rows()):
        if index ==0:
            continue
        kwargs = dict(zip(header, [value.value for value in row]))

        from django.contrib.auth.models import User
        User.objects.create(**kwargs)





@app.task()
def generate_report():
   user = User.objects.filter(is_active=1)

   print(user)

   workbook =xlsxwriter.Workbook('documents/Report_user_Active.xls')
   worksheet = workbook.add_worksheet()

   worksheet.write(0,0,"id")
   worksheet.write(0,1,"is_superuser")
   worksheet.write(0,2,"username")
   worksheet.write(0,3,"first_name")
   worksheet.write(0,4,"last_name")
   worksheet.write(0,5,"email")
   worksheet.write(0,6,"is_staff")
   worksheet.write(0,7,"is_active")

   for x, z in enumerate(user, start=1):
       worksheet.write(x, 0, z.id)
       worksheet.write(x, 1, z.is_superuser)
       worksheet.write(x, 2, z.username)
       worksheet.write(x, 3, z.first_name)
       worksheet.write(x, 4, z.last_name)
       worksheet.write(x, 5, z.email)
       worksheet.write(x, 6, z.is_staff)
       worksheet.write(x, 7, z.is_active)

   workbook.close()

   return 'documents/Report_user_Active.xls'

@app.task
def sendfile(path):
    e = EmailMessage()
    e.attach_file(path)
    e.body = "Those users are active"
    e.subject = "Users Actives in our server"
    e.to = ADMIN_EMAIL
    e.send()
    return path








