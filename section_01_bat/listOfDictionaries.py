#!/usr/bin/env python

# Set up and show a list of dictionaries

# We'll use pretty print to print it.
import pprint

# Set up a list of dictionaries.
l=[] # Empty list (square brackets)

d={} # Empty dictionary (curly brackets)
d['integer'] = 3
d['float'] = 3.1415927
d['string'] = 'Niles Oien'
l.append(d)

d={}
d['integer'] = 1
d['float'] = 2.71828
d['string'] = 'Sedona Crouch'
l.append(d)

d={}
d['integer'] = 2
d['float'] = 1.41
d['string'] = 'Mickey Mouse'
l.append(d)

# This prints the following :
# [{'float': 3.1415927, 'integer': 3, 'string': 'Niles Oien'},
#  {'float': 2.71828,   'integer': 1, 'string': 'Sedona Crouch'},
#  {'float': 1.41,      'integer': 2, 'string': 'Mickey Mouse'}]
pprint.pprint(l)

quit()

