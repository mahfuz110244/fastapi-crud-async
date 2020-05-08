from pydantic import BaseModel, Field


class NoteSchema(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., min_length=3, max_length=50)


class ClientSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    token: str = Field(..., min_length=3, max_length=255)


class NoteDB(NoteSchema):
    id: int
