#!/usr/bin/env python

from fastapi import FastAPI

# Set up tags that appear in the documentation pages that FastAPI generates.
tags_metadata = [
    {
        "name":"demoApp",
        "description":"An app that shows fast API serving out a dictionary.",
        "externalDocs": {
            "description": "How this documentation was added",
            "url": "https://fastapi.tiangolo.com/tutorial/metadata/#use-your-tags",
        },
    },
    {
        "name":"static-dict-service",
        "description":"An end point that serves out a static dictionary.",
    }
   ]



# Get an application object
demoApp = FastAPI(title="Fast API Example",
        summary="Very simple instance of FastAPI that just serves out a static dictionary",
        description="May be useful as an introduction to Fast API",
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
    "likesAurorasTooMuch" : True
}

# Serve out the static dictionary as JSON.
# The "@" operator below is a python decorator.
# You can think of a decorator as a sort of wrapper.
# In this case we are "decorating" the get function.
# All we do is return the dictionary, the business of
# serving that out as JSON (really, the heavy lifting)
# is handled by the underlying get function.
#
# So, with the uvicorn server running with the
# settings in startServer.sh, if you go to :
# http://127.0.0.1:8000/static-dict
# Then you get the JSON representation of the dict :
# {
#   "firstName": "Niles",
#   "lastName": "Oien",
#   "numPets": 5,
#   "usesPiApproximation": 3.141,
#   "likesAurorasTooMuch": true
# }
# 
# And you also get documentation (and a chance to try the interface) at :
# http://127.0.0.1:8000/docs (this documentation sometimes known as "swagger")
# And more docs at :
# http://127.0.0.1:8000/redoc
#
# Note that the docs can't say much about what gets delivered, beyond
# that you'll get a string.
# Anyway, here is the decorated function :
@demoApp.get("/static-dict", tags=['static-dict-service'])
async def get_static_dict():
    """
    Returns the static_data dictionary as a JSON response.
    """
    return static_data


