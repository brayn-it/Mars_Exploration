import customtkinter as ctk

class Login_pg_Ctrl:
    def __init__(self,root):
        self.root = root

    
    def to_home_pg(self):
        self.root.change_page_to("home")