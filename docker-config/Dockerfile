#
# Dockerfile
# Copyright (C) 2023 morita <masamorobo(a)gmail.com>
#

#####################################################################################################
## BASE image
#####################################################################################################
FROM ubuntu:20.04 AS openai-basic
ARG USER_NAME=openai
ENV DEBIAN_FRONTEND=noninteractive
# install general packages
RUN sed -i'' 's/archive.ubuntu.com/jp.archive.ubuntu.com/' /etc/apt/sources.list
RUN apt update && apt install locales sudo tzdata
RUN locale-gen en_US en_US.UTF-8
RUN update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
ENV LANG="en_US.UTF-8" \ 
    TZ="JST-9"
# install ROS2
## install general ROS2 packages
RUN apt update && apt install -y curl gnupg2 lsb-release
RUN apt update && apt install -y \
    build-essential \
    git \
    python3-pip \
    python3-pytest-cov \
    wget

## add sudo user
RUN groupadd -g 1000 developer && \
    useradd  -g developer -G sudo -m -s /bin/bash ${USER_NAME} && \
    echo "${USER_NAME}:${USER_NAME}" | chpasswd
RUN echo "Defaults visiblepw" >> /etc/sudoers
RUN echo "${USER_NAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER ${USER_NAME}
WORKDIR /home/${USER_NAME}

## install debug tools
RUN sudo apt install -y \
    vim \
    iputils-ping \
    net-tools \
    telnet \
    x11-apps

## install some pip packages needed for testing
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt 
RUN rm requirements.txt
ARG DEBIAN_FRONTEND=noninteractive

ENV TERM=xterm-256color 
ENV DISPLAY host.docker.internal:0.0

ENTRYPOINT ["/bin/bash"]