import customtkinter as ctk
from tkinter import ttk
from utilities import *
from customized_elements import *

col = ("Module Name","Purpose","Compatible Robots", "Energy Consumption","Special Feature","Limitations")

class Module_Datasheet_GUI(Datasheet_Table):
    def __init__(self, master=None, class_="", columns=col, cursor="", displaycolumns=None, height=10, name=None, padding=None, selectmode="extended", show="headings", style="", takefocus=None, xscrollcommand="", yscrollcommand=""):
        super().__init__(master, class_, columns, cursor, displaycolumns, height, name, padding, selectmode, show, style, takefocus, xscrollcommand, yscrollcommand)
        self.style.configure("hds",font=("Roboto",16,"bold"))
        for col in columns:
            self.column(col,width=150,anchor="w",stretch=True)
        self.configure(style="Custom.Treeview")
    def insert_value(self,value):
        if len(value)==6:
            self.insert(parent="",index='end',values=value) 
        #TODO Connecter au controleur pour recuperer les donnees

if __name__=="__main__":
    root = ctk.CTk()
    root.geometry(("1000x800"))
    tab = Module_Datasheet_GUI(root)
    tab.insert_value(("Role","lorem ipsum","sdfs","sdfsd","sdfsd","asdf"))
    tab.pack()
    root.mainloop()