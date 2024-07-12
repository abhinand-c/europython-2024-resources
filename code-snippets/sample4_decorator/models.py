from pydantic import BaseModel, Field


class UserModel(BaseModel):
    user_id: int = Field(
        ...,
        description="Unique Identifier",
        examples=[1],
    )
    name: str = Field(
        ..., description="User's Full Name", examples=["John Doe", "My Name"]
    )
