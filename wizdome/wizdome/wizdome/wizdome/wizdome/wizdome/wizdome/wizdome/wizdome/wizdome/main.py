from memory import Memory
from vitals_monitor import VitalsMonitor
from scheduler import Scheduler
from battery_manager import BatteryManager
from distress_detection import DistressDetection
from ai_companion import AICompanion
from alert_system import AlertSystem
import threading, time

memory = Memory()
vitals_monitor = VitalsMonitor(memory)
scheduler = Scheduler(memory)
battery_manager = BatteryManager(memory)
distress_detection = DistressDetection(memory)
ai_companion = AICompanion(memory)
alert_system = AlertSystem(memory)

modules = [vitals_monitor, scheduler, battery_manager, distress_detection, ai_companion, alert_system]

for module in modules:
    t = threading.Thread(target=module.run, daemon=True)
    t.start()

while True:
    time.sleep(1)
