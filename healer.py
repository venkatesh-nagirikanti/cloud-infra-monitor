import os
from logger import log

def restart_service(service):
    log(f"Restarting service: {service}")
    
    # simulate restart
    os.system(f"echo Restart command issued for {service}")
