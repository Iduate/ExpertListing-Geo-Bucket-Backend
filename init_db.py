#!/usr/bin/env python
"""Initialize the database by creating all tables."""

import sys
import os

# Add the workspace root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.models import Base
from src.database import engine

try:
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created successfully!")
    
    # Verify tables exist
    inspector_from_sqlalchemy = __import__('sqlalchemy').inspect
    inspector = inspector_from_sqlalchemy(engine)
    tables = inspector.get_table_names()
    print(f"✓ Tables in database: {tables}")
    
except Exception as e:
    print(f"✗ Error creating tables: {e}")
    import traceback
    traceback.print_exc()
