from pulsar import Client
import json

# Initialize the Pulsar client
client = Client('pulsar://localhost:6650')

# Subscribe to the topic and subscription
consumer = client.subscribe('my-topic',
                            subscription_name='my-sub')

# Wait for a single message
msg = consumer.receive()
try:
    # Decode and parse the JSON data
    parsed_data = json.loads(msg.data().decode('utf-8'))
    print(f"Received message: {parsed_data}")
    # Acknowledge successful processing of the message
    consumer.acknowledge(msg)
except:
    # Negative acknowledgement in case of processing failure
    consumer.negative_acknowledge(msg)

# Clean up
consumer.close()
client.close()