sh:
	docker-compose run --rm consumer /bin/bash
run:
	docker-compose up
test:
	docker-compose run --rm consumer pytest -v
