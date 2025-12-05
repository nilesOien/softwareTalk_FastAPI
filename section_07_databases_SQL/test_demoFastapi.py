#!/usr/bin/env python

# A series of tests to run with pytest.
# Tests the JSON delivered by FastAPI endpoints.
#
# pytest looks for any file named test_* and runs
# functions named test_* in those files.
#
# The file __init__.py has to be present for this
# to work (so that the directory is treated as a package).
#
# To see this run the linux command is :
# $ uv run pytest -v

from fastapi.testclient import TestClient
from fastapi import status

# Import the app from 
from .demoFastapi import demoApp

client=TestClient(demoApp)

# Test if we get good HTTP status (status 200) when we ask for the JSON
def test_getGoodStatus():
    response=client.get("/database-dict")
    assert response.status_code == status.HTTP_200_OK

# The returned JSON should look like :
# [
#  {
#     "firstName": "Niles",
#     "lastName": "Oien",
#     "numBikes": 3,
#     "usesPiApproximation": 3.141,
#     "likesAurorasTooMuch": 1
#   },
#   {
#     "firstName": "Noah",
#     "lastName": "Oien",
#     "numBikes": 1,
#     "usesPiApproximation": 3.1415927,
#     "likesAurorasTooMuch": 0
#   }
#  ]

# Test that all the keys are present in all the dictionaries in the returned list.
def test_allKeysPresent() :
    response=client.get("/database-dict")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)
    keysToTest = [ 'firstName', 'lastName', 'numBikes', 'usesPiApproximation', 'likesAurorasTooMuch' ]

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        for keyToTest in keysToTest :
            assert keyToTest in dictionary

# Test the types in the list of returned dictionaries.
def test_dictionariesTypes() :
    response=client.get("/database-dict")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert type(dictionary['firstName']) is str
        assert type(dictionary['lastName']) is str
        assert type(dictionary['numBikes']) is int
        assert type(dictionary['usesPiApproximation']) is float
        assert type(dictionary['likesAurorasTooMuch']) is int

