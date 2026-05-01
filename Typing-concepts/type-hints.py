from typing import NewType, Any

from dataclasses import dataclass

import random

RGB = NewType("RGB", tuple[int, int, int])

HSL = NewType("HSL", tuple[int, int, int])


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | None = None

    def generate_mail(self):
        return f"{self.first_name}_{self.last_name}@gmail.com"


def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> User:
    email = f"{first_name.lower()}_{last_name.lower()}@gmail.com"

    return User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        age=age,
        fav_color=fav_color,
    )


# We are justing creating a class and returning it


def random_choice[T](items: list[T]) -> T:
    return random.choice(items)


u1: User = create_user("Hari", "Krishnan", 28, fav_color=RGB((103, 200, 432)))

u2: User = create_user("John", "Wick", 28, fav_color=RGB((201, 301, 320)))

u1.first_name
u1.email

u2.age
u2.last_name

users = [u1, u2]

random_user = random_choice(users)

email_users = [user.email for user in users]

random_mail = random_choice(email_users)
print(random_mail)
u1.first_name

u1.generate_mail()


## Data class decorator example
def add_method(cls):
    def status_fn(self):
        print(f"Wrapper! fn Your status: {self.status}")

    cls.status_fn = status_fn
    return cls


## Adding Typing to a library methods

import requests

resp = requests.get("https://www.hotstar.com/in/home", timeout=5)
status = resp.status_code
