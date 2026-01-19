-------------------Test locally with Docker------------------
1. Start Docker Desktop
2. Build the docker at the same route where your folder is located (sentiment-web-app)

docker build -t multimodal-ai .
3. Test locally with docker

docker run -p 8000:8000 --env-file .env multimodal-ai

4.Open:
For Fast API

http://localhost:8000/
For local server:

http://localhost:8000/static/index.html

5. If you need to remove the Docker:

	a. Stop the container:
		docker ps
		docker stop <container_id_or_name>

	b. Remove the container:
		docker rm <container_id_or_name>

	c. Remove a specific Image + containers
		docker ps -a
		docker rm -f <container_id_or_name>
		docker rmi <container_id_or_name>
		 
		If it complains that the image is in use:

			docker rmi -f <container_id_or_name>

	d. Remove unused containers, images, networks and cache:
		

		docker system prune


		-Include Unused images:

			docker system prune -a

		-Clean Build Cache only:
		
			docker builder prune

	e. Check disk usage:

		docker system df

## To build faster without the previous cache
docker build --no-cache=false -t multimodal-ai .