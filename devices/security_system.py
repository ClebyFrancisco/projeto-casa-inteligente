from abstract_device import AbstractDevice
from transitions import Machine

class SecuritySystem(AbstractDevice):
    states = ['unarmed', 'armed_with_people_at_home', 'armed_without_anyone_at_home']

    def __init__(self):
        self.machine = Machine(model=self, states=SecuritySystem.states, initial='unarmed')
    
    def current_status(self):
        pass