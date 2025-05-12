import customtkinter as ctk
from IHM.Robots_Choice_pg_GUI import Choose_Rbts_GUI

class Login_Panel_Ctrl:
    def __init__(self,root):
        self.root = root

    
    def to_choose_robots_pg(self):
        self.root.add_page("choose_robots",Choose_Rbts_GUI(self.root))
        self.root.change_page_to("choose_robots")