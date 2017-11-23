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

# Install required python packages
RUN pip install -r /tmp/requirements.txt

# Install XGBoost
RUN cd /usr/local/lib/ && git clone --recursive https://github.com/dmlc/xgboost \
    && cd xgboost \
    && make -j4  \
    && cd python-package \
    && python setup.py install

# run as notebook user to access Jupyter
USER $NB_USER