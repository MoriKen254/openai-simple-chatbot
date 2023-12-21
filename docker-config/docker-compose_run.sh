#!/bin/bash
#
# docker-compose_run.sh
# Copyright (C) 2023 MoriKen <masamorobo(a)gmail.com>
#

cd ..

docker stop openai_container
docker rm openai_container

docker-compose down
docker-compose run --name openai_simple_chatbot_container openai_simple_chatbot_service bash -d
