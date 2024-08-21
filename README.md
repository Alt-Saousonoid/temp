## Run simulation

```sh
docker-compose up
```

will print something like 
```sh
Starting saria-project_server_1 ... done
Starting saria-project_client2_1 ... done
Starting saria-project_client1_1 ... done
Attaching to saria-project_server_1, saria-project_client1_1, saria-project_client2_1
server_1   | INFO :      Starting Flower server, config: num_rounds=30, no round_timeout
server_1   | INFO :      Flower ECE: gRPC server running (30 rounds), SSL is disabled
server_1   | INFO :      [INIT]
server_1   | INFO :      Requesting initial parameters from one random client
client2_1  | INFO :
client2_1  | INFO :      Received: get_parameters message 86032f22-c7c7-452e-8a65-25582e391167
client2_1  | INFO :      Sent reply
server_1   | WARNING :   Failed to receive initial parameters from the client. Empty initial parameters will be used.
server_1   | INFO :      Evaluating initial global parameters
server_1   | INFO :
server_1   | INFO :      [ROUND 1]
server_1   | INFO :      configure_fit: strategy sampled 2 clients (out of 2)
client1_1  | INFO :
client1_1  | INFO :      Received: train message 3ca931b4-32c2-4e22-834c-69532300a0ac
client2_1  | INFO :
client2_1  | INFO :      Received: train message 3f970626-7376-47d0-84a1-21ac6a3519fd
client2_1  | INFO :      Sent reply
client1_1  | INFO :      Sent reply
server_1   | INFO :      aggregate_fit: received 2 results and 0 failures
server_1   | Unexpected Error Occurred
server_1   | Model saved at: multitask.pth
```

## docker requirements

```
docker-ce
docker-compose
```