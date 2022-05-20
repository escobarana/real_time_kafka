# Sending sensors' measures in real time to kafka
In order to run the code you need to have installed in your computer the following software: `https://openhardwaremonitor.org/downloads/`
*IMPORTANT*  When producing records to a Kafka Topic, OpenHardwareMonitor must be running.

## Sensors folder
In `measures.py` you can find the three different methods used to measure each sensor (Temperature, Power, Load)

## Table reference of the sensors' measure values

| Sensor Type   | Measure          |
|---------------|------------------|
| Temperature   | `ºC (Celsius)`   |
| Power         | `W (Watt)`       |
| Load          | `% (percentage)` |


## Environmental Variables 

| Variable                | Description                                |
|-------------------------|--------------------------------------------|
| `KAFKA_CLUSTER_KEY`     | Confluent Cloud Cluster Key                |
| `KAFKA_CLUSTER_SECRET`  | Confluent Cloud Cluster Secret             |
| `KAFKA_BROKER_SETTINGS` | Confluent Cloud Cluster Endpoint           |
| `KAFKA_SCHEMA_ENDPOINT` | Confluent Cloud Schema Registry Endpoint   |
| `SCHEMA_USERNAME`       | Confluent Cloud Schema Registry Key        |
| `SCHEMA_PASSWORD`       | Confluent Cloud Schema Registry API Secret |
| `TOPIC_NAME`            | Topic name to produce records to           |


## Sensor Schema (JSON) - Schema Registry

The sensor schema can be found in `kafkaconfig > utils > sensor_schema.py`. This schema will ensure that every sensor 
record sent to the kafka topic will have this structure having always properly formatted messages.