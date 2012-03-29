'''
Created on Feb 6, 2012

@author: peymankazemian
'''
from examples.load_stanford_backbone import *
from config_parser.cisco_router_parser import ciscoRouter
from headerspace.hs import *
from headerspace.applications import *
from time import time, clock

ntf = load_stanford_backbone_ntf()
ttf = load_stanford_backbone_ttf()
(port_map,port_reverse_map) = load_stanford_backbone_port_to_id_map()
cs = ciscoRouter(1)
output_port_addition = cs.PORT_TYPE_MULTIPLIER * cs.OUTPUT_PORT_TYPE_CONST

#all_rules_set = set()
#for t in ntf.tf_list:
#    for rule in t.rules:
#        all_rules_set.add(rule["id"])

end_ports = get_end_ports()

all_x = byte_array_get_all_x(ntf.length)
test_pkt = headerspace(ntf.length)
test_pkt.add_hs(all_x)

f = open("rules.txt", 'w')
exercised_rules = set()
for end_port in end_ports:
    st = time()
    paths = find_reachability(ntf,ttf,end_port-output_port_addition,end_ports,test_pkt)
    en = time()
    for p_node in paths:
        f.write("%s:"%end_port)
        for (r,rule_id,port) in p_node["hdr"].applied_rule_ids:
            f.write("%s,"%rule_id)
        f.write("\n")
    print"found %d paths from: %s in %d seconds"%(len(paths),end_port,en-st)

f.close()

