import simplemetrics

# Should use: https://docs.python.org/3/library/unittest.html

print("Testing simplemetrics.cpu() ...")
simplemetrics.cpu()
print("Testing simplemetrics.memory() ...")
simplemetrics.memory()
print("Testing simplemetrics.disks() ...")
simplemetrics.disks()
print("Testing simplemetrics.network() ...")
simplemetrics.network()
print("Testing simplemetrics.process() ...")
simplemetrics.process()

print("... done")