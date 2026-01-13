# Geo-Bucket Property Search System Design

## 1. Geo-Bucket Strategy

**Goal:** Group nearby properties into logical buckets to ensure consistent, typo-tolerant search results.

- **Bucket Definition:**
  - Each bucket represents a circular area with a fixed radius (e.g., 500 meters).
  - Properties within this radius are assigned to the same bucket.
  - Buckets are created dynamically based on property locations.
  - Each bucket has a canonical location name (e.g., "Sangotedo") and centroid coordinates.

- **Grouping Logic:**
  - When a property is added, its coordinates are checked against existing buckets.
  - If within the radius of a bucket centroid, it is assigned to that bucket.
  - Otherwise, a new bucket is created.

## 2. Database Schema

**Tables:**

- `geo_buckets`
  - id (PK)
  - name (canonical location name)
  - centroid_lat
  - centroid_lng
  - created_at
  - spatial_index (PostGIS geometry)

- `properties`
  - id (PK)
  - title
  - location_name
  - lat
  - lng
  - price
  - bedrooms
  - bathrooms
  - geo_bucket_id (FK to geo_buckets)
  - created_at
  - spatial_index (PostGIS geometry)

**Indexes:**
- Spatial index on `geo_buckets.spatial_index` and `properties.spatial_index` for fast geo-queries.
- Index on `geo_buckets.name` for fast location name lookup.

**Relationships:**
- Each property links to one geo-bucket via `geo_bucket_id`.

## 3. Location Matching Logic

- **String Matching:**
  - Normalize input (lowercase, remove punctuation, trim whitespace).
  - Use fuzzy string matching (Levenshtein distance) to match location names.
  - Map variants like "Sangotedo", "Sangotedo, Ajah", "sangotedo lagos" to the same bucket.

- **Coordinate Proximity:**
  - If a search includes coordinates, find buckets within a threshold radius.
  - If only a name is provided, use fuzzy matching to find the best bucket(s).

- **Combined Logic:**
  - Search input is normalized and matched against bucket names.
  - If multiple buckets match, return properties from all relevant buckets.

## 4. Flow Diagram

```
User Search (e.g., "Sangotedo")
        |
        v
Normalize & Fuzzy Match Location Name
        |
        v
Find Matching Geo-Bucket(s)
        |
        v
Query Properties in Bucket(s)
        |
        v
Return Property Results
```

## Example
- User searches for "Sangotedo".
- System normalizes and matches to bucket(s) with canonical name "Sangotedo" (including variants).
- Returns all properties in those buckets.

---

This design ensures consistent, reliable, and typo-tolerant property search results using geo-buckets and spatial indexing.