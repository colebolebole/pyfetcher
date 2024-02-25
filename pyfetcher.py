import os
import platform
import psutil
import cpuinfo
from rich import print

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

def show_os_icon(os_name):
    if os_name.lower() == 'windows':
        return '🪟'
    elif os_name.lower() == 'linux':
        return '🐧'
    elif os_name.lower() == 'darwin':
        return ''
    else:
        return '🚫'

def main():
    os_name = get_os_info()
    os_icon = show_os_icon(os_name)
    print(f'OS: {os_icon} [bold cyan]{os_name}[/bold cyan]')
    print(f'CPU: [bold magenta]{get_cpu_info()}[/bold magenta]')
    print(f'Memory: [bold yellow]{get_memory_info()}[/bold yellow]')
    print(f'Disks: [bold green]{get_disk_info()}[/bold green]')

if __name__ == "__main__":
    main()
