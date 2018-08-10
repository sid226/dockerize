#!/bin/bash

set -ex

IMAGE_NAME="${2}"
REGISTRY="${1}"

docker build -t ${REGISTRY}/${IMAGE_NAME}:latest .




