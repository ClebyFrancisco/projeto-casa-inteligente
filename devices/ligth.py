from abstract_device import AbstractDevice
from transitions import Machine

class Ligth(AbstractDevice):

    states = ['off', 'on']

    def __init__(self):
        self.machine = Machine(model=self, states=Ligth.states, initial='off')
    
    def current_status(self):
        pass
