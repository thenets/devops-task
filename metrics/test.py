import psutil, statistics, json, os

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
    

