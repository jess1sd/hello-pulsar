# Setup 
## Install Packages
``` 
pip install requests
pip install pulsar-python
```
## Run Pulsar locally

Download docker
``` 
docker run -it -p <local-server-port>:<remote-server-port>  -p <local-admin-port>:<remote-admin-port> --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:<version> bin/pulsar standalone
docker run -it -p 6650:6650  -p 8088:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:2.10.6 bin/pulsar standalone


```

## Run test scripts
Run 