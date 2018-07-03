from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pika
import json
import smtplib


def send(remitente, destinatario, mensaje):
	# Host y puerto SMTP de Gmail
	gmail = smtplib.SMTP('smtp.gmail.com', 587)
	# Protocolo de cifrado de datos utilizado por Gmail
	gmail.starttls()
	# Credenciales

	gmail.login('jmmdaya@gmail.com','XXXXXXXXXX')

	gmail.login('jmmdaya@gmail.com','jmm1047384159')

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


def importers (ch, method, properties, body):
    info = json.loads(body)
    send(info['From'], info['For'], info['Mensaje'])


if __name__ == "__main__":
	connection = pika.BlockingConnection(
		pika.ConnectionParameters('localhost')
	)

	channel = connection.channel()
	channel.queue_declare(queue="importers")

	channel.basic_consume(importers, queue="importers", no_ack=True)
	print("inicio del Worker")
	channel.start_consuming()


