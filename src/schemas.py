from pydantic import BaseModel, Field
from typing import Optional

class PropertyCreate(BaseModel):
    title: str
    location_name: str
    lat: float
    lng: float
    price: float
    bedrooms: int
    bathrooms: int

class PropertyOut(BaseModel):
    id: int
    title: str
    location_name: str
    lat: float
    lng: float
    price: float
    bedrooms: int
    bathrooms: int
    geo_bucket_id: int

    class Config:
        from_attributes = True

class GeoBucketStats(BaseModel):
    bucket_id: int
    name: str
    property_count: int
    centroid_lat: float
    centroid_lng: float
