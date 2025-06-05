from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



# POSTGRES IMPLEMENTATION, TESETED AND WORKING
'''from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace with your actual values
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "123456aa"
POSTGRES_DB = "TodoApplicaionDatabase"
POSTGRES_HOST = "localhost"  # or IP address
POSTGRES_PORT = "5432"  # default port
POSTGRES_SCHEMA = "todos_schema"

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create schema-aware metadata
metadata = MetaData(schema=POSTGRES_SCHEMA)

# Set schema-aware Base
Base = declarative_base(metadata=metadata)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)'''

