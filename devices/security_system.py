from devices.abstract_device import AbstractDevice
from transitions import Machine

class SecuritySystem(AbstractDevice):
    states = ['unarmed', 'armed_with_people_at_home', 'armed_without_anyone_at_home']

    def __init__(self):
        super().__init__()
        self.machine = Machine(model=self, states=SecuritySystem.states, initial='unarmed')
        self.machine.add_transition(trigger='armed_without_people_at_home', source='unarmed', dest='armed_without_people_at_home')
        self.machine.add_transition(trigger='armed_with_people_at_home', source='unarmed',  dest='armed_with_people_at_home')
        self.machine.add_transition(trigger='unarmed', source=['armed_without_people_at_home', 'armed_with_people_at_home'], dest='unarmed')
    
    def current_status(self):
        return self.state