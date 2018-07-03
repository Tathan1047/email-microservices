import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="importers")
channel.basic_publish(
		exchange="",
		routing_key="importers",
		body =json.dumps({'From':'jmmdaya@gmailcom', 'For':'castillabend@gmail.com', 'Mensaje':'Prueba Correo'}))

print ("Finalizado")
connection.close()