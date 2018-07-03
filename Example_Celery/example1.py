import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import Celery

app = Celery("example1", backend="amqp://guest:guest@localhost", broker="amqp://localhost")

@app.task
def send(remitente, destinatario, mensaje):
	# Host y puerto SMTP de Gmail
	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	# Protocolo de cifrado de datos utilizado por Gmail
	gmail.starttls()
	# Credenciales
	gmail.login('jonathan.martinez.ing@gmail.com','jmm1047384159')
	# Muestra la depuracion de la operacion de envio de email 1= True
	gmail.set_debuglevel(1)
	header = MIMEMultipart()
	header['From'] = remitente
	header['To'] = destinatario
	mensaje = MIMEText(mensaje, 'html')
	header.attach(mensaje)
	# Enviar Email
	gmail.sendmail(remitente, destinatario, header.as_string())
	# Cerrar conexion SMTP
	gmail.quit()
	return "Send Sucess"

@app.task
def create_log (ch, method, properties, body):
    info = json.loads(body)
    send= '{},{}'.format(info['type'],info['code'],info['body'] )
    file = open('info.txt','a')
    file.write(send + '\n')
    file.close()
    print("writting File txt")