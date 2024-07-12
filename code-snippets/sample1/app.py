from faststream import FastStream
from faststream.nats import NatsBroker
# from faststream.kafka import KafkaBroker
# from faststream.confluent import KafkaBroker
# from faststream.rabbit import RabbitBroker
# from faststream.redis import RedisBroker

broker = NatsBroker("nats://localhost:4222")
# broker = KafkaBroker("localhost:9092")
# broker = RabbitBroker("amqp://guest:guest@localhost:5672/")
# broker = RedisBroker("redis://localhost:6379/")

app = FastStream(broker)


@broker.subscriber("test")
async def base_handler(body):
    print(f"Recieved: {body}")


@app.after_startup
async def test():
    await broker.publish("Hello EuroPython", subject="test")
