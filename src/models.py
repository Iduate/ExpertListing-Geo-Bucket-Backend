from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from geoalchemy2 import Geometry
import datetime

Base = declarative_base()

class GeoBucket(Base):
    __tablename__ = "geo_buckets"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    centroid_lat = Column(Float)
    centroid_lng = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    spatial_index = Column(Geometry(geometry_type="POINT", srid=4326), index=True)
    properties = relationship("Property", back_populates="geo_bucket")

class Property(Base):
    __tablename__ = "properties"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    location_name = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    price = Column(Float)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    geo_bucket_id = Column(Integer, ForeignKey("geo_buckets.id"))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    spatial_index = Column(Geometry(geometry_type="POINT", srid=4326), index=True)
    geo_bucket = relationship("GeoBucket", back_populates="properties")
