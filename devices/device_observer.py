from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, device):
        pass

class DeviceObserver(Observer):
    def update(self, device):
        print(f"{device.__class__.__name__} device status changed to {device.current_status()}")
