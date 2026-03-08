```bash
conda create -n webapp python=3.11 -y

conda activate webapp
```

## 1. Login with you AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash

sudo apt-get update -y

sudo apt-get update

# Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu 

newgrp docker
```

```bash
git clone 'your-project'
```

```bash
docker build -t yousseflarbi/imageclswebapp:latest
```

```bash
docker images -a
```

```bash
docker run -d -p 8080:8080 yousseflarbi/imageclswebapp
```

```bash
docker ps
```

```bash
docker stop_container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker push yousseflarbi/imageclswebapp:latest
```

```bash
docker rmi yousseflarbi/imageclswebapp:latest
```

```bash
docker pull yousseflarbi/imageclswebapp
```