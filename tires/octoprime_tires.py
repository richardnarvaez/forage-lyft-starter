from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        return sum(self.tires) >= 3.0