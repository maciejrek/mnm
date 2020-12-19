import pika
import random
import time


def generate_int_pair():
    """
    Generate pair of ints. Rand range is fixed cause it wasn't specified in task.
    :return: List(int,int)
    """
    return [str(random.randint(1, 100)), str(random.randint(1, 100))]


def generate_list_of_int_pairs():
    """
    Generate list of int pairs. Range value is fixed cause it wasn't specified in task.
    :return: List(List(int,int))
    """
    return [generate_int_pair() for _ in range(100)]


def send_data_to_message_broker():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    body = generate_int_pair()
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=' '.join(body),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    print(f"Message sent, message body:{body}")
    return body


def generate_data_samples():
    res = []
    for i in range(100):
        res.append(send_data_to_message_broker())
    with open("file.txt", 'w') as file:
        for item in res:
            file.write(f"{item}\n")
    print(f"Data set:{res}")


sleepTime = 15
print(' [*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(sleepTime)
generate_data_samples()
