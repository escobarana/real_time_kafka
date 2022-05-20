schema = """
{
  "description": "Sensor's measurements",
  "properties": {
    "maximum": {
      "description": "Sensor's maximum value reachable (ºC, w, %)",
      "type": "number"
    },
    "measure": {
      "description": "Sensor's measure (ºC, w, %)",
      "type": "number"
    },
    "name": {
      "description": "Sensor's name",
      "type": "string"
    },
    "sensor_id": {
      "description": "Sensor's identifier",
      "type": "string"
    },
    "sensor_type": {
      "description": "Sensor's type (Temperature, Power, Load)",
      "type": "string"
    }
  },
  "required": [
    "sensor_id",
    "name",
    "sensor_type",
    "measure",
    "maximum"
  ],
  "title": "Sensor",
  "type": "object"
}
"""
