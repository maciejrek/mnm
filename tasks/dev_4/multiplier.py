import pika
import time

sleepTime = 5
print('[*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)

print('[*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print('[*] Waiting for messages.')


def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)
    cmd = body.decode()

    val1, val2 = cmd.split(" ")

    result = int(val1) * int(val2)
    print(f" {val1} * {val2} = {result}")
    print(" [x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
