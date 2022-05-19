import wmi


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

    def get_temperature(self):
        """
        Function to measure CPU temperature in celsius
        :return: dictionary containing CPU temperature sensor relevant information
        """
        measure = dict
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Temperature':
                measure = {'id': sensor.InstanceId,
                           'name': sensor.Name,
                           'type': sensor.SensorType,
                           'measure_celsius': sensor.Value,
                           'maximum_celsius': sensor.Max}
        return measure

    def get_power(self):
        """
        Function to measure CPU power in watt
        :return: dictionary containing CPU temperature sensor relevant information
        """
        measure = dict
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Power':
                measure = {'id': sensor.InstanceId,
                           'name': sensor.Name,
                           'type': sensor.SensorType,
                           'measure_watt': sensor.Value,
                           'maximum_watt': sensor.Max}
        return measure

    def get_load(self):
        """
        Function to measure CPU load in percentage
        :return: dictionary containing CPU temperature sensor relevant information
        """
        measure = dict
        for sensor in self.temperature_info:
            if sensor.SensorType == 'Load':
                measure = {'id': sensor.InstanceId,
                           'name': sensor.Name,
                           'type': sensor.SensorType,
                           'measure_percentage': sensor.Value,
                           'maximum_percentage': sensor.Max}
        return measure
