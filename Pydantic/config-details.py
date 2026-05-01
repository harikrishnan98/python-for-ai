from pydantic import (
    BaseModel,
    Field,
    EmailStr,
    HttpUrl,
    SecretStr,
    field_validator,
    computed_field,
    ConfigDict
)

from datetime import datetime
from typing import Annotated

from uuid import UUID, uuid4

import json

class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        # strict=True,
        extra="allow",
        validate_assignment=True
    )


    uid: UUID = Field(alias="id",default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20, to_upper=True)]
    email: EmailStr  # Email string

    website: HttpUrl | None = None  # Optional

    password: SecretStr

    age: Annotated[
        int, Field(ge=13, le=130,strict=True)
    ]  # ge = greater than or equal to. , le = less than or equal to
    # OPTIONAL
    verified_at: datetime | None = None

    bio: str = ""
    is_active: bool = True


    first_name: str = ""

    last_name: str = ""

    follower_count: int = 0


    @field_validator("username") # Its works like after
    @classmethod
    def validate_username(cls,val: str) -> str:
        print(f'MODEL {cls.model_fields}')
        if not val.replace('_','').isalnum():
            raise ValueError("Username must be alphanumeric and underscore is allowed")
        return val.lower()

    # Runs before the pydantic validation begins for HTTP Url
    @field_validator("website", mode="before")
    @classmethod
    def modify_url(cls, val:str) -> str:
        if not val.startswith(("http://", "https://")):
            return f"https://{val}"
        return val

    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000



user_data = {
    "id": "761364f4-631a-44d7-b2e3-b2c8cea0cd1a",
    "username": "Hari_Krish",
    "email": "jokeract98@gmail.com",
    "age": 39, # we are sending a str instead of int
    "password": "secret123",
    "notes": "I am py developer"
}

# updated_data = {**user_data, "id": UUID(user_data['id'])}
#
# update_user = User.model_validate(updated_data)

user = User.model_validate_json(json.dumps(user_data))

user.email = "harikrishnan1411@gmail.com"

user.dob = "14-11-1998"

# user.some_id = "121341"

print(f"Updated User: {user.model_dump_json(indent=2)}")
# Import a dict to the Model
# user = User.model_validate(user_data )
#
# # Import a JSON to the Model
# user_1 = User.model_validate_json(json.dumps(user_data))
#
# print(f"Dict to JSON: {user_1.model_dump_json(indent=2,include={"username", "email"})}")
#
#
# print(f"User-with-Config: {user.model_dump_json(indent=2,by_alias=True,exclude={"password","is_active"})}")
#
# print(f"Include only some fields: {user.model_dump_json(indent=2,include={"username","email","age"})}")

