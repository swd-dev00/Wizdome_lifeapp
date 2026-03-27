import random, time

class DistressDetection:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        while True:
            if random.random() < 0.05:
                self.memory.log_alert("distress_detected")
                print("[DistressDetection] Distress detected! Alert sent.")
            time.sleep(10)
