from devices.abstract_device import AbstractDevice
from transitions import Machine


class Light(AbstractDevice):

    states = ['off', 'on']

    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=Light.states, initial='off')
        self.machine.add_transition(trigger='turnOn', source='off', dest='on')
        self.machine.add_transition(trigger='turnOff', source='on', dest='off')
    
    def current_status(self):
        return self.state
    
    def turn_on(self):
        self.turn_on()

    def turn_off(self):
        self.turn_off()
