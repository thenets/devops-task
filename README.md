# docker-hostmetrics

Simple metrics from container's host. 

## 0. Requirements

The host most be a Linux x64 and the Docker most be installed.

Install the Docker:

```bash
# Install Docker for the most common Linux distros
curl -sSL https://get.docker.com | sh
```

## 1. How to deploy

The `hostmetrics` need to access two directories from the host. 

- `/proc` : Has information about the processes running in the related namespace and all childres.
- `/sys`  : Has information about the devices managed by the kernel in the related namespace and all childres.

Environment Variables:

- `ACCESS_KEY` : If defined, turn this key required during the HTTP requests.
- `ACCESS_IPS` : If defined, restrict the source connections to those IPs. Each IP most my separated by one space. 


### 1.1. Docker command

The easiest way to deploy the `hostmetrics` is creating a simple Docker container. Here is an example:

```bash
docker container run -d \
    --name hostmetrics \
    --restart unless-stopped \
    -p 80:5000 \
    -v /proc:/proc_host:ro \
    -v /sys:/sys_host:ro \
    -e ACCESS_KEY="myawesomepass" \ # OPTINAL
    -e ACCESS_IPS="127.0.0.1" \     # OPTINAL
    thenets/hostmetrics
```

### 1.2. Ansible Playbook

You can find an example of an Ansible Playbook at [playbook-hostmetrics.yml](playbook-hostmetrics.yml).


## 2. Examples

### 2.1 Run without access control

This example run the `hostmetrics` without any access control. Pay attention that anyone with a route to the serve can access all API endpoints.

```bash
docker container run -d \
    --name hostmetrics \
    --restart unless-stopped \
    -p 80:5000 \
    -v /proc:/proc_host:ro \
    -v /sys:/sys_host:ro \
    thenets/hostmetrics
```

### 2.2 Run with access control

This example run the `hostmetrics` with two types of access control. The first one is the `ACCESS_KEY`, so you will need to pass this string to the HTTP method GET during the request (see more in "How to use"). The second one is the `ACCESS_IPS` that allows you the pass all the IPs that will access the server.

You can use only one access control method if you want.

```bash
docker container run -d \
    --name hostmetrics \
    --restart unless-stopped \
    -p 80:5000 \
    -v /proc:/proc_host:ro \
    -v /sys:/sys_host:ro \
    -e ACCESS_KEY="myawesomepass" \
    -e ACCESS_IPS="1.2.3.4 192.168.1.40 172.46.12.1" \
    thenets/hostmetrics
```

## 3. How to use

After deploy the server you can access thoses endpoints:

- http://myserver/metrics/cpu?key=myawesomepass
- http://myserver/metrics/ram?key=myawesomepass
- http://myserver/metrics/disk?key=myawesomepass
- http://myserver/metrics/network?key=myawesomepass
- http://myserver/metrics/services?key=myawesomepass

You don't need to pass the `key` if the `ACCESS_KEY` environment variable was not defined.


### TODO

- Add unit tests.
- Add Docker Compose file.
- Improve README file with more "How to use" examples.
- Add comments to the 'simplemetrics.py' lib.
