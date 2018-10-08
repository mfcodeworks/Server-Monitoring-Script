import socket, psutil

# Hostname Info
hostname = socket.gethostname()
print("Hostname", hostname)

# CPU Info
cpu_count = psutil.cpu_count()
cpu_usage = psutil.cpu_percent(interval=1)
print("CPU:")
print("Count", cpu_count, "Usage", cpu_usage)
memory_stats = psutil.virtual_memory()

# Memory Info
memory_total = memory_stats.total/1e+6
memory_used = memory_stats.used/1e+6
memory_used_percent = memory_stats.percent
print("Memory:")
print("Percent:", memory_used_percent, "\tTotal:", "%.2f" % memory_total, "MB", "\tUsed:", "%.2f" % memory_used, "MB")

# Disk Info
disk_info = psutil.disk_partitions()
print("Disks:")
for disk in disk_info:
    print("Disk name",disk.device,"\tMount Point:",disk.mountpoint,"\tType",disk.fstype,"\tSize:",psutil.disk_usage(disk.mountpoint).total,"\tUsage:",psutil.disk_usage(disk.mountpoint))