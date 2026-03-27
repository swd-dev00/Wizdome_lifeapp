import time
from datetime import datetime, timedelta

class Scheduler:
    def __init__(self, memory):
        self.memory = memory
        self.last_bag_change = datetime.now()
        self.bag_interval = timedelta(hours=4)

    def run(self):
        while True:
            now = datetime.now()
            if now - self.last_bag_change > self.bag_interval:
                self.memory.log_alert("bag_change_due")
                print(f"[Scheduler] Bag change due! Time: {now.strftime('%H:%M:%S')}")
                self.last_bag_change = now
            time.sleep(10)
