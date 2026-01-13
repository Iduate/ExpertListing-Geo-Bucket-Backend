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

### 2. Activate Virtual Environment
On Windows:
```
.venv\Scripts\Activate.ps1
```

Or if using Command Prompt:
```
.venv\Scripts\activate.bat
```

### 3. Database Setup
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

### 4. Run the API
```
uvicorn src.main:app --reload
```

### 5. API Endpoints
- `POST /api/properties` - Create property
- `GET /api/properties/search?location=...` - Search properties
- `GET /api/geo-buckets/stats` - Bucket stats

### 6. Run Tests
```
pytest
```
