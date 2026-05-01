from pydantic import BaseModel,ValidationError,Field

from datetime import datetime

from typing import Annotated



class User(BaseModel):
    uid: Annotated[int, Field(gt = 0)] # gt = greater than
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: str

    age: Annotated[int, Field(ge=13,le=130)] # ge = greater than or equal to. , le = less than or equal to 
     #OPTIONAL
    verified_at: datetime | None = None

    bio: str = ""
    is_active: bool = True

    #OPTIONAL
    full_name: str | None = None

u1 = User(uid=123 ,username="Hari_Krishnan", email="hari@gmail.com")

print(u1)

print(f"UserName: {u1.username}")

u1.bio = "Python Developer"

## Convert to Dict
print(f"DICT: {u1.model_dump()}")

## Covert to JSON
print(f"JSON - {u1.model_dump_json()}")

# Indent spaces
print(f"JSON - with 2 space{u1.model_dump_json(indent=2)}")

# USing try .. catch

try:
    user = User(uid="Test", username=None, email=123)

except ValidationError as e:
    print(f"VALIDATION-ERR: {e}")