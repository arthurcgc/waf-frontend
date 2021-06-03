docker-build:
	docker build --tag arthurcgc/waf-frontend:latest .

docker-push:
	docker push arthurcgc/waf-frontend:latest