import json, os
from cryptography.fernet import Fernet
from datetime import datetime

KEY_FILE = "wizdome_key.key"
MEMORY_FILE = "wizdome_memory.json"

class Memory:
    def __init__(self):
        if not os.path.exists(KEY_FILE):
            self.key = Fernet.generate_key()
            with open(KEY_FILE, "wb") as f:
                f.write(self.key)
        else:
            with open(KEY_FILE, "rb") as f:
                self.key = f.read()
        self.cipher = Fernet(self.key)
        self.data = self._load_memory()

    def _load_memory(self):
        if not os.path.exists(MEMORY_FILE):
            return {
                "vitals": [],
                "schedule": [],
                "alerts": [],
                "ai_messages": [],
                "notifications": [],
                "battery_status": {}
            }
        else:
            with open(MEMORY_FILE, "rb") as f:
                encrypted = f.read()
            decrypted = self.cipher.decrypt(encrypted)
            return json.loads(decrypted)

    def save(self):
        with open(MEMORY_FILE, "wb") as f:
            f.write(self.cipher.encrypt(json.dumps(self.data).encode()))

    def log_vitals(self, heart_rate, steps, motion, weight):
        self.data["vitals"].append({
            "timestamp": datetime.now().isoformat(),
            "heart_rate": heart_rate,
            "steps": steps,
            "motion": motion,
            "weight": weight
        })
        self.save()

    def log_alert(self, alert_type):
        self.data["alerts"].append({
            "timestamp": datetime.now().isoformat(),
            "type": alert_type
        })
        self.save()

    def update_battery(self, device, level):
        self.data["battery_status"][device] = level
        self.save()

    def get_latest(self):
        return self.data
