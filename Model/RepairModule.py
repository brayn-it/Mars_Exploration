from Model.Module import *


# Module de Réparation
class RepairModule(Module):
    def __init__(self):
        super().__init__("reparair", 2)

    def repair_robot(self, robot):
        """Répare un robot"""
        if robot.usure < 100 and self.use():
            robot.usure = 0
            print(f"Robot {robot.id} réparé à 0% d'usure")