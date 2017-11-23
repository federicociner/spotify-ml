SHELL=/bin/bash

tUSER=$(shell ./get_user.sh)
repo_tag=federicociner

image_tag=spotify-ml:latest
full_image_tag=$(repo_tag)/$(image_tag)

user_id=$$(id -u)
group_id=$$(id -g)
container_name=spotify-ml

ifeq ($(PORTP),)
PORTP=8888
endif

testuser:
	@echo $$USER
	@echo $(tUSER)
	@echo $(user_id)
	@echo $(group_id)
buildlocal:
	@echo "Building container"
	sudo docker build . --tag $(full_image_tag)

build:
	@echo "Building container"
	sudo docker build $(build_dir)

runlocal:
	@echo "Running container locally"
	sudo docker run --name $(container_name) -d -p $(PORTP):8888 -v ~/Projects:/home/notebook:z $(full_image_tag)

.PHONY: buildlocal build runlocal