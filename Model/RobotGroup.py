import uuid
from Model.Robot import *
from Model.ExplorationRobot import *
from Model.RepairRobot import *
from Model.CarrierRobot import *
from Model.GeologicalRobot import *

import customtkinter as ctk
# Classe Groupe de Robots
class RobotGroup:
    def __init__(self, nom):
        self.id = str(uuid.uuid4())[:8]  # Identifiant unique
        self.nom = nom
        self.robots = []
        self.mission = None #Mission principale d'exploration

    def add_robot(self, robot):
        """Ajouter un robot au groupe"""
        if robot not in self.robots:
            self.robots.append(robot)
            print(f"Robot {robot.id} ajouté au groupe {self.nom}")

    def remove_robot(self, robot):
        """Retirer un robot du groupe"""
        if robot in self.robots:
            self.robots.remove(robot)
            print(f"Robot {robot.id} retiré du groupe {self.nom}")

    def assign_exploration_mission(self, mission_pos):
        """Assigner une mission collective d'exploration ;  reserve aux robots d'exploration"""
        self.mission = mission_pos
        for robot in self.robots:
            if isinstance(robot,ExplorationRobot):
                robot.set_mission(mission_pos)
        print(f"Mission d'exploration assignée au groupe {self.nom} : {mission_pos}")

    def assign_geological_mission(self, mission_pos):
        """Assigner une mission collective d'exploration ;  reserve aux robots d'exploration"""
        #self.mission = mission_pos
        for robot in self.robots:
            if isinstance(robot,GeologicalRobot):
                robot.set_mission(mission_pos)
        print(f"Mission d'exploration assignée au groupe {self.nom} : {mission_pos}")

    def assign_repair_mission(self, target_robot):
        """Assigner une mission collective d'exploration ;  reserve aux robots d'exploration"""
        #self.mission = mission_pos
        for robot in self.robots:
            if isinstance(robot,RepairRobot):
                robot.set_target_robot(target_robot)
        print(f"Mission de reparation assignée au groupe {self.nom} : {robot.x,robot.y}")
    
    def assign_carrier_mission(self, target_robot):
        """Assigner une mission collective d'exploration ;  reserve aux robots d'exploration"""
        #self.mission = mission_pos
        for robot in self.robots:
            if isinstance(robot,CarrierRobot):
                robot.set_target_robot(target_robot)
        print(f"Mission d'exploration assignée au groupe {self.nom} : {robot.x,robot.y}")

    def start_exploration_mission(self):
        """Démarrer le déplacement des robots d'exploration"""
        if self.mission:
            for robot in self.robots:
                if isinstance(robot,ExplorationRobot):
                    robot.start_mission()
            print(f"Groupe {self.nom} en route vers {self.mission} pour Exploration.")

    def start_geological_mission(self):
        """Démarrer le déplacement des robots de recolte geo"""
        if self.mission:
            for robot in self.robots:
                if isinstance(robot,GeologicalRobot):
                    robot.start_mission()
            print(f"Groupe {self.nom} en route vers {self.mission} pour récolte géo.")

    def start_repair_mission(self):
        """Démarrer le déplacement des robots de reparation"""
        if self.mission:
            for robot in self.robots:
                if isinstance(robot,RepairRobot):
                    robot.start_mission()
            print(f"Groupe {self.nom} en route vers {self.mission} pour réparation.")

    def start_carrier_mission(self):
        """Démarrer le déplacement des robots de reparation"""
        if self.mission:
            for robot in self.robots:
                if isinstance(robot,CarrierRobot):
                    robot.start_mission()
            print(f"Groupe {self.nom} en route vers {self.mission} pour réparation.")

    def print_composition(self):
        """Afficher la composition du groupe"""
        print(f"Groupe {self.nom} - ID : {self.id}")
        for robot in self.robots:
            print(f"- Robot {robot.id} ({robot.type})")

    def update(self):
        """Faire avancer tous les robots du groupe selon leur etat"""
        for robot in self.robots:
            robot.move()
            print(f"Robot id : {robot.id}")
            print(f"Robot pos : {robot.x,robot.y}\n\n")

#TODO Carrier Robot missions

if __name__=="__main__":
    root = ctk.CTk()
    gp = RobotGroup("Groupe")
    rob = ExplorationRobot((0,0),(0,0))
    rob1 = GeologicalRobot((0,0),(0,0))
    rob2 = RepairRobot((0,0),(0,0))
    gp.add_robot(rob)
    gp.add_robot(rob1)
    gp.add_robot(rob2)
    gp.print_composition()
    gp.assign_exploration_mission((500,500))
    gp.start_exploration_mission()
    gp.assign_geological_mission((400,400))
    i=0
    while(1):
        if i == 20:
            gp.start_geological_mission()
            gp.assign_repair_mission(gp.robots[0])
            gp.start_repair_mission()
        root.after(100,gp.update())
        print("i=",i)
        print(rob2.etat)
        i+=1

    root.mainloop()