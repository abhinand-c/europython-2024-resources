from faststream import FastStream
from faststream.nats import NatsBroker

broker = NatsBroker("nats://localhost:4222")
app = FastStream(broker)


@broker.subscriber("*.info", "workers")
async def base_handler1(body: str):
    print(f"handler1-{body=}")


@broker.subscriber("*.info", "workers")
async def base_handler2(body: str):
    print(f"handler2-{body=}")


@broker.subscriber("*.error", "workers")
async def base_handler3(body: str):
    print(f"handler3-{body=}")


@app.after_startup
async def send_messages():
    await broker.publish("This is an info log", "logs.info")  # handlers: 1 or 2
    await broker.publish("This is also an info log", "logs.info")  # handlers: 1 or 2
    await broker.publish("This is an error log", "logs.error")  # handlers: 3
