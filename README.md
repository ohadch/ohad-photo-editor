# Photo Editor
Turn photos to a cartoon.

## Requirements
- Python 3.7
- node & yarn

## Quick Start

```shell
make up
```

## Setup a development environment

### Backend

```shell
cd server
pip install -r requirements.txt
pre-commit install
```

### Frontend

```shell
cd frontend
yarn
yarn dev
```

## Deploy on local Kubernetes

```shell
# Spin up the local helm repo and docker registry
make local-docker-compose-local-repo-and-registry-up

# Build the local docker images
docker-compose build

# Push the images to the local registry
docker-compose push

# Install the local helm repo
make up-k8s
```
