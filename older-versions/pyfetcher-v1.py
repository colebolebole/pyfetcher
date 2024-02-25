import os
import psutil
import platform
import cpuinfo

def get_os_info():
    os_name = os.name
    if os_name == 'nt':
        os_name = platform.system()
    return os_name

def get_cpu_info():
    info = cpuinfo.get_cpu_info()
    cpu_model = info['brand_raw']
    cpu_count = psutil.cpu_count(logical=False)
    return f'{cpu_model} ({cpu_count} cores)'

def get_memory_info():
    total_memory = psutil.virtual_memory().total / (1024 ** 3) # in GiB
    return f'{total_memory:.2f} GiB'

def get_disk_info():
    partitions = psutil.disk_partitions()
    disks = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total_space = usage.total / (1024 ** 3) # in GiB
        disks.append(f'{partition.device} ({total_space:.2f} GiB)')
    return ', '.join(disks)

if __name__ == "__main__":
    print("OS:", get_os_info())
    print("CPU:", get_cpu_info())
    print("Memory:", get_memory_info())
    print("Disks:", get_disk_info())
