import wmi
from sensor import Sensor


class Measures:
    """
    Class Measures which measures different types of CPU sensors (Temperature, Power, Load)
    """

    def __init__(self):
        """
        Initialization of the class Measures using wmi library and OpenHardMonitor Software
        """
        w = wmi.WMI(namespace="root\OpenHardwareMonitor")
        self.temperature_info = w.Sensor()

    def get_temperature(self) -> Sensor:
        """
        Function to measure CPU temperature in celsius
        :return: Sensor object containing CPU temperature sensor relevant information
        """
        sensor = None
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Temperature':
                sensor = Sensor(sensor_id=sensor.InstanceId,
                                name=sensor.Name,
                                sensor_type=sensor.SensorType,
                                measure=sensor.Value,
                                maximum=sensor.Max)
        return sensor

    def get_power(self) -> Sensor:
        """
        Function to measure CPU power in watt
        :return: Sensor object containing CPU power sensor relevant information
        """
        sensor = None
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Power':
                sensor = Sensor(sensor_id=sensor.InstanceId,
                                name=sensor.Name,
                                sensor_type=sensor.SensorType,
                                measure=sensor.Value,
                                maximum=sensor.Max)
        return sensor

    def get_load(self) -> Sensor:
        """
        Function to measure CPU load in percentage
        :return: Sensor object containing CPU load sensor relevant information
        """
        sensor = None
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Load':
                sensor = Sensor(sensor_id=sensor.InstanceId,
                                name=sensor.Name,
                                sensor_type=sensor.SensorType,
                                measure=sensor.Value,
                                maximum=sensor.Max)
        return sensor
