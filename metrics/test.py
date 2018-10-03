import psutil, statistics, json

cpu = {}
cpu['per_cpu'] = psutil.cpu_percent(interval=1, percpu=True)
cpu['total'] = statistics.median(cpu['per_cpu'])

print(json.dumps(cpu))