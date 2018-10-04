IMAGE_TAG=thenets/devops-task:latest

build:
	docker build -t $(IMAGE_TAG) .

test-shell:
	docker run -it --rm \
		-v $(PWD):/app \
		-v /proc:/proc_host:ro \
		-p 5000:5000 \
		$(IMAGE_TAG) bash
