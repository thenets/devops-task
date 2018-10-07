# -*- coding: utf-8 -*-

""" Simple Metrics

Returns basic information about the system:
- RAM
- CPU
- Network
- Disk usage
- Processes running
"""

import psutil, statistics, os

class bcolors:
    """Color helper for console output"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def hello ():
    return "coffee"

def hasRequirements():
    success = True

    if not os.path.isdir("/sys_host"):
        success = False
        print(bcolors.FAIL + "ERROR: Volume '/sys_host' doesn't exist!" + bcolors.ENDC)
        
    if not os.path.isdir("/proc_host"):
        success = False
        print(bcolors.FAIL + "ERROR: Volume '/proc_host' doesn't exist!" + bcolors.ENDC)

    if not success:
        print(bcolors.FAIL + "Check the documentation to fix it." + bcolors.ENDC)

    return success

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
    net_interfaces_dir = '/sys_host/class/net/'

    interfaces = {}

    # For each network interface
    for net_interface_name in os.listdir(net_interfaces_dir):
        net_interface_dir = os.path.join(net_interfaces_dir, net_interface_name)

        if not os.path.isdir(net_interface_dir):
            continue

        statistics = {}

        # For each statistic
        statistics_dir = os.path.join(net_interface_dir, "statistics")
        for statistic_name in os.listdir(statistics_dir):
            statistics[statistic_name] = open(os.path.join(statistics_dir, statistic_name), 'r').read().replace("\n",'')

        interfaces[net_interface_name] = statistics
    
    return interfaces
        



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