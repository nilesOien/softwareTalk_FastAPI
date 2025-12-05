#!/usr/bin/env python

from fastapi import FastAPI, HTTPException, Query

# New concept - import the BaseModel class from Pydantic
from pydantic import BaseModel

# Needed to use Pydantic on a list of dicts rather than just a dict.
from typing import List

# Deal with the environment file.
from dotenv import load_dotenv
import os

# Database imports.
from sqlalchemy import create_engine, Column, String, CHAR, Integer, or_, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Add middleware so I can run everything on localhost.
# The web client needs this. Only do this for demo - not production.
from fastapi.middleware.cors import CORSMiddleware

# Set up origins.
origins = ["*"]

# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name":"demoApp",
        "description":"Fast API serving out a list of dictionaries with Pydantic.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags"
        },
    },
    {
        "name":"database-dict-service",
        "description":"An end point that serves out a list of dictionaries pointing to H-Alpha data. minTime and maxTime are in YYYYMMDDhhmmss format, siteCSV is a comma separated list of site codes. Setting minTime=20251015000000, maxTime=20251015235959, siteCSV=L,C would retrieve data for October 15 2025 for the sites Learmonth and Cerro Tololo. An upper limit of 5 (for example) on the number of dictionaries to be returned can be set with limitNum=5"
    },
    {
        "name":"database-summary-service",
        "description":"An end point that serves out a database summary. By default the summary is daily, if binBy is set to \"hour\" then it is hourly."
    }
   ]

# Get an application object
demoApp = FastAPI(title="Fast API Example",
        summary="Serves out a database using an ORM to talk to the database",
        description="Introduces a real database",
        contact={
          "name": "Niles Oien",
          "url": "https://nso.edu",
          "email": "noien@nso.edu",
        },
        version="1.0.0",
        openapi_tags=tags_metadata)

# Add middleware to allow all origins. Again, only do this for demo!
demoApp.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_methods=["*"],
        allow_headers=["*"])

# The table we're trying to connect to is :
# CREATE TABLE IF NOT EXISTS halpha (
#    url      TEXT NOT NULL,
#    datatime TEXT NOT NULL,
#    day      TEXT NOT NULL,
#    hour     TEXT NOT NULL,
#    site     CHAR NOT NULL,
#    size     INT  NOT NULL
# );
#
# Create a class that models that table. Must have at least one primary key.
Base = declarative_base()
class tableModel(Base):
    __tablename__ = "halpha"
    url=      Column('url',      String, primary_key=True)
    datatime= Column('datatime', String)
    day=      Column('day',      String)
    hour=     Column('hour',     String)
    site=     Column('site',     CHAR(1))
    size=     Column('size',     Integer)


# This end point serves out the url and size as JSON
# as a list of dicts.
# Takes the following arguments :
#  minTime : Minimum time, string, YYYYMMDDhhmmss format, inclusive.
#  maxTime : Maximum time, same format.
#  siteCSV : Comma separated list of sites. Setting siteCSV="L,C"
#            means get data for sites "L" (Learmonth, Australia)
#            and "C" (Cerro Tololo, Chile).
# Returns JSON in this format :
# [
#  {
#    "url": "https://gong2.nso.edu/HA/haf/202510/20251015/20251015092702Uh.fits.fz",
#    "size": 2977920
#  },
#  {
#    "url": "https://gong2.nso.edu/HA/haf/202510/20251015/20251015092742Lh.fits.fz",
#    "size": 3003840
#  }
# ]

# Define a class that has the general format of the JSON response.
# This is a pydantic class (inherits from "BaseModel" class) that is
# used for verification.
class responseClass(BaseModel) :
    # This triple quoted comment winds up on the documentation page
    # for this schema.
    """
    Pydantic class that defines the format of what this endpoint delivers.
    """
    url:      str
    size:     int

