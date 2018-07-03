import json
import sys
import pika


#Crear Conexion
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#Abrimos Canal de Conexion
channel = connection.channel()
#Declaramos el Exchange y su tipo
channel.exchange_declare(exchange='logs', exchange_type ='direct')
#Mensaje que se enviará
message = json.dumps({'type':'Info',
                      'code':'F0146',
                      'body':'info En Sistema'})

channel.basic_publish(exchange ='logs', routing_key='Info', body=message)
print("[*] Sent message : {}".format(message))
connection.close(   )


