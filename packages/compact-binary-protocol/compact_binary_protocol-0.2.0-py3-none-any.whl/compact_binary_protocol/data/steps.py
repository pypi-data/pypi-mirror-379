import struct
from .constants import TYPE_STEPS

class DataSteps:
    def __init__(self, battery: int, rssi: int, steps: int):
        self.sensor_type = TYPE_STEPS
        self.sensor_version = 1
        self.battery = int(battery)
        self.rssi = int(rssi)
        self.steps = int(steps)

    def to_bytes(self):
        payload = struct.pack('>BBi', self.battery, self.rssi, self.steps)
        header = struct.pack('>BBH', self.sensor_type, self.sensor_version, len(payload))
        return header + payload

    def describe(self):
        return (
            f"Steps(type={self.sensor_type}, ver={self.sensor_version}, "
            f"batt={self.battery}%, rssi={self.rssi}, steps={self.steps})"
        )
