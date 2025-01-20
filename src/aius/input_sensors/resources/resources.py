import platform
import sys

try:
    import psutil
except ImportError:
    print("psutil module not found. Memory and CPU info will not be available.")
    psutil = None

try:
    import pyopencl as cl
except ImportError:
    print("pyopencl module not found. GPU info will not be available.")
    cl = None

try:
    import concurrent.futures
except ImportError:
    print("concurrent.futures module not found. Thread pool info will not be available.")
    concurrent = None

class SystemResources:
    def __init__(self, psutil=psutil, cl=cl, concurrent=concurrent):
        self._memory_info = None
        self._cpu_info = None
        self._gpu_info = None
        self._thread_pool_info = None
        self._psutil = psutil
        self._cl = cl
        self._concurrent = concurrent
        self._platform = platform

    @property
    def memory_info(self):
        if self._memory_info is None and self._psutil is not None:
            self._memory_info = {
                "total": self._psutil.virtual_memory().total,
                "available": self._psutil.virtual_memory().available,
                "used": self._psutil.virtual_memory().used,
                "percentage": self._psutil.virtual_memory().percent,
            }
        return self._memory_info

    @property
    def cpu_info(self):
        if self._cpu_info is None and self._psutil is not None:
            self._cpu_info = {
                "physical_cores": self._psutil.cpu_count(logical=False),
                "logical_cores": self._psutil.cpu_count(logical=True),
                "current_frequency": self._psutil.cpu_freq().current,
                "max_frequency": self._psutil.cpu_freq().max,
                "min_frequency": self._psutil.cpu_freq().min,
                "usage": self._psutil.cpu_percent(),
            }
        return self._cpu_info

    @property
    def gpu_info(self):
        if self._gpu_info is None and self._cl is not None:
            self._gpu_info = []
            try:
                devices = self._cl.get_platforms()[0].get_devices()
                for device in devices:
                    self._gpu_info.append({
                        "name": device.name,
                        "type": self._cl.device_type.to_string(device.type),
                        "global_memory": device.global_mem_size,
                    })
            except Exception as e:
                print(f"Failed to get GPU info: {e}")
        return self._gpu_info

    @property
    def thread_pool_info(self):
        if self._thread_pool_info is None and self._concurrent is not None:
            self._thread_pool_info = {
                "max_workers": 5,  # default max workers
            }
        return self._thread_pool_info

    def get_system_info(self):
        return {
            "platform": self._platform.system(),
            "release": self._platform.release(),
            "version": self._platform.version(),
            "processor": self._platform.processor(),
        }

    def get_resource_usage(self):
        return {
            "memory": self.memory_info,
            "cpu": self.cpu_info,
            "gpu": self.gpu_info,
            "thread_pool": self.thread_pool_info,
        }

if __name__ == "__main__":
    system_resources = SystemResources()
    system_info = system_resources.get_system_info()
    resource_usage = system_resources.get_resource_usage()

    print("System Info:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    print("\nResource Usage:")
    for resource, info in resource_usage.items():
        print(f"{resource.capitalize()}:")
        if info is not None:
            for key, value in info.items():
                if isinstance(value, list):
                    for i, item in enumerate(value):
                        print(f"  {key} {i+1}:")
                        for k, v in item.items():
                            print(f"    {k}: {v}")
                else:
                    print(f"  {key}: {value}")
        else:
            print(f"  {resource} info not available")