#!/usr/bin/env python

from fastapi import FastAPI

# New concept - import the BaseModel class from Pydantic
from pydantic import BaseModel

# Needed to use Pydantic on a list of dicts rather than just a dict.
from typing import List

# Deal with the environment file.
from dotenv import load_dotenv
import os

# Database imports.
from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name":"demoApp",
        "description":"Fast API serving out a list of dictionaries with Pydantic.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags",
        },
    },
    {
        "name":"database-dict-service",
        "description":"An end point that serves out a list of dictionaries from a small database using an object relational mapper (ORM).",
    }
   ]

# Get an application object
demoApp = FastAPI(title="Fast API Example",
        summary="Serves out a database using an ORM to talk to the database",
        description="Introduces a database",
        contact={
          "name": "Niles Oien",
          "url": "https://nso.edu",
          "email": "noien@nso.edu",
        },
        version="1.0.0",
        openapi_tags=tags_metadata)


# Define a class that has the general format of the expected response.
# This is a pydantic class (inherits from "BaseModel" class) that is
# used for verification.
class responseClass(BaseModel) :
    # This triple quoted comment winds up on the documentation page
    # for this schema.
    """
    Pydantic class that defines the format of what this endpoint delivers.
    """
    firstName: str
    lastName: str
    numBikes: int # Changed from numPets
    usesPiApproximation: float
    likesAurorasTooMuch: int # This used to be a bool but
                             # sqlite doesn't support bool
                             # so I made it an int.


# Serve out database table dictionary as JSON, now with expected response
# as a list of dicts.
@demoApp.get("/database-dict", response_model=List[responseClass], tags=['database-dict-service'])
async def get_database_dict():
    """
    Returns a list of dictionaries from a small database as a JSON response.
    """
    # Connect to the database. Usually uses the .env file but
    # for this demo it's a DotEnv file. First, read the environment file.
    if not os.path.exists("../database/little.db"):
        print("The database file was not found")
        quit()

    # Load the enviroment file. Usually the file is named
    # .env which is the default, and so it can be loaded with :
    # load_dotenv()
    # But because for this demo the environment file is DotEnv we use :
    # load_dotenv("DotEnv")
    load_dotenv("DotEnv")
    dbURL = os.getenv("DATABASE_URL")
    # Check that it went OK.
    if dbURL is None :
        print("DATABASE_URL not in environment file DotEnv")
        quit()

    # The table we're trying to connect to is :
    # CREATE TABLE IF NOT EXISTS small (
    #     firstName           TEXT NOT NULL,
    #     lastName            TEXT NOT NULL,
    #     numBikes            INT  NOT NULL,
    #     usesPiApproximation REAL NOT NULL,
    #     likesAurorasTooMuch INT  NOT NULL
    # );
    #
    # Create a class that models that table. Must have at least one primary key.
    Base = declarative_base()
    class tableModel(Base):
        __tablename__ = "small"
        firstName=          Column('firstName',           String, primary_key=True)
        lastName=           Column('lastName',            String, primary_key=True)
        numBikes=           Column('numBikes',            Integer)
        usesPiApproximation=Column('usesPiApproximation', Float)
        likesAurorasTooMuch=Column('likesAurorasTooMuch', Integer)

    # Connect to the database.
    engine = create_engine(dbURL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # Query is pretty simple - get the whole table.
    db_results = db.query(tableModel).all()

    db.close()

    # Return the results, which are the list of dicts to be served out.
    return db_results

