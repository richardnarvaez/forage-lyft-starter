from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        return any(tire >= 0.9 for tire in self.tires)