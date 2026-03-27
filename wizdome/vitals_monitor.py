import random, time

class VitalsMonitor:
    def __init__(self, memory):
        self.memory = memory
        self.device_name = "Tablet"

    def run(self):
        while True:
            heart_rate = random.randint(80, 110)
            steps = random.randint(0, 20)
            motion = random.randint(0, 2)
            weight = random.uniform(0.2, 1.5)
            self.memory.log_vitals(heart_rate, steps, motion, weight)
            print(f"[Vitals] HR:{heart_rate} Steps:{steps} Motion:{motion} Bag:{weight:.2f}kg")
            time.sleep(10)
