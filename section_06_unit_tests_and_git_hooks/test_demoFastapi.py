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
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK

# The returned JSON should look like :
# {
#   "firstName": "Niles",
#   "lastName": "Oien",
#   "numPets": 5,
#   "usesPiApproximation": 3.141,
#   "likesAurorasTooMuch": true
# }

# Test that all the keys are present in the returned dictionary.
def test_allKeysPresent() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    keysToTest = [ 'firstName', 'lastName', 'numPets', 'usesPiApproximation', 'likesAurorasTooMuch' ]
    for keyToTest in keysToTest :
        assert keyToTest in dictionary

# Test that all the keys are of the correct type.
def test_keysCorrectType() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    assert type(dictionary['firstName']) is str
    assert type(dictionary['lastName']) is str
    assert type(dictionary['numPets']) is int
    assert type(dictionary['usesPiApproximation']) is float
    assert type(dictionary['likesAurorasTooMuch']) is bool

# Test the values returned (normally would not get down to this level)

# Test first name
def test_firstNameValue() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    assert dictionary['firstName'] == 'Niles'

# Test last name
def test_lastNameValue() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    assert dictionary['lastName'] == 'Oien'

# Test number of pets
def test_numPetsValue() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    assert dictionary['numPets'] == 5

# Test usesPiApproximation
def test_usesPiApproximationValue() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    assert dictionary['usesPiApproximation'] == 3.141

# Test likesAurorasTooMuch
# Note JSON "true" (lower case "t") becomes Python "True" (upper case T)
def test_likesAurorasTooMuchValue() :
    response=client.get("/static-dict")
    assert response.status_code == status.HTTP_200_OK
    dictionary = response.json()
    desiredValue = True
    assert dictionary['likesAurorasTooMuch'] == desiredValue


