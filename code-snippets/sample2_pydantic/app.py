from faststream import FastStream
from faststream.nats import NatsBroker
from models import UserModel

broker = NatsBroker("nats://localhost:4222/")

app = FastStream(broker)


@broker.subscriber("user-register")
async def handle_msg(user: UserModel) -> None:  # Return type is also validated
    print(f"Welcome to EuroPython {user.name}, your ID is {user.user_id}")


@app.after_startup
async def test():
    user = UserModel(name="Abhinand", user_id=1)
    await broker.publish(user, subject="user-register")
