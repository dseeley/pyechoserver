TAG := $(if $(TAG),$(TAG),latest)
IMG_NAME := $(if $(IMG_NAME),$(IMG_NAME),pyechoserver)
DOCKERREPO = dseeley/$(IMG_NAME)

test: FORCE
	python3 -m unittest discover -s test -p pyechoserver_test.py

dockerbuild: test
	docker build --pull -t $(DOCKERREPO):$(TAG) -t $(DOCKERREPO):latest .

dockerpush: dockerbuild
	docker push $(DOCKERREPO):$(TAG)
	docker push $(DOCKERREPO):latest

FORCE:
