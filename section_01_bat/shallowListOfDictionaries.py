#!/usr/bin/env python

# Show shallow copies

import pprint

# Set up a list of dictionaries.
l=[] # Empty list

d={} 
d['integer'] = 3
d['float'] = 3.1415927
d['string'] = 'Niles Oien'
l.append(d)

# d={} Commented out the re-init of d to show shallow copy
d['integer'] = 1
d['float'] = 2.71828
d['string'] = 'Sedona Crouch'
l.append(d)

# d={}
d['integer'] = 2
d['float'] = 1.41
d['string'] = 'Mickey Mouse'
l.append(d)

# This prints the following :
# [{'float': 1.41, 'integer': 2, 'string': 'Mickey Mouse'},
#  {'float': 1.41, 'integer': 2, 'string': 'Mickey Mouse'},
#  {'float': 1.41, 'integer': 2, 'string': 'Mickey Mouse'}]
# That's right - the last element three times. Because when
# we do this :
# l.append(d)
# It's doing a *shallow* copy of dictionary d when it appends
# it to the end of list l, so we get the last dictionary
# three times, because d always points to the same object.


pprint.pprint(l)

quit()

