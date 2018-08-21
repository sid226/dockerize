# Using Docker
Sample codes to understand how to containerize applications and use docker and docker compose.

* [more info](https://docs.docker.com/get-started/#images-and-containers)


# Requirements
* Docker
* Docker-Compose


# Try out 

## Build and run docker image locally

* Navigate to image directory
```
cd image
```
* Build image
```
docker build -t <image_name> .
```
* List images
```
docker images
```

* Run container
```
docker run -d -p <host_port>:<container_port> <image_name>
```
* List containers
```
docker ps -a
```




##  Build and push docker image to dockerhub

* Docker Login
```
docker login
```

* Navigate to image directory
```
cd image
```

* Add image version
```
echo '0.0.1' > VERSION
```

```
./release.sh <registry> <image_name>
```
* Run container
```
docker pull <registry>/<image_name>
docker run -d -p <host_port>:<container_port> <registry>/<image_name>
```

##  Run docker-compose

* Navigate to compose directory
```
cd compose
```

* Build and run containers using docker-compose
```
docker-compose -f docker-compose.yaml up -d
```
* Stop containers
```
docker-compose -f docker-compose.yaml down
```
* List containers
```
docker ps -a
```














