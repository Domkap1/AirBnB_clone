#!/user/bin/python3
"""Defines the user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """The user class."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
