import os

from sensors.measures import Measures
from kafkaconfig.producer import KafkaProducer

# This main class is made for testing purposes
if __name__ == '__main__':
    topic_name = os.environ['TOPIC_NAME']
    for i in range(5):
        temp = Measures().get_temperature()
        power = Measures().get_power()
        load = Measures().get_load()

        # send data to kafka topic 'test'
        KafkaProducer().produce_json(topic_name, temp)
        KafkaProducer().produce_json(topic_name, power)
        KafkaProducer().produce_json(topic_name, load)
