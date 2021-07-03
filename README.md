# pyechoserver

Simple python http/ REST echo server.  Serves only the reply: 
> "Hello from '_hostname_' (_<ip_addr>_)!"

Available as image on dockerhub:  https://hub.docker.com/repository/docker/dseeley/pyechoserver

## Prerequisites:
+ python3
+ gnu make
+ docker

## Test (on optional `SRV_PORT`)
```bash
[SRV_PORT=8090] python3 -m unittest test/pyechoserver_test.py -v
```

## Run locally (on optional `port`)
```bash
python3 src/main.py [--port 8090]
```

## Docker
### Create docker image
Runs built-in tests, then builds a docker image with the tag `latest`, and the (optional) `TAG` version.
```bash
[TAG=0.0.1] make dockerbuild
```

### Create docker image and push to dockerhub
Runs built-in tests, then builds a docker image and pushes to DockerHub with the tag `latest`, and the (optional) `TAG` version.
```bash
[TAG=0.0.1] make dockerpush
```

### Run in docker (on `SRV_PORT`):
```bash
docker run -d --name pyechoserver -e SRV_PORT=8090 dseeley/pyechoserver:latest
```

### Run in k8s
Also bundled a deployment and service manifests for reference.
