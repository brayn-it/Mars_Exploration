from Model.Module import *

# Module de Batterie
class BatteryModule(Module):
    def __init__(self):
        super().__init__("battery", 2)

    def recharge_robot(self, robot):
        """Recharge un robot"""
        if self.use():
            robot.batterie = 100
            print(f"Robot {robot.id} rechargé à 100%")

if __name__=="__main__":
    pass