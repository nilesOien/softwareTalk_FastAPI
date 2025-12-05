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

############# TESTS OF END POINT THAT DELIVERS URLs ################

# Test if we get good HTTP status (status 200) when we ask for the JSON
def test_halpha_urls_get_good_status():
    response=client.get("/database-dict?minTime=20251015000000&maxTime=20251015010000&siteCSV=L,C,U")
    assert response.status_code == status.HTTP_200_OK

# The returned JSON should look like :
# [
#  {
#    "url": "https://gong2.nso.edu/HA/haf/202510/20251015/20251015000042Lh.fits.fz",
#    "datatime": "20251015000042",
#    "site": "L",
#    "size": 3015360
#  },
#  {
#    "url": "https://gong2.nso.edu/HA/haf/202510/20251015/20251015000142Lh.fits.fz",
#    "datatime": "20251015000142",
#    "site": "L",
#    "size": 2920320
#  }
# ]



# Test that all the keys are present in all the dictionaries in the returned list.
def test_halpha_urls_all_keys_present() :
    response=client.get("/database-dict?minTime=20251015000000&maxTime=20251015010000&siteCSV=L,C,U")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)
    keysToTest = [ 'url', 'size' ]

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        for keyToTest in keysToTest :
            assert keyToTest in dictionary

# Test the types in the list of returned dictionaries.
def test_halpha_urls_dictionaries_types() :
    response=client.get("/database-dict?minTime=20251015000000&maxTime=20251015010000&siteCSV=L,C,U")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert type(dictionary['url']) is str
        assert type(dictionary['size']) is int



############# TESTS OF END POINT THAT DELIVERS TEMPORAL SUMMARIES ################
#
# The returned JSON should look like this for daily summaries :
# [ {
#    "timerange": "20251015",
#    "num": 3290
#   },
#   {
#    "timerange": "20251016",
#    "num": 3331
#   } ]
#
# And like this for hourly summaries :
# [ {
#     "timerange": "2025101500",
#     "num": 60
#    },
#    {
#     "timerange": "2025101501",
#     "num": 60
#    },
#    {
#     "timerange": "2025101502",
#     "num": 72
#    } ]

def test_halpha_summaries_get_good_status_hourly():
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251015235959&site=L&binBy=hour")
    assert response.status_code == status.HTTP_200_OK

def test_halpha_summaries_get_good_status_daily():
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251020235959&site=L&binBy=day")
    assert response.status_code == status.HTTP_200_OK



# Test that all the keys are present in all the dictionaries in the returned list.
def test_halpha_summaries_all_keys_present_hourly() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251016235959&site=L&binBy=hour")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)
    keysToTest = [ 'timerange', 'num' ]

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        for keyToTest in keysToTest :
            assert keyToTest in dictionary

def test_halpha_summaries_all_keys_present_daily() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251020235959&site=L&binBy=day")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)
    keysToTest = [ 'timerange', 'num' ]

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        for keyToTest in keysToTest :
            assert keyToTest in dictionary

# Test of types in returned dictionaries.
def test_halpha_summaries_dictionaries_types_daily() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251016235959&site=L&binBy=day")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert type(dictionary['timerange']) is str
        assert type(dictionary['num']) is int


def test_halpha_summaries_dictionaries_types_hourly() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251016235959&site=L&binBy=hour")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert type(dictionary['timerange']) is str
        assert type(dictionary['num']) is int


# Rather specific tests on values.
def test_halpha_summaries_dictionaries_values_daily() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251016235959&site=L&binBy=day")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert len(dictionary['timerange']) == 8
        assert dictionary['num'] > 0


def test_halpha_summaries_dictionaries_values_hourly() :
    response=client.get("/database-summary?minTime=20251015000000&maxTime=20251016235959&site=L&binBy=hour")
    assert response.status_code == status.HTTP_200_OK
    returnedList = response.json()
    # Check that it is indeed a list
    assert isinstance(returnedList, list)

    for dictionary in returnedList :
        # Check that the items in the list are all dictionaries.
        assert isinstance(dictionary, dict)
        assert len(dictionary['timerange']) == 10
        assert dictionary['num'] > 0
        assert dictionary['num'] <= 60 # Given that a site was specified, we
                                       # can only have 60 per hour max.

