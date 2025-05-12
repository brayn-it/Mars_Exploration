from Model.Robot import *

# Classe Robot de Réparation
class RepairRobot(Robot):
    def __init__(self, pos, base_pos):
        super().__init__(pos, 4, "repair", base_pos)
        self.cout = 600

    def repair_robot(self):
        if self.target_robot.usure < 100:
            self.target_robot.usure = max(0, self.target_robot.usure - 50)
            self.send_message(f"Robot {self.target_robot.id} réparé.")

    def set_target_robot(self,robot):
        self.set_target(robot)
        self.set_mission((robot.x,robot.y))
        
    def move(self):
        self.follow_target()
        if self.target_robot and self.target_robot.get_position() == self.get_position():
            self.repair_robot()
        super().move()