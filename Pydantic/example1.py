from pydantic import BaseModel


def create_user(username, email, age=None):
    if not isinstance(username, str):
        raise TypeError("Username must be string")

    if not isinstance(email, str):
        raise TypeError("Email must be string")

    if not isinstance(age, int):
        raise TypeError("AGE must be Integer")
    
create_user.__defaults__


user1 = create_user("HK", "hk_krish@gmail.com", 27)
print(user1)

user2 = create_user("johndoe", "doe_joh@gmail.com", "old")
print(user2)


class User(BaseModel):
        username: str
        email: str
        age: int | str

user1 = User(username="HK", email="hk_krish@gmail.com", age=27)

print(user1)

user2 = User(username="John", email="HK@cc.com", age="29")

print(user2)
