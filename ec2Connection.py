import boto
from pprint import pprint
from boto import ec2
import sys

#instance_id = sys.argv[1]


region = 'eu-west-1'
ec2 = boto.ec2.connect_to_region(region)

# instance = ec2.get_instance_attribute(instance_id='i-1bc89491', attribute='interfaces')
# print instance


instances = ec2.get_only_instances(['i-534d7bd9'])
if not instances or len(instances) == 0:
    sys.exit(1)


# nic_id_1 = i[0].interfaces[1].id
# nic_id_2 = i[0].interfaces[0].id
# print nic_id_1
# print nic_id_2


# x = ec2.get_all_network_interfaces(filters={'network-interface-id': nic_id})
# print x


# reservations = ec2.get_all_instances()
# instances = [i for r in reservations for i in r.instances]
# for i in instances:
#     if i.id == 'i-1bc89491':
#        pprint(i.__dict__)
#        myInstance = i
#        break

#interfaces = ec2.get_all_network_interfaces()

# instances = [i for r in reservations for i in r.instances]
# for i in instances:
#     pprint(i.__dict__)
#     break # remove this to list all instances

# for i in interfaces:
#     #print(i)
#     iface = str(i).split(':')
#     print iface[1]

#                 pprint(i.__dict__)
#    break # remove this to list all instances

