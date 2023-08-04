from django.shortcuts import render

from typing import NamedTuple
from collections.abc import Iterator

from faker import Faker
import string

def get_credentials():
    faker = Faker()

    characters = string.ascii_letters
    password_characters = string.ascii_letters + string.digits

    login = faker.lexify(text="?" * 8, letters=characters)
    password = faker.lexify(text="?" * 12, letters=password_characters)


    domain_name = faker.unique.domain_name()
    email = f"{login}@{domain_name}"

    return login, email, password



class User(NamedTuple):
    login: str
    email: str
    password: str

def generate_user() -> User:
    credentials = get_credentials()

    return User(
        login=credentials[0],
        email=credentials[1],
        password=credentials[2],
    )

def generate_users(amount=20) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()






def generator(request):
    user_generator = generate_users()


    unique_user_set = set(user_generator)
    user_list = list(unique_user_set)

    return render(
        request=request,
        template_name="index.html",
        context={"users": user_list, "view_name": "generate_users"},
    )
