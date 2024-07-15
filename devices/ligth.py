from abstract_device import AbstractDevice
from transitions import Machine

class Ligth(AbstractDevice):

    states = ['off', 'on']

    def __init__(self):
        self.machine = Machine(model=self, states=Ligth.states, initial='off')
        self.machine.add_transition(trigger='turnOn', source='off', dest='on')
        self.machine.add_transition(trigger='turnOff', source='on', dest='off')
    
    def current_status(self):
        return self.state
