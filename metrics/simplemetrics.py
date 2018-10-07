# -*- coding: utf-8 -*-

""" Simple Metrics

Returns basic information about the system:
- RAM
- CPU
- Network
- Disk usage
- Processes running
"""


import psutil, statistics


def hello ():
    return "coffee"

def cpu ():
    cpu = {}
    cpu['per_cpu'] = psutil.cpu_percent(interval=1, percpu=True)
    cpu['total'] = statistics.median(cpu['per_cpu'])
    return cpu

def memory ():
    memory = {}
    memory['virtual'] = psutil.virtual_memory()._asdict()
    memory['swap'] = psutil.swap_memory()._asdict()
    return memory

def disks ():
    disks = {}
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if "tmpfs" in partition.device:
            continue
        disks[partition.device] = {
            'device' : partition.device,
            'usage' : psutil.disk_usage(partition.mountpoint)._asdict()
        }
    return disks



def network ():
    from multiprocessing import Pool
    p = Pool(processes=20)
    data = p.map(getNetworkStats, [1])
    p.close()
    network = data[0]
    return network

def getNetworkStats (nothing):
    network = {}
    network['interfaces'] = psutil.net_io_counters(pernic=True)
    for key, value in network['interfaces'].items():
        network['interfaces'][key] = value._asdict()
    # network['connections'] = []
    # for connection in psutil.net_connections():
    #     network['connections'].append(connection._asdict())
    #print("sonho")
    import json
    return json.loads(json.dumps(network))



def process ():

    import os, re

    process_list = {}
    proc_host_dir = '/proc_host'
    for i in os.listdir(proc_host_dir):
        process_path = os.path.join(proc_host_dir,i)
        if os.path.isdir(process_path) and i.isdigit():
            process_list[i] = {}
            process_list[i]['cmdline'] = open(os.path.join(process_path, "cmdline"), 'r').read().replace("\x00", " ")

            uid_map = open(os.path.join(process_path, "uid_map"), 'r').read().replace("\n","")
            uid_map = re.sub(' +', ' ', uid_map.replace(" +", " ")).split(" ")
            process_list[i]['user_id'] = uid_map[1]
            process_list[i]['group_id'] = uid_map[2]
            
            process_list[i]['pid'] = i
    
    return process_list