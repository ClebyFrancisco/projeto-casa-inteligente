from abc import ABC, abstractmethod

class AbstractDevice(ABC):

    @abstractmethod
    def current_status(self):
        ...
    

