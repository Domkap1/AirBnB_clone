#!/usr/bin/python3
"""Defines the place class."""
from models.base_models import BaseModel


class Place(BaseModel):
    """Place class."""
    amenity_ids: list[str] = []
    city_id: str = ""
    description: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    max_guest: int = 0
    number_bathrooms: int = 0
    number_rooms: int = 0
    price_by_night: int = 0
    name: str = ""
    user_id: str = ""
