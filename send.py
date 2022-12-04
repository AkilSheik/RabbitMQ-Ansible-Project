import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='queue', durable=True)
channel.basic_publish(exchange='', routing_key='hello',body= f"{sys.argv[1]}", properties=pika.BasicProperties(
                         delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
print(f"{sys.argv[1]} was sent")
connection.close()

