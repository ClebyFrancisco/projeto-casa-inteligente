from ligth import Ligth
from thermostat import Thermostat
from security_system import SecuritySystem

class DeviceFactory:
    @staticmethod
    def create_device(type):
        type = type.lower()

        if type == 'ligth':
            return Ligth()
        elif type == 'thermostat':
            return Thermostat()
        elif type == 'security system':
            return SecuritySystem()
        else:
            raise ValueError("unknown device type")