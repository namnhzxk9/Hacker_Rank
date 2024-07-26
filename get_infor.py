import platform
import psutil
import cpuinfo
import GPUtil

def get_system_info():
    # Basic system information
    print("Basic System Information:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print()

    # Detailed CPU information
    cpu_info = cpuinfo.get_cpu_info()
    print("CPU Information:")
    print(f"CPU Brand: {cpu_info['brand_raw']}")
    print(f"CPU Arch: {cpu_info['arch']}")
    print(f"CPU Bits: {cpu_info['bits']}")
    print(f"CPU Count: {cpu_info['count']}")
    print(f"CPU Frequency: {psutil.cpu_freq().current} MHz")
    print()

    # Memory information
    memory = psutil.virtual_memory()
    print("Memory Information:")
    print(f"Total Memory: {memory.total / (1024 ** 3)} GB")
    print(f"Available Memory: {memory.available / (1024 ** 3)} GB")
    print(f"Used Memory: {memory.used / (1024 ** 3)} GB")
    print(f"Memory Percentage: {memory.percent}%")
    print()

    # Disk information
    disk = psutil.disk_usage('/')
    print("Disk Information:")
    print(f"Total Disk Space: {disk.total / (1024 ** 3)} GB")
    print(f"Used Disk Space: {disk.used / (1024 ** 3)} GB")
    print(f"Free Disk Space: {disk.free / (1024 ** 3)} GB")
    print(f"Disk Percentage: {disk.percent}%")
    print()

    # GPU information
    gpus = GPUtil.getGPUs()
    if gpus:
        print("GPU Information:")
        for gpu in gpus:
            print(f"GPU ID: {gpu.id}")
            print(f"GPU Name: {gpu.name}")
            print(f"GPU Load: {gpu.load * 100}%")
            print(f"GPU Memory Free: {gpu.memoryFree}MB")
            print(f"GPU Memory Used: {gpu.memoryUsed}MB")
            print(f"GPU Memory Total: {gpu.memoryTotal}MB")
            print(f"GPU Temperature: {gpu.temperature} °C")
            print(f"GPU UUID: {gpu.uuid}")
            print()
    else:
        print("No GPU found")

if __name__ == "__main__":
    get_system_info()