from pydantic import BaseModel, Field


class ClientBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=80
    )
    lastname: str = Field(
        ...,
        min_length=2,
        max_length=80
    )


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    pass


class ClientResponse(ClientBase):
    id: int