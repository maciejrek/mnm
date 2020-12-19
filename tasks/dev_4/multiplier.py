import pika
import time
from db_handler import connect_to_db, create_table


sleepTime = 10
print('[*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)

create_table()
print('[*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print('[*] Waiting for messages.')


def callback(ch, method, properties, body):
    conn = connect_to_db()
    cur = conn.cursor()
    print(" [x] Received %s" % body)
    cmd = body.decode()

    val1, val2 = cmd.split(" ")

    result = int(val1) * int(val2)
    cur.execute(f"INSERT INTO MY_TABLE (NUMBER1,NUMBER2,RESULT) VALUES ({int(val1)},{int(val2)},{result})")
    print(f" {val1} * {val2} = {result}")
    conn.commit()
    conn.close()
    print(" [x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
