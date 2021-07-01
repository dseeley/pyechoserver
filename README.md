# pyechoserver

Simple python http/ REST echo server.  Serves only the reply: 
> "Hello from '`hostname`'!"

## Prerequisites:
+ python3
+ gnu make
+ docker

## Test
+ `[SRV_PORT=8090] python3 -m unittest test/pyechoserver_test.py -v`

## Build
Test, then builds a docker image and pushes to DockerHub with the tag `latest`, and the (optional) `TAG`.
+ `[TAG=0.0.1] make`

## Run locally (on `port`)
+ ` python3 src/main.py [--port 8090]`

### Or run in docker (on `SRV_PORT`):
+ `docker run -d --name pyechoserver -e SRV_PORT=8090 dseeley/pyechoserver:1.0.0`

## k8s
Also bundled a deployment and service manifest for reference.
