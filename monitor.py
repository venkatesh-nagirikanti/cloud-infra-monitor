import psutil
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, DISK_THRESHOLD, SERVICES_TO_MONITOR
from logger import log
from healer import restart_service


def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    log(f"CPU Usage: {cpu}%")

    if cpu > CPU_THRESHOLD:
        log("High CPU detected!")


def check_memory():
    memory = psutil.virtual_memory().percent
    log(f"Memory Usage: {memory}%")

    if memory > MEMORY_THRESHOLD:
        log("High Memory detected!")


def check_disk():
    disk = psutil.disk_usage('/').percent
    log(f"Disk Usage: {disk}%")

    if disk > DISK_THRESHOLD:
        log("High Disk usage detected!")


def check_services():
    running = [p.name() for p in psutil.process_iter()]

    for service in SERVICES_TO_MONITOR:
        if service not in running:
            log(f"{service} is DOWN")
            restart_service(service)
        else:
            log(f"{service} is running")


if __name__ == "__main__":
    log("Starting Cloud Infrastructure Monitor")

    check_cpu()
    check_memory()
    check_disk()
    check_services()

    log("Monitoring complete")
