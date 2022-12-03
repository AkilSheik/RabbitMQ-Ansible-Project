import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello',body= f"{sys.argv[1]}")
print(f"{sys.argv[1]}")
connection.close()

