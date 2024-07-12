from faststream.nats.fastapi import NatsRouter
from fastapi import FastAPI
from models import UserModel

router = NatsRouter("nats://localhost:4222/")


@router.subscriber("user-register")
async def handle_msg(user: UserModel) -> None:  # Return type is also validated
    print(f"Welcome to EuroPython {user.name}, your ID is {user.user_id}")


app = FastAPI(lifespan=router.lifespan_context)
app.include_router(router)
