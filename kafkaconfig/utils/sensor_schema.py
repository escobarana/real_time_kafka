schema = """
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Sensor",
  "description": "Sensor's measurements",
  "type": "object",
  "properties": {
    "sensor_id": {
      "description": "Sensor's identifier",
      "type": "string"
    },
    "name": {
      "description": "Sensor's name",
      "type": "string"
    },
    "sensor_type": {
      "description": "Sensor's type (Temperature, Power, Load)",
      "type": "string"
    },
    "measure": {
      "description": "Sensor's measure (ºC, w, %)",
      "type": "number"
    },
    "maximum": {
      "description": "Sensor's maximum value reachable (ºC, w, %)",
      "type": "number"
    }
  },
  "required": ["sensor_id", "name", "sensor_type", "measure", "maximum"]
}
"""
