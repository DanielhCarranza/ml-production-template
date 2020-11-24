#!/bin/bash

sed 's/tensorflowORpytorch==/tensorflowORpytorch-cpu==/' requirements.txt > api/requirements.txt

docker build -t model_core_api -f api/Dockerfile .
