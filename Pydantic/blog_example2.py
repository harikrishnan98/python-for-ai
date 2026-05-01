from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    EmailStr,
    HttpUrl,
    SecretStr,
    field_validator,
    model_validator,
    ValidationInfo,
    computed_field,
    ConfigDict
)
from uuid import UUID, uuid4

from functools import partial

from uuid import UUID, uuid4

from datetime import datetime, UTC

from typing import Annotated, Literal


class User(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    uid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20, to_upper=True)]
    email: EmailStr  # Email string

    website: HttpUrl | None = None  # Optional

    password: SecretStr

    age: Annotated[
        int, Field(ge=13, le=130)
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



user1 = User(
    username="hari_krishnan", email="HKKrish@gmail.com", age=39, password="mysecret123"
)
#
# print(f"User: {user1}")
#
# print(f"Access pass val: {user1.password.get_secret_value()}")

user2 = User(username="HK_JOHN_WICK", email="HK@cc.com", age=28, password="joker123", website="fakeapi.com", first_name="Hari Krishnan", last_name="GTV", follower_count=20000)

print(f"user2 - JSON: {user2.model_dump_json(indent=2)}")

print(f"Display_name: {user2.display_name}")


class UserRegistration(BaseModel):
    username: str
    password: SecretStr
    re_enter_password: SecretStr


    @model_validator(mode="after")
    def validate_pass(self):
        if self.password != self.re_enter_password:
            raise ValueError("Password is not matching")
        return self


## Comment Model

class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0



class BlogPost(BaseModel):
    # Required Field
    title: Annotated[str, Field(min_length=1, max_length=200)]
    content: Annotated[str, Field(min_length=10)]
    author: User # Now the type of author_id is another Base Model -> User

    view_count: int = 0
    is_published: bool = False

    # default_factory for mutables and dynamic values

    tags: list[str] = Field(default_factory=list)

    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))

    status: Literal["draft", "published", "archived"] = "draft"

    # slug - only contains lower case letters, hyphens and numbers

    slug: Annotated[
        str, Field(pattern=r"^[a-z0-9-]+$")
    ]  # pattern=r" = regex Pattern with regular expression

    comments: list[Comment] = Field(default_factory=list) # default value = empty_list



# Creating Dict

post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy",
    "slug": "understanding-pydantic-models",
    "author": {
        "username": "HK_ZKr",
        "email": "hk_z@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think i understand nested models now",
            "author_email": "student1@gmail.com",
            "likes": 25
        },
        {
            "content": "Can u cover Fast API",
            "author_email": "viewer@gmail.com",
            "likes": 15
        }
    ]
}

# Using ** unpacking
# post = BlogPost(**post_data)

# Using model_validate

post = BlogPost.model_validate(post_data)

print(f"Blog Post: Post 1 {post.model_dump_json(indent=2)}")

# user1 = User(
#     username="hari_krishnan", email="HKKrish@gmail.com", age=39, password="mysecret123"
# )
#
# print(f"User: {user1}")
#
# print(f"Access pass val: {user1.password.get_secret_value()}")

# user2 = User(username="HK_JOHN_WICK", email="HK@cc.com", age=28, password="joker123", website="fakeapi.com")
#
# print(f"user2: {user2}")
 

# try:
#     ur1 = UserRegistration(username="HK_Z",password="mysecret_123", re_enter_password="my_secret_345")
# except ValidationError as e:
#     print(f"UserRegistration-Error: {e}")


# try:
#     user = User(
#         uid=0,
#         username="hk",
#         email="hk@gmail.com",
#         age=1
#     )
# except ValidationError as e:
#     print(f'error: {e}')


# post = BlogPost(
#     title="Getting started with Python",
#     content="Here's how to begin...",
#     author_id="1224",
# )
#
# print(f"BLOG-POST: {post}")





# try:
#     user = User(
#         uid=0,
#         username="hk",
#         email="hk@gmail.com",
#         age=1
#     )
# except ValidationError as e:
#     print(f'error: {e}')


# post = BlogPost(
#     title="Getting started with Python",
#     content="Here's how to begin...",
#     author_id="1224",
# )
#
# print(f"BLOG-POST: {post}")

