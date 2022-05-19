from confluent_kafka import Producer
import os

# https://www.confluent.io/blog/getting-started-with-apache-kafka-in-python/?_ga=2.173179299.1203553419.1652971193-440072228.1652822793
class KafkaProducer:
    """
    KafkaProducer Class to send topics to kafka cloud cluster
    """
    def __init__(self):
        """
        Initialization of the class KafkaProducer configuring the broker and cloud settings
        """
        conf = {
            'bootstrap.servers': os.environ["KAFKA_BROKER_SETTINGS"],
            'security.protocol': 'SASL_SSL',
            'sasl.mechanisms': 'PLAIN',
            'sasl.username': os.environ["KAFKA_CLUSTER_KEY"],
            'sasl.password': os.environ["KAFKA_CLUSTER_SECRET"]
        }
        self.producer = Producer(conf)

    def send_data(self, topic_name: str, value):
        """
        Function to send a topic to the kafka cluster
        :param topic_name: topic name
        :param value: the value to be sent
        :return:
        """
        self.producer.produce(topic_name, value)
        # Wait up to 1 second for events. Callbacks will be invoked during
        # this method call if the message is acknowledged.
        self.producer.poll(1)
        print(f'produced to topic {topic_name}')
