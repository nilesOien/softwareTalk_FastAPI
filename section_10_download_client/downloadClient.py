#!/usr/bin/env python

# Demonstrates how to grab H-Alpha URLs from the API set up
# in section 9 and download them.
# The server in section 9 must be running for this to work.
#
# Note that you can :
# uv run downloadClient.py --help
# to get command line help, since standard argument parsing is used.


import os
from urllib.parse import urlsplit
import requests
import argparse

parser = argparse.ArgumentParser(description='Download H-Alpha data from URLs served out by the demo API. The demo API in section 9 must be running for this to work.')

parser.add_argument('--minTime', default='20251015000000', type=str, help='Minimum time (inclusive) in YYYYMMDDhhmmss format.')

parser.add_argument('--maxTime', default='20251015235959', type=str, help='Maximum time (inclusive) in YYYYMMDDhhmmss format.')

parser.add_argument('--siteCSV', default='L,C', type=str, help='Comma separated list of single character H-Alpha site codes to fetch.')

parser.add_argument('--outDir', default='./data', type=str, help='Output directory to download to, will be created if it does not exist.')

parser.add_argument('--verbose', action='store_true', help='Activate verbose messaging.')

args = parser.parse_args()

apiURL=f"http://127.0.0.1:8009/database-dict?minTime={args.minTime}&maxTime={args.maxTime}&siteCSV={args.siteCSV}"

print(f"Using API at {apiURL}")

# Get the list of dictionaries.
try:
    response = requests.get(apiURL)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    dictionaryList = response.json()  # Parses JSON into  Python list of dicts
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    quit()

print(f"Received info for {len(dictionaryList)} data files")

# Create the target directory
os.makedirs(args.outDir, exist_ok=True)

count=0
for dictionary in dictionaryList :
    count += 1
    url=dictionary['url']
    if args.verbose :
        print(f"Downloading {dictionary['size']} bytes from {dictionary['url']}")
        print(f"(file {count} of {len(dictionaryList)})")

    path=urlsplit(url).path
    fn=os.path.basename(path) # Filename from URL
    outFile= args.outDir + '/' + fn

    response = requests.get(url)
    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    with open(outFile, 'wb') as file:
        file.write(response.content)

    if args.verbose :
        s = dictionary['size']
        u = dictionary['url']
        print(f'Downloaded to {outFile}')
        print('')

print('Download done')

quit()

