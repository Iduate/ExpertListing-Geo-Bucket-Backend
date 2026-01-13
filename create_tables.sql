-- Create geo_buckets table
CREATE TABLE IF NOT EXISTS geo_buckets (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    centroid_lat FLOAT NOT NULL,
    centroid_lng FLOAT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    spatial_index GEOMETRY(POINT, 4326)
);

-- Create index on name
CREATE INDEX IF NOT EXISTS idx_geo_buckets_name ON geo_buckets(name);

-- Create properties table
CREATE TABLE IF NOT EXISTS properties (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    location_name VARCHAR NOT NULL,
    lat FLOAT NOT NULL,
    lng FLOAT NOT NULL,
    price FLOAT NOT NULL,
    bedrooms INTEGER NOT NULL,
    bathrooms INTEGER NOT NULL,
    geo_bucket_id INTEGER REFERENCES geo_buckets(id),
    created_at TIMESTAMP DEFAULT NOW(),
    spatial_index GEOMETRY(POINT, 4326)
);

-- Create index on spatial_index
CREATE INDEX IF NOT EXISTS idx_geo_buckets_spatial ON geo_buckets USING GIST(spatial_index);
CREATE INDEX IF NOT EXISTS idx_properties_spatial ON properties USING GIST(spatial_index);
