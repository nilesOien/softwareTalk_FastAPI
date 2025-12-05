#!/usr/bin/env python

# Set up and show a dictionary

# We'll use pretty print to print it.
import pprint

# Set up an empty dictionary and add elements.
# A dictionary is like an array, but the index
# can be a string.
d={} 
d['integer'] = 3
d['float'] = 3.1415927
d['string'] = 'Niles Oien'

# This prints the following :
# {'float': 3.1415927, 'integer': 3, 'string': 'Niles Oien'}
# That format is known as Java Script Object Notation (JSON)
pprint.pprint(d)

quit()

