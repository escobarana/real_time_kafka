import sys
from confluent_kafka import Consumer, KafkaError, KafkaException, DeserializingConsumer
from confluent_kafka.schema_registry.json_schema import JSONDeserializer
from confluent_kafka.serialization import StringDeserializer
from sensors.sensor import Sensor
import os
from utils.sensor_schema import schema

running = True


def dict_to_sensor(obj, ctx):
    """
    Function to transform a dictionary object to a Sensor object
    :param obj: dictionary to be transformed
    :param ctx:
    :return:
    """
    if obj is None:
        return None
    return Sensor(sensor_id=obj['sensor_id'],
                  name=obj['name'],
                  sensor_type=obj['sensor_type'],
                  measure=obj['measure'],
                  maximum=obj['maximum'])


# https://www.confluent.io/blog/getting-started-with-apache-kafka-in-python/?_ga=2.173179299.1203553419.1652971193-440072228.1652822793
class KafkaConsumer:
    """
    Class KafkaConsumer to consume data from kafka configuring the broker, schema registry
    and cloud settings from Confluent Cloud
    """
    def __init__(self):
        """
        Initialization of the class KafkaConsumer
        """
        conf = {'bootstrap.servers': os.environ["KAFKA_BROKER_SETTINGS"],
                'group.id': "foo",
                'auto.offset.reset': 'earliest'  # read from the beginning of the topic
                }

        json_deserializer = JSONDeserializer(schema, from_dict=dict_to_sensor)
        string_deserializer = StringDeserializer('utf_8')
        conf_schema = {
            'bootstrap.servers': os.environ["KAFKA_BROKER_SETTINGS"],
            'key.deserializer': string_deserializer,
            'value.deserializer': json_deserializer,
            'group.id': 'json-consumer-group-1',
            'auto.offset.reset': 'earliest'  # read from the beginning of the topic
        }

        self.serializing_consumer = DeserializingConsumer(conf_schema)
        self.consumer = Consumer(conf)

    def consume(self, topics: list):
        """
        Function to consume data from a list of topics
        :param topics: list of topics to consume data from
        :return:
        """
        try:
            self.consumer.subscribe(topics)

            while running:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None: continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                         (msg.topic(), msg.partition(), msg.offset()))
                    elif msg.error():
                        raise KafkaException(msg.error())
                else:
                    self.consumer.commit(asynchronous=False)
                    # msg_process(msg)

        finally:
            # Close down consumer to commit final offsets.
            self.consumer.close()

    def consume_json(self, topic_name: str):
        """
        Function to consume json documents from a kafka topic and print the information on screen
        :param topic_name: Name of the topic
        :return:
        """
        # https://docs.confluent.io/platform/current/installation/configuration/consumer-configs.html

        self.serializing_consumer.subscribe([topic_name])

        while True:
            try:
                msg = self.serializing_consumer.poll(1.0)
                if msg is None:
                    continue

                sensor = msg.value()
                if sensor is not None:
                    print(f'Sensor id: {sensor.id}, '
                          f'name: {sensor.name}, '
                          f'type: {sensor.type}, '
                          f'measure: {sensor.measure}, '
                          f'maximum value: {sensor.maximum}')
            except KeyboardInterrupt:
                break

        print('Closing the Consumer ...')
        self.serializing_consumer.close()
