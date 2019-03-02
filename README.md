This is a simple Flask Application in order to solve an API exercise.

Disclaimer: I am aware we need to add unit test and other software best practice but for the first version is ok to go.

If you want to build and execute this project, ensure you have installed:
<br>
**Docker stack**
	`-Docker`
	`-Docker composer`
	`-Python 3.6`

You can find the requirements file, this file is needed in order to build the docker image.
Additional to docker files the file db_resource.py is required in order to build the schema, in case you want to modify the current schema if not everything is set just to be executed in docker build command.

The next libraries were used as dependencies for this exercise:
<br>
	`* flask`
	`* flask-restful`
	`* flask-sqlalchemy`
	`* flask_jsontools`
	`* flask-Redis`
	`* flask-Injecto`
	`* connexion[swagger-ui]`
	`* redis`
	

**Execution:**
<br>
If you have Docker stack installed and docker composer installed by just run:

	**Run docker composer**

	`docker-compose up `

In case you want to build the image isolate, but remember you should change the environment variables to connect to redis
<br>
**Docker**

`$ sudo docker build --rm -t dog_running_sa .`

`$ docker run -p 8098:8098 dog_running_sa `

<br>


Once you have the project up and running go to :

	`http://localhost:8098/v1.0/ui/`

 This endpoint has the swagger utility to document the endpoints.

