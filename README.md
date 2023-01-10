# Photo Editor

Turn photos to a cartoon.

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/17769668/211489351-9a4e3bcf-bbcb-409d-b382-999f7e5004c3.gif)


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
