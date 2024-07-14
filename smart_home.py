class SmartHome:
    __instance = None
    def __new__(cls):
        if SmartHome.__instance is None:
            SmartHome.__instance = super().__new__(cls)
        return SmartHome.__instance
    