import numpy as np
import time

class IotTelemetryProcessor:
    """
    High-Throughput IoT Sensor Stream Processor
    Maintains rolling averages and triggers alert thresholds on telemetries.
    """
    def __init__(self, rolling_window=10, limit=90.0):
        self.window = rolling_window
        self.limit = limit
        self.stream = []

    def ingest_reading(self, sensor_val):
        self.stream.append(sensor_val)
        if len(self.stream) > self.window:
            self.stream.pop(0)
        
        rolling_avg = np.mean(self.stream)
        if rolling_avg > self.limit:
            return f"ALERT: Rolling average reached {rolling_avg:.2f}! Limit exceeded!"
        return f"Reading ingested. Rolling Avg: {rolling_avg:.2f}"

if __name__ == "__main__":
    processor = IotTelemetryProcessor()
    for temp in [75.0, 80.0, 85.0, 92.0, 95.0]:
        print(processor.ingest_reading(temp))
