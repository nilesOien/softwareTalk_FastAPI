#!/usr/bin/env python

# Demonstrates how to grab H-Alpha URLs from the API set up
# in section 9 and download them in parallel.
# The server in section 9 must be running for this to work.
#
# Note that you can :
# uv run downloadClient.py --help
# to get command line help, since standard argument parsing is used.


from parfive import Downloader
import requests
import argparse

parser = argparse.ArgumentParser(description='Download H-Alpha data from URLs served out by the demo API. The demo API in section 9 must be running for this to work.')

parser.add_argument('--minTime', default='20251015000000', type=str, help='Minimum time (inclusive) in YYYYMMDDhhmmss format.')

parser.add_argument('--maxTime', default='20251015235959', type=str, help='Maximum time (inclusive) in YYYYMMDDhhmmss format.')

parser.add_argument('--siteCSV', default='L,C', type=str, help='Comma separated list of single character H-Alpha site codes to fetch.')

parser.add_argument('--outDir', default='./data', type=str, help='Output directory to download to, will be created if it does not exist.')

parser.add_argument('--verbose', action='store_true', help='Activate verbose messaging.')

args = parser.parse_args()

apiURL=f"http://127.0.0.1:8000/database-dict?minTime={args.minTime}&maxTime={args.maxTime}&siteCSV={args.siteCSV}"

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

# Sort so that we do the largest file first.
# Probably not a big difference but may be a bit better.
dictionaryList = sorted(dictionaryList, key=lambda x: x['size'], reverse=True)

# Create a Downloader object
dl = Downloader()

# Queue up the list of URLs.
for dictionary in dictionaryList :
    dl.enqueue_file(dictionary['url'], path=args.outDir)
    if args.verbose :
        s = dictionary['size']
        u = dictionary['url']
        print(f'Added {s} bytes from {u}')

# Start the download process
files = dl.download()

print('Download done')

quit()

