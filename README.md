# RPyC illustrated using Docker

A simple example of using RPyC for remote procedure calls in Python using Docker

## How-to

### Build

`docker build -t rpyc:server -f Dockerfile.server .`

`docker build -t rpyc:client -f Dockerfile.client .`

### Run

Run the server in the background:

`docker run -d -p 18861:18861 rpyc:server`

Pass the --network flag to be able to access the server via "localhost"

`docker run -it --network "host" rpyc:client`
