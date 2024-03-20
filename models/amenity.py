#!/usr/bin/python3
"""Defines the amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """The amenity class."""
    name: str = ""
