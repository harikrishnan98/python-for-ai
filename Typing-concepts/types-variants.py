from pydantic import validate_call


@validate_call
def create_user(first_name: str, last_name: str, age: int) -> dict:
    email = f"{first_name.lower()}_{last_name.lower()}@gmail.com"

    return {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
    }


user1: dict = create_user("Hari Krishnan", "Velayutham", 28)
print(user1)
