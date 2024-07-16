from .light import Light
from .thermostat import Thermostat
from .security_system import SecuritySystem

class DeviceFactory:
    @staticmethod
    def create_device(type):
        type = type.lower()

        if type == 'light':
            return Light()
        elif type == 'thermostat':
            return Thermostat()
        elif type == 'security_system':
            return SecuritySystem()
        else:
            raise ValueError("unknown device type")