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

## Deployment

### Local Kubernetes

```shell
make local-registry-up
docker-compose build
docker-compose push
make up-k8s
```