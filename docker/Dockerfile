# spotify-ml Dockerfile

FROM federicociner/python-notebook:latest
MAINTAINER Federico Ciner <federico.ciner@gmail.com>

ARG DEBIAN_FRONTEND=noninteractive

ENV NB_USER notebook
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8

COPY . /tmp/

USER root

RUN pip install -r /tmp/requirements.txt

# run as notebook user to access Jupyter
USER $NB_USER