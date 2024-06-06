import json

from aiokafka import AIOKafkaProducer, AIOKafkaConsumer

from .config import KAFKA_BOOTSTRAP_SERVERS


async def send_kafka_message(topic: str, message: dict):
    producer = AIOKafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS)
    await producer.start()
    try:
        value_json = json.dumps(message).encode('utf-8')
        await producer.send_and_wait(topic, value_json)
    finally:
        await producer.stop()


async def consume_kafka_messages(topic: str, group_id: str):
    print('Consuming kafka messages')
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=group_id,
        auto_offset_reset='earliest'
    )
    await consumer.start()
    try:
        async for msg in consumer:
            message = json.loads(msg.value.decode('utf-8'))
            print(f"Consumed message: {message}")
    finally:
        await consumer.stop()
