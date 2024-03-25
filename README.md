# Setup 
## Install Packages
``` 
pip install requests
pip install pulsar-client
```
## Run Pulsar locally

Download docker
``` 
docker run -it -p <local-server-port>:<remote-server-port>  -p <local-admin-port>:<remote-admin-port> --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:<version> bin/pulsar standalone
docker run -it -p 6650:6650  -p 8088:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:2.10.6 bin/pulsar standalone


```

## Run test scripts
Run client to subscribe and start listening. 
``` 
$ python client.py

```
You should see logs like 
``` 
2024-03-25 13:19:09.614 INFO  [0x1f5275e00] Client:86 | Subscribing on Topic :my-topic
2024-03-25 13:19:09.615 INFO  [0x1f5275e00] ClientConnection:190 | [<none> -> pulsar://localhost:6650] Create ClientConnection, timeout=10000
2024-03-25 13:19:09.615 INFO  [0x1f5275e00] ConnectionPool:114 | Created connection for pulsar://localhost:6650-0
2024-03-25 13:19:09.617 INFO  [0x16fbf7000] ClientConnection:404 | [[::1]:55131 -> [::1]:6650] Connected to broker
2024-03-25 13:19:09.693 INFO  [0x16fbf7000] HandlerBase:83 | [persistent://public/default/my-topic, my-sub, 0] Getting connection from pool
2024-03-25 13:19:09.863 INFO  [0x16fbf7000] BinaryProtoLookupService:87 | Lookup response for persistent://public/default/my-topic, lookup-broker-url pulsar://localhost:6650, from [[::1]:55131 -> [::1]:6650] 
2024-03-25 13:19:10.181 INFO  [0x16fbf7000] ConsumerImpl:298 | [persistent://public/default/my-topic, my-sub, 0] Created consumer on broker [[::1]:55131 -> [::1]:6650] 
...
```
Then open another terminal and send some test messages using server.py. 
This script will just run and exit. 
``` 
python server.py
```
Then go back to the client.py terminal and you should see that the client has 
received messages
``` 
Received message: 'b'hello-pulsar-0''
Received message: 'b'hello-pulsar-1''
Received message: 'b'hello-pulsar-2''
Received message: 'b'hello-pulsar-3''
Received message: 'b'hello-pulsar-4''
Received message: 'b'hello-pulsar-5''
Received message: 'b'hello-pulsar-6''
Received message: 'b'hello-pulsar-7''
Received message: 'b'hello-pulsar-8''
Received message: 'b'hello-pulsar-9''
...
```
To print the stats for a topic, one can use pulsar's admin api. To test it out, 
open another terminal and run 
``` 
python stats.py
```
And you should see stats in json format, printed every 5 seconds until the server.py process is killed:
``` 
{'msgRateIn': 0.0, 'msgThroughputIn': 0.0, 'msgRateOut': 0.0, 'msgThroughputOut': 0.0, 'bytesInCounter': 490, 'msgInCounter': 10, 'bytesOutCounter': 490, 'msgOutCounter': 10, 'averageMsgSize': 0.0, 'msgChunkPublished': False, 'storageSize': 490, 'backlogSize': 0, 
'publishRateLimitedTimes': 0, 'earliestMsgPublishTimeInBacklo...
```