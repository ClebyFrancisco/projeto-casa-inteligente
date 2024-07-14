from abstract_device import AbstractDevice
from transitions import Machine

class Thermostat(AbstractDevice):

    states = ['off', 'heating', 'cooling']

    def __init__(self):
        self.machine = Machine(model=self, states=Thermostat.states, initial='off')
        
    def current_status(self):
        pass


