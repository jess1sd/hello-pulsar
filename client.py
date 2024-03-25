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


if __name__ == '__main__':
    subscribe()
