from devices.abstract_device import AbstractDevice
from transitions import Machine

class Thermostat(AbstractDevice):

    states = ['off', 'heating', 'cooling']

    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=Thermostat.states, initial='off')
        self.machine.add_transition(trigger='warm', source='off', dest='heating')
        self.machine.add_transition(trigger='coolDown', source='off', dest='cooling')
        self.machine.add_transition(trigger='turnOff', source=['heating', 'cooling'], dest='off')

        
    def current_status(self):
        return self.state
