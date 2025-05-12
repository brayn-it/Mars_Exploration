from Model.Robot import *
from Model.BatteryModule import *
from Model.CollectModule import *
from Model.RepairModule import *

# Classe Robot Mule
class CarrierRobot(Robot):
    def __init__(self,pos, base_pos):
        super().__init__(pos, 1, "carrier", base_pos)
        self.cout = 300
        self.repair_module = BatteryModule()
        self.battery_module = CollectModule()
        self.repair_module = RepairModule()

    def transporter(self, module):
        self.modules.append(module)
        self.envoyer_message(f"Module {module.type} transporté.")