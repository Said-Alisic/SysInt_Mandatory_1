# Mandatory 1 - System Integration

## Server 1

- Sends XML request to Server 2
- Receives CSV request from Server 3
- Run form in terminal -> Navigate to `localhost:1111/signup` (GET)
- Receive CSV and print in console after form submission -> `localhost:1111/signup` (POST)

## Server 2

- Receives XML request from Server 1
- Sends JSON request to Server 3
- Receive POST request and send to next server -> `localhost:2222/signup` (POST)

## Server 3

- Receives JSON request from Server 2
- Sends CSV to Server 1
- Receive POST request and send to next server -> `localhost:1111/signup` (POST)
