import wmi
from sensors.sensor import Sensor


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
        sensor = Sensor(sensor_id="", name="", sensor_type="", measure=0, maximum=0)
        for each in self.temperature_info:
            if each.SensorType == 'Temperature':
                sensor.set_sensor_id(each.InstanceId)
                sensor.set_name(each.Name)
                sensor.set_sensor_type(each.SensorType)
                sensor.set_measure(each.Value)
                sensor.set_maximum(each.Max)
        return sensor

    def get_power(self) -> Sensor:
        """
        Function to measure CPU power in watt
        :return: Sensor object containing CPU power sensor relevant information
        """
        sensor = Sensor(sensor_id="", name="", sensor_type="", measure=0, maximum=0)
        for each in self.temperature_info:
            if each.SensorType == 'Power':
                sensor.set_sensor_id(each.InstanceId)
                sensor.set_name(each.Name)
                sensor.set_sensor_type(each.SensorType)
                sensor.set_measure(each.Value)
                sensor.set_maximum(each.Max)
        return sensor

    def get_load(self) -> Sensor:
        """
        Function to measure CPU load in percentage
        :return: Sensor object containing CPU load sensor relevant information
        """
        sensor = Sensor(sensor_id="", name="", sensor_type="", measure=0, maximum=0)
        for each in self.temperature_info:
            if each.SensorType == 'Load':
                sensor.set_sensor_id(each.InstanceId)
                sensor.set_name(each.Name)
                sensor.set_sensor_type(each.SensorType)
                sensor.set_measure(each.Value)
                sensor.set_maximum(each.Max)
        return sensor
