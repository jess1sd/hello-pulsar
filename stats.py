import time

import requests

# Replace these variables with your actual Pulsar cluster information
pulsar_admin_url = 'http://localhost:8088'
tenant = 'public'
namespace = 'default'
topic = 'my-topic'

# Construct the URL for topic stats
# curl http://localhost:8080/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool

url = f"{pulsar_admin_url}/admin/v2/persistent/{tenant}/{namespace}/{topic}/stats"

def get_stats() -> str:
    # Make the GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        stats = response.json()
        return stats
    else:
        return "Failed to retrieve stats:" + response.status_code

if __name__ == "__main__":
    while (True):
        print(get_stats())
        print ("\n\nWill pull in 5 more seconds\n\n")
        time.sleep(5)