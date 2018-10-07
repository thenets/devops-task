IMAGE_TAG=thenets/devops-task:latest

# Volumes used to access host's kernel data
REQUIRED_VOLUMES= \
	-v /proc:/proc_host:ro \
	-v /sys:/sys_host:ro


# Build Docker image
build:
	docker build -t $(IMAGE_TAG) .

# Run server in the development mode
server-development:
	docker run -it --rm \
		-e DEBUG=TRUE \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_VOLUMES} \
		$(IMAGE_TAG)

# Enter inside the container's bash
shell:
	docker run -it --rm \
		-e DEBUG=TRUE \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_VOLUMES} \
		$(IMAGE_TAG) bash

# Run server in the production mode
server-production:
	docker run -it --rm \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_VOLUMES} \
		$(IMAGE_TAG)
