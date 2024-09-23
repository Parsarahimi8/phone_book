from pydantic import BaseModel

class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    description: str | None = None 

class PersonOut(PersonCreate):
    id: int

    class Config:
        orm_mode = True  # This allows the Pydantic model to work with SQLAlchemy models
