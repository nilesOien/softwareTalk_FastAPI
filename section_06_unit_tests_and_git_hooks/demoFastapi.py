#!/usr/bin/env python

from fastapi import FastAPI

# New concept - import the BaseModel class from Pydantic
from pydantic import BaseModel


# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name":"demoApp",
        "description":"Fast API serving out a dictionary with Pydantic.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags",
        },
    },
    {
        "name":"static-dict-service",
        "description":"An end point that serves out a static dictionary that has been checked by Pydantic.",
    }
   ]

# Get an application object
demoApp = FastAPI(title="Fast API Example with Pydantic checking",
        summary="Serves out a static dictionary but check its format first",
        description="Introduction to Pydantic",
        contact={
          "name": "Niles Oien",
          "url": "https://nso.edu",
          "email": "noien@nso.edu",
        },
        version="1.0.0",
        openapi_tags=tags_metadata)

# Define a static dictionary
static_data = {
    "firstName": "Niles",
    "lastName": "Oien",
    "numPets" : 5,
    "usesPiApproximation" : 3.141,
    "likesAurorasTooMuch" : True,
    # The lines below are dictionary entries
    # that won't get sent out because they
    # fail the pydantic format check.
    # That's because things are now
    # in the dictionary that are not in the
    # responseClass defined below.
    "thisShouldNotBeHere": "NoItShouldNot",
    "mySecretPassword": "iDontWantThisServedOut"
}

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
    numPets: int
    usesPiApproximation: float
    likesAurorasTooMuch: bool


# Serve out the static dictionary as JSON, now with expected response.
@demoApp.get("/static-dict", tags=['static-dict-service'], response_model=responseClass)
async def get_static_dict():
    """
    Returns the static_data dictionary as a JSON response.
    """
    return static_data


