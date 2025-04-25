from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    weight: int
    abilities: list