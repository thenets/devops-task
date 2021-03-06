IMAGE_TAG=thenets/hostmetrics:latest

# - Volumes used to access host's kernel data
# - Key and IPs allowed
REQUIRED_PARAMS= \
	-v /proc:/proc_host:ro \
	-v /sys:/sys_host:ro \
	-e ACCESS_KEY="0q5YeCfBAryPtxTDQfB9O4cr72HrHOUjtK" \
	-e ACCESS_IPS="127.0.0.1 172.17.0.1"

# Build Docker image
build:
	docker build -t $(IMAGE_TAG) .

# Run server in the development mode
server-development:
	docker run -it --rm \
		-e DEBUG=TRUE \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG)

# Enter inside the container's bash
shell:
	docker run -it --rm \
		-e DEBUG=TRUE \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG) bash

# Enter inside the container's bash as root
shell-root:
	docker run -it --rm \
		-u root \
		-e DEBUG=TRUE \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG) bash

# Run server in the production mode
server-production:
	docker run -it --rm \
		-p 5000:5000 \
		-v $(PWD):/app \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG)

# Test production mode without mount local volume
server-test:
	docker run -it --rm \
		-p 5000:5000 \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG)

# Run all unit tests
unit-test:
	docker run -it --rm \
		-p 5000:5000 \
		${REQUIRED_PARAMS} \
		$(IMAGE_TAG) /app/unit-test.sh