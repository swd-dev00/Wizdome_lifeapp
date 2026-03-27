import time

class AlertSystem:
    def __init__(self, memory):
        self.memory = memory

    def run(self):
        processed_alerts = set()
        while True:
            alerts = self.memory.get_latest()["alerts"]
            for alert in alerts:
                alert_id = alert["timestamp"] + alert["type"]
                if alert_id not in processed_alerts:
                    print(f"[AlertSystem] ALERT: {alert['type']} at {alert['timestamp']}")
                    processed_alerts.add(alert_id)
            time.sleep(5)
