from datetime import datetime

LOG_FILE = "system.log"

def log(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{time}] {message}"
    
    print(entry)

    with open(LOG_FILE, "a") as f:
        f.write(entry + "\n")
