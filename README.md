### Website-checker
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/triklozoid/webchecker/Python%20application)


#### Howto run project

##### Requirements
- [docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

##### Kafka & Postgresql connection

- You need to create `.env` file with connection information, example:
```
DATABASE_URL=postgres://login:password@hostname:port:port/dbname
KAFKA_HOST=localhost
KAFKA_PORT=21388

```
- You need to create `certs` folder in the root of the project and put kafka connection certificates there
```
$ ls certs
ca.pem  service.cert  service.key
```

##### Run

```
docker-compose up
```

