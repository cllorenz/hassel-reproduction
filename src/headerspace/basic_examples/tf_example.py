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
from headerspace.tf import *
from config_parser.helper import *

# Create a transfer function object for packet header of length 2 nibbles
tf = TF(2)
    
# Adding rules to the transfer function
tf.add_rewrite_rule(TF.create_standard_rule([1,2,3], "100100xx", [5], "00111111", "01111111","",[]))
tf.add_rewrite_rule(TF.create_standard_rule([1,2], "1001xxxx", [5], "00001111", "01101111","",[]))
tf.add_fwd_rule(TF.create_standard_rule([1,2], "000011xx", [5], "00111111", "00111111","",[]))
tf.add_fwd_rule(TF.create_standard_rule([2,4], "10xxxxxx", [5], None , None,"",[]))

print tf
 
# Apply a headerspace object to TF we expect this to match on rule 1,2,4
hs = headerspace(2)
hs.add_hs(hs_string_to_byte_array("100xxxxx"))
result = tf.T(hs,2)
print "Result is:\n---------"
for (h,p) in result:
        print "at port %s:\n%s"%(p,h)
        print "#"
        
# Computing Inverse Transfer function
print "\n--------\nINVERSE\n--------\n"
result = tf.T_inv(hs, 5)
print "Result is:\n---------"
for (h,p) in result:
    print "at port %s:\n%s"%(p,h)
    print "#"
 