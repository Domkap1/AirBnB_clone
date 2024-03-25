#!/usr/bin/python3
"""Defines the place class."""
from models.base_models import BaseModel


class Place(BaseModel):
    """Place class."""
    amenity_ids = []
    city_id = ""
    description = ""
    latitude = 0.0
    longitude = 0.0
    max_guest = 0
    number_bathrooms = 0
    number_rooms = 0
    price_by_night = 0
    name = ""
    user_id = ""