@demoApp.get("/database-dict", response_model=List[responseClass], tags=['database-dict-service'])
async def get_halpha_urls(minTime:  str = Query(default=None),
                          maxTime:  str = Query(default=None),
                          siteCSV:  str = Query(default=None),
                          limitNum: int = Query(default=None)):
    """
    Returns a list of dictionaries applicable to H-Alpha data.
    """
    # Connect to the database. Usually uses the .env file but
    # for this demo it's a DotEnv file. First, read the environment file.
    if not os.path.exists("../database/halphaOct2025.db"):
        print("The database file was not found")
        quit()

    # Load the environment file. Usually the file is named
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

    # Connect to the database.
    engine = create_engine(dbURL)

    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # This query would get data from the two columns for the whole table.
    query = db.query(tableModel.url, tableModel.size)

    # If a minimum time was specified, filter on that.
    if minTime is not None :
        query = query.filter(tableModel.datatime >= minTime)

    # Ditto maximum time.
    if maxTime is not None :
        query = query.filter(tableModel.datatime <= maxTime)

    # If a list of sites was specified, apply filters on that.
    if siteCSV is not None :
        sites=siteCSV.split(',')
        # This is a bit tricky.
        # If the caller specified siteCSV="L,C"
        # then sites is now the list [ "L", "C" ].
        #
        # The * operator (the unpacking operator)
        # when used in a function call
        # takes an iterable (like a list or tuple) and
        # unpacks its elements as separate positional
        # arguments, so for example we can :
        # >>> x=[1,2,3]  # A list
        # >>> print(x)   #
        # [1, 2, 3]      # Printed the list
        # >>> print(*x)  #
        # 1 2 3          # Printed the list as positional parameters
        #
        # So we can pass the elements of a list
        # to the function as positional arguments
        # (in this case the or_()
        # function).
        #
        # So make the list of filters that we want to throw at or_() :
        site_filters = [tableModel.site == site for site in sites]
        # And then use the unpacking operator to throw them all at or_()
        # as positional arguments :
        query = query.filter(or_(*site_filters))
    

    # Specify the order to return results in.
    query = query.order_by(tableModel.datatime, tableModel.site)

    # Set an upper limit on the number of rows
    # from the database to return, if specified.
    # Have to do this limit() after the order_by()
    if limitNum is not None :
        query = query.limit(limitNum)

    # It's also possible to specify a limit on how many to return.
    # Useful when developing when you don't want to get clobbered
    # by the sheer mass of data, but commented out below :
    #
    # query = query.limit(300)

    # Do the query
    db_results = query.all()

    # Close the database, we're done with it.
    db.close()

    # Return the results, which are the list of dicts to be served out,
    # or throw a 404 if there was an issue.
    if db_results is None:
        raise HTTPException(status_code=404, detail="Problem getting data")

    return db_results




class summaryResponseClass(BaseModel) :
    """
    Pydantic class that defines the format of what this summary endpoint delivers.
    """
    timerange:  str
    num:        int

@demoApp.get("/database-summary", response_model=List[summaryResponseClass], tags=['database-summary-service'])
async def get_halpha_summary(minTime: str = Query(default=None), maxTime: str = Query(default=None), site: str = Query(default=None), binBy: str = Query(default='day')):
    """
    Returns a database summary.
    """
    # Connect to the database. Usually uses the .env file but
    # for this demo it's a DotEnv file. First, read the environment file.
    if not os.path.exists("../database/halphaOct2025.db"):
        print("The database file was not found")
        quit()

    # Load the environment file. Usually the file is named
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

    # Connect to the database.
    engine = create_engine(dbURL)

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    # See if we are binning by day or hour.
    groupByColumn = tableModel.day
    if binBy == 'hour' :
        groupByColumn = tableModel.hour

    query = db.query(groupByColumn.label("timerange"), func.count(tableModel.day).label("num"))

    # Filter by site, if requested.
    if site is not None :
        query = query.filter(tableModel.site == site)

    # If a minimum time was specified, filter on that.
    if minTime is not None :
        query = query.filter(tableModel.datatime >= minTime)

    # Ditto maximum time.
    if maxTime is not None :
        query = query.filter(tableModel.datatime <= maxTime)

    query = query.group_by(groupByColumn)

    query = query.order_by(groupByColumn)

    db_results = query.all()

    # Close the database, we're done with it.
    db.close()

    # Return the results, which are the list of dicts to be served out,
    # or throw a 404 if there was an issue.
    if db_results is None:
        raise HTTPException(status_code=404, detail="Problem getting data")

    # Because of the group_by() we don't get a list of dicts, reformat
    # so that it is in fact a list of dicts.
    list_of_dicts = [row._asdict() for row in db_results]

    return list_of_dicts




