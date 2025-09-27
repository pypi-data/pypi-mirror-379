import struct
from .constants import TYPE_BASIC


class DataBasic:
    def __init__(self, temperature, battery, rssi):
        self.sensor_type = int(TYPE_BASIC)
        self.sensor_version = 1
        self.temperature = float(temperature)
        self.battery = int(battery)
        self.rssi = int(rssi)

    def to_bytes(self):
        payload = struct.pack('>HBB', int(self.temperature * 10), self.battery, self.rssi)
        header = struct.pack('>BBH', self.sensor_type, self.sensor_version, len(payload))
        return header + payload

    def describe(self):
        return f"Basic(type={self.sensor_type}, ver={self.sensor_version}, temp={self.temperature}°C, batt={self.battery}%, rssi={self.rssi})"
