'''
Created on Aug 14, 2011

@author: peymankazemian
'''
from headerspace.hs import byte_array_list_contained_in

class emulated_tf(object):
    
    def __init__(self,n_reapet):
        self.switch_id_mul = 100000
        self.port_type_mul = 10000
        self.output_port_const = 2
        self.tf_list = []
        self.num_repeat = n_reapet
        self.length = 0
        
    def set_switch_id_multiplier(self,m):
        self.switch_id_mul = m
        
    def append_tf(self,tf):
        self.tf_list.append(tf)
        self.length = tf.length
        
    def insert_tf_at(self,tf,pos):
        self.tf_list.insert(pos, tf)
        
    def remove_duplicates(self,input_hs_list):
        #print "Start Removing Duplicates - len: %d"%len(input_hs_list)
        hs_buckets = {}
        to_be_removed = []
        for input_index in range(len(input_hs_list)):
            (cur_hs,cur_ports) = input_hs_list[input_index]
            bucket_name = "%s_%s"%(cur_hs.applied_rule_ids[len(cur_hs.applied_rule_ids) - self.num_repeat + 1],cur_ports)
            if bucket_name not in hs_buckets.keys():
                hs_buckets[bucket_name] = [input_index]
            else:
                renew_bucket = []
                for i in hs_buckets[bucket_name]:
                    (prev_hs,prev_ports) = input_hs_list[i]
                    if byte_array_list_contained_in(prev_hs.hs_list,cur_hs.hs_list) and byte_array_list_contained_in(cur_hs.hs_diff,prev_hs.hs_diff):
                        to_be_removed.append(i)
                    else:
                        renew_bucket.append(i)
                renew_bucket.append(input_index)
                hs_buckets[bucket_name] = renew_bucket
                
        to_be_removed.sort(cmp=None, key=None, reverse=True)
        for i in to_be_removed:
            input_hs_list.pop(i)
        #print "Start Removing Duplicates - len: %d"%len(input_hs_list)
                
        
    def T(self,hs,port):
        sw_id = port / self.switch_id_mul - 1
        if sw_id >= len(self.tf_list):
            return []
        tf = self.tf_list[sw_id]
        phase = [(hs,[port])]
        for i in range(0,self.num_repeat):
            tmp = []
            prt = 0
            for (hs,port_list) in phase:
                prt += len(port_list)
                for p in port_list:
                    tmp.extend(tf.T(hs,p))
            phase = tmp

        result = []
        for (h,ports) in phase:
            if port + self.output_port_const * self.port_type_mul in ports:
                ports.remove(port + self.output_port_const * self.port_type_mul)
            if (len(ports)>0):
                result.append((h,ports))
        self.remove_duplicates(result)
        return result 
    
    def T_inv(self,hs,port):
        sw_id = port / self.switch_id_mul - 1
        if sw_id >= len(self.tf_list):
            return []
        tf = self.tf_list[sw_id]
        phase = [(hs,[port])]
        for i in range(0,self.num_repeat):
            tmp = []
            for (hs,port_list) in phase:
                for p in port_list:
                    tmp.extend(tf.T_inv(hs,p))
            phase = tmp
        return phase
    def sp(self):
        tf = self.tf_list[10]
        print "####################"
        print tf
        print "####################"
        