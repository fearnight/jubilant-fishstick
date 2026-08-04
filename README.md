This repo is a practice exercice where I tried to create a complete infrasctrure.

It includes the application and the observability for the application:
Inside the application we have, a redis database and the application itself, which is a simple html
    - With the application, using a Dockerfile, we trigger a python script that use the redis database to count how many visits does the         web has
For the observability part, we have a grafana, a node-exporter and prometheus:
    - the node-exporter is installed within the docker container and gets the usage information about it(cpu used, memory...) then it sends     it to the prometheus
    then, grafana gets it and show us the information in a easy way to check it
Also, all of this has an action in github, which creates a docker image and push it to docker.hub. This action also checks if the docker-compose and the images are valid
