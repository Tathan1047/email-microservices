import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pika


#Crear Conexion
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel =connection.channel()

channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)


results = channel.queue_declare(exclusive= True)
queue_name = results.method.queue
channel.queue_bind(exchange = 'logs', queue= queue_name)
print('[*] Staritng worker with queue {}'.format(queue_name))


def callback (ch, method, properties, body):
    info = json.loads(body)
    data = '{}'.format(info['type'])
    print(data)
    send(data)


def send(mensaje):
    if mensaje == "Error":
    	# Host y puerto SMTP de Gmail
        gmail = smtplib.SMTP('smtp.gmail.com', 587)
        # Protocolo de cifrado de datos utilizado por Gmail
        gmail.starttls()
        # Credenciales
        gmail.login('jonathan.martinez.ing@gmail.com','jmm1047384159')
        # Muestra la depuracion de la operacion de envio de email 1= True
        gmail.set_debuglevel(1)
        header = MIMEMultipart()
        header['From'] = 'jonathan.martinez.ing@gmail.com'
        header['To'] = 'jmmdaya@gmail.com'
        mensaje = MIMEText(mensaje, 'html')
        header.attach(mensaje)
        # Enviar Email
        gmail.sendmail('jonathan.martinez.ing@gmail.com', 'jmmdaya@gmail.com', header.as_string())
        # Cerrar conexion SMTP
        gmail.quit()
    else:
        print("There isn't Error, Don't Send Email")




channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()
