# ExpertListing Geo-Bucket Backend

## Setup Instructions

### Prerequisites
- Python 3.9+
- PostgreSQL with PostGIS extension
- pip

### 1. Install Dependencies
```
pip install -r requirements.txt
```

### 2. Database Setup
- Create a PostgreSQL database (e.g., `expertlisting`)
- Enable PostGIS extension:
```
CREATE EXTENSION postgis;
```
- Run migrations:
```
alembic upgrade head
```
- Seed the database:
```
psql -U <user> -d expertlisting -f seed.sql
```

### 3. Run the API
```
uvicorn src.main:app --reload
```

### 4. API Endpoints
- `POST /api/properties` - Create property
- `GET /api/properties/search?location=...` - Search properties
- `GET /api/geo-buckets/stats` - Bucket stats

### 5. Run Tests
```
pytest
```
