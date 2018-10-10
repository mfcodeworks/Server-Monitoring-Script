import socket, time, json, datetime, platform, psutil, requests

def main():
    # Hostname Info
    hostname = socket.gethostname()
    print("Hostname:", hostname)

    # CPU Info
    cpu_count = psutil.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)
    print("CPU:")
    print("Count:", cpu_count, "Usage:", cpu_usage)

    # Memory Info
    memory_stats = psutil.virtual_memory()
    memory_total = memory_stats.total
    memory_used = memory_stats.used
    memory_used_percent = memory_stats.percent
    print("Memory:")
    print("Percent:", memory_used_percent, "\tTotal:", memory_total / 1e+6, "MB", "\tUsed:", memory_used / 1e+6, "MB")

    # Disk Info
    disk_info = psutil.disk_partitions()
    print("Disks:")
    disks = []
    for x in disk_info:
        disk = {
            "name" : x.device, 
            "mount_point" : x.mountpoint, 
            "type" : x.fstype, 
            "total_size" : psutil.disk_usage(x.mountpoint).total, 
            "used_size" : psutil.disk_usage(x.mountpoint).used, 
            "percent_used" : psutil.disk_usage(x.mountpoint).percent
        }

        disks.append(disk)

        print("Disk name",disk["name"], "\tMount Point:", disk["mount_point"], "\tType",disk["type"], "\tSize:", disk["total_size"] / 1e+9,"\tUsage:", disk["used_size"] / 1e+9, "\tPercent Used:", disk["percent_used"])

    # Network Info 
    print("Network:")
    network_stats = get_bandwidth()
    print("Traffic in:",network_stats["traffic_in"] / 1e+6,"\tTraffic out:",network_stats["traffic_out"] / 1e+6)

    # Platform Info
    print("OS:")
    system = {
        "name" : platform.system(),
        "version" : platform.release()
    }
    print(system["name"],system["version"])

    # Time Info
    timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    ## Set Machine Info
    machine = {
    	"hostname" : hostname,
        "system" : system,
    	"cpu_count" : cpu_count,
    	"cpu_usage" : cpu_usage,
    	"memory_total" : memory_total,
    	"memory_used" : memory_used,
    	"memory_used_percent" : memory_used_percent,
    	"drives" : disks,
    	"network_up" : network_stats["traffic_out"],
    	"network_down" : network_stats["traffic_in"],
        "timestamp" : timestamp
    }

    data = json.dumps(machine)
    print("\nData:")
    print(data)

    post_data(data)

def get_bandwidth():
    # Get net in/out
    net1_out = psutil.net_io_counters().bytes_sent
    net1_in = psutil.net_io_counters().bytes_recv

    time.sleep(1)

    # Get new net in/out
    net2_out = psutil.net_io_counters().bytes_sent
    net2_in = psutil.net_io_counters().bytes_recv

    # Compare and get current speed
    if net1_in > net2_in:
        current_in = 0
    else:
        current_in = net2_in - net1_in
    
    if net1_out > net2_out:
        current_out = 0
    else:
        current_out = net2_out - net1_out
    
    network = {"traffic_in" : current_in, "traffic_out" : current_out}
    return network

def post_data(data):
    try:
        endpoint = "http://monitor.localhost.local/api/"
        response = requests.get(url = endpoint, params = {"data" : data})
        print("\nGET:")
        print("Response:", response.status_code)
        print("Headers:", response.headers)
        print("Content:\n", response.json())
    except requests.exceptions.RequestException as e:
        print("\nGET Error:\n",e)

while True:
    main()
    print("-----------------------------------------------------------------")
    time.sleep(3)