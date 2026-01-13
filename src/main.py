from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src.models import Base, Property, GeoBucket
from src.schemas import PropertyCreate, PropertyOut, GeoBucketStats
from src.utils import normalize_location_name, fuzzy_match
from geoalchemy2.shape import to_shape
from sqlalchemy import func

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/properties", response_model=PropertyOut)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    # Find existing buckets within 500m
    point_wkt = f"POINT({property.lng} {property.lat})"
    bucket = db.query(GeoBucket).filter(
        func.ST_DWithin(GeoBucket.spatial_index, func.ST_GeomFromText(point_wkt, 4326), 0.5)
    ).first()
    if not bucket:
        # Create new bucket
        bucket = GeoBucket(
            name=normalize_location_name(property.location_name),
            centroid_lat=property.lat,
            centroid_lng=property.lng,
            spatial_index=func.ST_GeomFromText(point_wkt, 4326)
        )
        db.add(bucket)
        db.commit()
        db.refresh(bucket)
    prop = Property(
        title=property.title,
        location_name=property.location_name,
        lat=property.lat,
        lng=property.lng,
        price=property.price,
        bedrooms=property.bedrooms,
        bathrooms=property.bathrooms,
        geo_bucket_id=bucket.id,
        spatial_index=func.ST_GeomFromText(point_wkt, 4326)
    )
    db.add(prop)
    db.commit()
    db.refresh(prop)
    return prop

@app.get("/api/properties/search", response_model=list[PropertyOut])
def search_properties(location: str = Query(...), db: Session = Depends(get_db)):
    buckets = db.query(GeoBucket).all()
    bucket_names = [b.name for b in buckets]
    matches = fuzzy_match(location, bucket_names, threshold=2)
    if not matches:
        raise HTTPException(status_code=404, detail="No matching location found")
    matched_buckets = db.query(GeoBucket).filter(GeoBucket.name.in_(matches)).all()
    bucket_ids = [b.id for b in matched_buckets]
    properties = db.query(Property).filter(Property.geo_bucket_id.in_(bucket_ids)).all()
    return properties

@app.get("/api/geo-buckets/stats", response_model=list[GeoBucketStats])
def bucket_stats(db: Session = Depends(get_db)):
    buckets = db.query(GeoBucket).all()
    stats = []
    for b in buckets:
        count = db.query(Property).filter(Property.geo_bucket_id == b.id).count()
        stats.append(GeoBucketStats(
            bucket_id=b.id,
            name=b.name,
            property_count=count,
            centroid_lat=b.centroid_lat,
            centroid_lng=b.centroid_lng
        ))
    return stats
