import time, random

class AICompanion:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        while True:
            vitals = self.memory.get_latest()["vitals"]
            if vitals:
                last_hr = vitals[-1]["heart_rate"]
                if last_hr > 105:
                    print(f"[AICompanion] Hey Wisdom, your heart rate is high ({last_hr} bpm). Take it easy!")
            if random.random() < 0.1:
                print("[AICompanion] Keep up the great work, Wisdom! You’re doing amazing!")
            time.sleep(15)
