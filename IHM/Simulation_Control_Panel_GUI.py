import customtkinter as ctk
from tkinter import ttk
from utilities import *
from customized_elements import *
import PIL.ImageTk

class Simulation_Control_Panel_GUI(Bg_Frame2):
    def __init__(self, master, width=600, height=200, corner_radius=40):
        super().__init__(master, width, height, corner_radius)

        self.main_frame = ctk.CTkFrame(self,fg_color="transparent",corner_radius=corner_radius)
        self.main_frame.pack(expand=True,fill="both",padx=10,pady=10)
        
        #val division 
        div = 1/7

        #Col 0
        self.col0 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col0.place(relheight=1,relwidth=div)

        #Col 1
        self.col1 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col1.place(relheight=1,relwidth=div,relx=div)

        #Col 2
        self.col2 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col2.place(relheight=1,relx=div*2,relwidth=div)

        #Col 3
        self.col3 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col3.place(relx=div*3,relheight=1,relwidth=div)

        #Col 4
        self.col4 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col4.place(relx=div*4,relheight=1,relwidth=div)

        #Col 5
        self.col5 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col5.place(relx=div*5,relheight=1,relwidth=div)

        #Col 6
        self.col6 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.col6.place(relx=div*6,relheight=1,relwidth=div)



if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("800x800")
    
    frm = ctk.CTkFrame(root)
    frm.pack(expand=True,fill="both")
    panel = Simulation_Control_Panel_GUI(frm)
    panel.pack()
    root.mainloop()