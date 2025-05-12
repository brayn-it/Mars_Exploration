import customtkinter as ctk
from tkinter import ttk
from utilities import *
from customized_elements import *
import PIL.ImageTk

class Simulation_Pg_GUI(ctk.CTkFrame):
    def __init__(self, master, width=1200, height=800, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = "black", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.pack(expand=True,fill="both")

        self.main_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.main_frame.pack(expand=True,fill="both")



if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1200x800+50+50")
    pg = Simulation_Pg_GUI(root)
    root.mainloop()