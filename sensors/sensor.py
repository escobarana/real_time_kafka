class Sensor:
    """
    Class to identify the properties of a sensor and deserialize the data when consuming from a Kafka topic
    """
    def __init__(self, sensor_id, name, sensor_type, measure, maximum):
        """
        Initialization of class Sensor
        :param sensor_id: Unique identifier of the sensor
        :param name: Sensor's name
        :param sensor_type: Type of the sensor (Temperature, Power, Load)
        :param measure: The value of the measure (ºC, w, %)
        :param maximum: Maximum value the sensor can reach
        """
        self.sensor_id = sensor_id
        self.name = name
        self.sensor_type = sensor_type
        self.measure = measure
        self.maximum = maximum
