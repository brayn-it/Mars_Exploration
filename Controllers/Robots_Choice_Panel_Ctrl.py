import customtkinter as ctk
from IHM.Simulation_GUI import Simulation_GUI

class Robots_Choice_Panel_Ctrl:
    def __init__(self,root):
        self.root = root

    
    def to_simulation_pg(self):
        print("OOOOOOOKKKKKK")
        self.root.add_page("simulation_page",Simulation_GUI(self.root))
        self.root.change_page_to("simulation_page")