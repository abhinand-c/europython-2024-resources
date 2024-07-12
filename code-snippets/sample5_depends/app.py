from faststream import FastStream, Depends
from faststream.nats import NatsBroker

broker = NatsBroker("nats://localhost:4222")
app = FastStream(broker)


def simple_dependency():
    """A simple function to demostrate dependency injection"""
    return 1


@broker.subscriber("test")
async def handler(body: str, d: int = Depends(simple_dependency)):
    assert d == 1
    print(f"{body=} and {d=} ")


@app.after_startup
async def test():
    await broker.publish("Hello EuroPython", subject="test")
