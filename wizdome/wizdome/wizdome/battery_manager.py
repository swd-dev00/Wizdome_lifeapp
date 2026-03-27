import random, time

class BatteryManager:
    def __init__(self, memory):
        self.memory = memory
        self.devices = ["Tablet", "Fitbit1", "Fitbit2"]
        for device in self.devices:
            if device not in self.memory.get_latest()["battery_status"]:
                self.memory.update_battery(device, 100)

    def run(self):
        while True:
            for device in self.devices:
                level = self.memory.get_latest()["battery_status"].get(device, 100)
                level -= random.uniform(0.5, 1.5)
                if level < 20:
                    print(f"[Battery] {device} low: {level:.1f}% — triggering auto-switch")
                    self.memory.log_alert(f"{device}_low_battery")
                if random.random() < 0.3:
                    recharge = random.uniform(5, 15)
                    level = min(100, level + recharge)
                    print(f"[Battery] {device} recharged +{recharge:.1f}% -> {level:.1f}%")
                self.memory.update_battery(device, level)
            time.sleep(10)
