import json
import sys
import pika


#Crear Conexion
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#Canal de Conexion
channel = connection.channel()
#Declaramos el Exchange y su tipo
channel.exchange_declare(exchange='logs', exchange_type ='fanout')
#Mensaje que se enviará
message = json.dumps({'type':'Info',
                      'code':'F0145',
                      'body':'Error En Sistema'})

channel.basic_publish(exchange ='logs', routing_key='', body=message)
print("[*] Sent message : {}".format(message))
connection.close(   )


