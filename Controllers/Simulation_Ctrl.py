import customtkinter as ctk

import sys
import os

# Ajouter le chemin racine du projet
sys.path.append(os.path.abspath("."))
from IHM import Simulation_GUI as simgui
from Model import Simulator
from Model import CentralBase as cb
from Model import ExplorationRobot


class Simulation_Ctrl():
    def __init__(self,root:ctk.CTk,gui:simgui,simulator:Simulator):
        self.simulation_gui  = gui
        self.simulator = simulator
        self.root= root

        self.update()
    def update(self):
        """Mettre à jour la simulation"""
        self.simulator.update()
        self.canvas.delete("all")
        
        # Affichage de la base
        if self.simulator.base:
            x, y = self.simulator.base.position
            self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow")

        # Déplacement et affichage des robots
        if self.simulator.robots:
            for robot in self.robots:
                robot.move()
                self.canvas.create_oval(robot.x - 5, robot.y - 5, robot.x + 5, robot.y + 5, fill="blue")
                self.canvas.create_text(robot.x, robot.y - 10, text=robot.id, fill="white")

    def run(self):
        while(self.state=="running"):
            self.update()
            self.root.update(500)

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1280x800")
    sim = Simulator.Simulator()
    view = simgui.Simulation_GUI(root)
    ctrl = Simulation_Ctrl(root,view,sim)

    #////////Init simulation//////
    sim.base = cb.CentralBase(100,100)
    sim.add_robot(ExplorationRobot.ExplorationRobot(sim.base.position))
    sim.add_robot(ExplorationRobot.ExplorationRobot(sim.base.position))
    sim.add_robot(ExplorationRobot.ExplorationRobot(sim.base.position))

    sim.create_group()

    sim.groupes[0].assign_exploration_mission((500,500))
    sim.groupes[0].start_exploration_mission()

    ctrl.run()

    root.mainloop()