import typing

import pydantic
class Pokemon(pydantic.BaseModel):
    name: str
    weight: int
    abilities: list