import json
from pulsar import Client

# Initialize the Pulsar client
client = Client('pulsar://localhost:6650')

# Create a producer on the topic you wish to publish to
producer = client.create_producer('my-topic')

# Your data
data = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Serialize your data to JSON
json_data = json.dumps(data)

# Send the JSON data
producer.send(json_data.encode('utf-8'))

print("JSON message sent to Pulsar topic.")

# Clean up
producer.close()
client.close()
