#!/usr/bin/env python

from fastapi import FastAPI

# New concept - import the BaseModel class from Pydantic

# Needed to use Pydantic on a list of dicts rather than just a dict.

# Deal with the environment file.
from dotenv import load_dotenv
import os

# Database imports.
from sqlalchemy import create_engine, text

# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name":"dumpWholeDBapp",
        "description":"Fast API serving out a list of dictionaries with Pydantic.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags",
        },
    },
    {
        "name":"get-whole-database",
        "description":"An end point that dumps the whole halpha database.",
    }
   ]

# Get an application object
dumpWholeDBapp = FastAPI(title="Fast API Example",
        summary="Serves out a database using SQL to talk to the database",
        description="Introduces a database",
        contact={
          "name": "Niles Oien",
          "url": "https://nso.edu",
          "email": "noien@nso.edu",
        },
        version="1.0.0",
        openapi_tags=tags_metadata)


# Serve out the static dictionary as JSON, now with expected response
# as a list of dicts.
@dumpWholeDBapp.get("/getWholeDatabase", tags=['get-whole-database'])
async def get_whole_database():
    """
    Returns a list of dictionaries from a small database as a JSON response.
    """
    # Connect to the database. Usually uses the .env file but
    # for this demo it's a DotEnv file. First, read the environment file.
    if not os.path.exists("../../database/halphaOct2025.db"):
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

    engine = create_engine(dbURL)

    with engine.connect() as connection:
        result = connection.execute(text("select url, datatime, day, hour, site, size from halpha order by datatime"))
        # Process the results into a list of dictionaries.
        outList=[]
        for row in result:
            d = { "url": row.url, "datatime": row.datatime, "day": row.day, "hour": row.hour, "site": row.site, "size": row.size }
            outList.append(d)

    # Return the list of dicts so it gets served out.
    return outList

