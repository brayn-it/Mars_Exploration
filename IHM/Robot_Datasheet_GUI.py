import customtkinter as ctk
from tkinter import ttk
from utilities import *
from customized_elements import *

class Robot_Datasheet_GUI(Datasheet_Table):
    def __init__(self, master=None, class_="", columns=("Attributes","Details"), cursor="", displaycolumns=None, height=10, name=None, padding=None, selectmode="extended", show="headings", style="", takefocus=None, xscrollcommand="", yscrollcommand=""):
        """Datasheet des robots"""
        super().__init__(master, class_, columns, cursor, displaycolumns, height, name, padding, selectmode, show, style, takefocus, xscrollcommand, yscrollcommand)
        self.column("Attributes",width=150,anchor="center",stretch=True)
        self.column("Details",width=550,anchor="w",stretch=True)

    def insert_value(self,value):
        if len(value)==2:
            self.insert(parent="",index='end',values=value) 
        #TODO Connecter au controleur pour recuperer les donnees

if __name__=="__main__":
    root = ctk.CTk()
    root.geometry(("1000x800"))
    tab = Robot_Datasheet_GUI(root)
    tab.insert_value(("Role","lorem ipsum"))
    tab.pack()
    root.mainloop()