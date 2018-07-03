from example1 import send, create_log



send.delay('jonathan.martinez.ing@gmail.com', 'jmmdaya@gmail.com', 'Este mensaje fue enviado con celery')
print("Orden Enviada")

create_log()