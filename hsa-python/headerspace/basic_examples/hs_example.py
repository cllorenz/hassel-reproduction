'''
    Copyright 2012, Stanford University. This file is licensed under GPL v2 plus
    a special exception, as described in included LICENSE_EXCEPTION.txt.
    
Created on Jun 7, 2012

@author: Peyman Kazemian
'''

from headerspace.hs import *
from headerspace.wildcard_dictionary import *

# Creating a header space object of length 8 bits (2 nibbles)
hs = headerspace(2)

# Adding some wildcard expressions to the headerspace object
hs.add_hs(hs_string_to_byte_array("101xxxxx"))
hs.add_hs(hs_string_to_byte_array("0010xxxx"))
print "original HS is\n",hs,"\n---------"

# Removing some wildcard expressions from the headerspace object
hs.diff_hs(hs_string_to_byte_array("1010011x"))
hs.diff_hs(hs_string_to_byte_array("1010xxx0"))
print "New HS is\n",hs,"\n---------"

# Intersecting this headerspace with some wildcard expression
hs.intersect(hs_string_to_byte_array("10100xxx"))
print "After intersection HS is\n",hs,"\n---------"

# Forcing the subtraction to be computed
hs.self_diff()
print "Calculating the difference:\n",hs,"\n---------"