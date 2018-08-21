## Exercises

- Fork https://github.com/sid226/dockerize

- Create a simple **Hello World!! REST application with a hit counter** in your own language (java,node,python)
	1. Copy application code into a docker image
	2. Build docker image using Ubuntu 16.04 as the base image 
- Write a docker compose file, that:
	1. For your image, Exposes REST endpoints POST/GET from container to host
	2. Add a MySQL/Mongo DB/LevelDB container (Dont use Redis! You can refer to the sample created using Redis)
	3. Mount database volume from host machine to local to persistent DB data across container deletes/restarts (the container mount location will vary depending on the database, refer to you specific DockerHub image documentation to find this out)
- Push to docker registry in Gitlab
- Need few different exercises for different people
  - Run as non-root
  - Constrained resources
  - Slim images
  - Volumes in read only mode
