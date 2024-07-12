import asyncio
from faststream.nats import NatsBroker

from models import UserModel

broker = NatsBroker("nats://localhost:4222/")


async def main():
    async with NatsBroker() as br:
        user = UserModel(name="Tony Stark", user_id=10)
        await br.publish(user, subject="user-register")


asyncio.run(main())
