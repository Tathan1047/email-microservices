import json
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
    send= '{},{}'.format(info['type'],info['code'],info['body'] )
    file = open('info.txt','a')
    file.write(send + '\n')
    file.close()
    print("writting File txt")



channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()