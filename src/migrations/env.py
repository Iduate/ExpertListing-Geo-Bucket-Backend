from src.models import Base
from src.database import engine

# This is a simplified migration script for initial setup
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
