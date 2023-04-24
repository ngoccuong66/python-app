from typing import Optional

from pydantic import Field, BaseModel


class UserResponse(BaseModel):
    id: int = Field()
    user_name: str = Field()
    pass_word: str = Field()
    token: int = Field()

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True