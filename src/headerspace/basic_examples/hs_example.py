'''
    Copyright (C) 2012 Stanford University

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
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