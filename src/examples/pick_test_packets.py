'''
Created on Feb 8, 2012

@author: peymankazemian
'''
from examples.load_stanford_backbone import *
from config_parser.cisco_router_parser import ciscoRouter
from headerspace.hs import *
from headerspace.applications import *
from time import time, clock
end_ports = get_end_ports()
print len(end_ports)
ntf = load_stanford_backbone_ntf()
ttf = load_stanford_backbone_ttf()
(port_map,port_reverse_map) = load_stanford_backbone_port_to_id_map()
cs = ciscoRouter(1)
output_port_addition = cs.PORT_TYPE_MULTIPLIER * cs.OUTPUT_PORT_TYPE_CONST
all_rules_set = set()
for t in ntf.tf_list:
    for rule in t.rules:
        all_rules_set.add(rule["id"])
for rule in ttf.rules:
        all_rules_set.add(rule["id"])

init_sum = len(all_rules_set)
f = open('rules.txt','r')


counter = 0
for line in f:
    tokens = line.split(":")
    port = tokens[0]
    rules = tokens[1].split(",")
    include_rule = False
    for rule in rules:
        if rule != "\n" and rule in all_rules_set:
            include_rule = True
            all_rules_set.remove(rule)
    if (include_rule):
        print "test packet from %s"%port
        counter += 1
        
print "Total Test Packets: %d"%counter
print "total rule count: %d"%init_sum
print "Unexercised rules: %d"%len(all_rules_set)
            
            
            