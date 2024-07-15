class SmartHome:
    __instance = None
    def __new__(cls):
        if SmartHome.__instance is None:
            SmartHome.__instance = super().__new__(cls)
        return SmartHome.__instance
    
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
    