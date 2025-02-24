from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from apps.model import Base
from apps.model.db import (
    Users,
)

username = "postgres"
password = "d3XZdhqD"
port = "5432"
database_domain = "postgres"
database_name = "phantom"

def create_tables():
    db_url = f"postgresql://{username}:{password}@{database_domain}:{port}/{database_name}"
    engine = create_engine(db_url)

    Base.metadata.create_all(bind=engine, tables=[
        Users.__table__,
    ])

class Session:
    def __new__(cls, engine=None):
        # should be configurable for local and VM
        db_url = f"postgresql://{username}:{password}@{database_domain}:{port}/{database_name}"
        engine = create_engine(db_url)
        session_local = sessionmaker(autocommit=False, autoflush=False,
                                     bind=engine)
        session = session_local()
        return session

def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()
