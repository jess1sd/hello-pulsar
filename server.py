import pulsar


def produce():
    client = pulsar.Client('pulsar://localhost:6650')
    producer = client.create_producer('my-topic')

    for i in range(10):
        producer.send(('hello-pulsar-%d' % i).encode('utf-8'))
        stats = producer.stats()
        print (stats)
    client.close()


if __name__ == '__main__':
    produce()
