import sys

from confluent_kafka import Consumer, KafkaError, KafkaException
import os

running = True

# https://www.confluent.io/blog/getting-started-with-apache-kafka-in-python/?_ga=2.173179299.1203553419.1652971193-440072228.1652822793
class KafkaConsumer:
    def __init__(self):
        conf = {'bootstrap.servers': os.environ["KAFKA_BROKER_SETTINGS"],
                'group.id': "foo",
                'auto.offset.reset': 'earliest'  # read from the beginning of the topic
                }
        self.consumer = Consumer(conf)

    def consume_topic(self, topics: list):
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
