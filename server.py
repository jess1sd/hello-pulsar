# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pulsar


def subscribe():
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe('my-topic',
                                subscription_name='my-sub')

    while True:
        msg = consumer.receive()
        print("Received message: '%s'" % msg.data())
        consumer.acknowledge(msg)

    client.close()

def produce():
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer('my-topic')

    for i in range(10):
        producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
        stats = producer.stats()
        print (stats)
    client.close()

def stat():
    client = pulsar.Client('pulsar://localhost:6650')
    consumer = client.subscribe('my-topic', 'my-sub')
    stats = consumer.stats()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    produce()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
