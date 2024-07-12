from faststream.nats.fastapi import NatsRouter
from fastapi import FastAPI
from models import UserModel

router = NatsRouter("nats://localhost:4222/")


@router.subscriber("user-register")
@router.publisher("chain-event")
async def handle_user_register(
    user: UserModel,
) -> UserModel:  # Return type is also validated
    print(f"Welcome to EuroPython {user.name}, your ID is {user.user_id}")
    return user


@router.subscriber("chain-event")
async def handle_chain_event(user: UserModel) -> None:
    print(f"Recieved: {user.user_id}:{user.name}")


app = FastAPI(lifespan=router.lifespan_context)
app.include_router(router)
