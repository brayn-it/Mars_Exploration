import customtkinter as ctk
from IHM.Login_pg_GUI import Login_pg_GUI

class Home_Ctrl:
    def __init__(self,root):
        self.root = root

    
    def to_login_pg(self):
        self.root.add_page("login",Login_pg_GUI(self.root))
        self.root.change_page_to("login")