import PIL.ImageTk
import customtkinter as ctk
import PIL
from IHM.utilities import *
from IHM.customized_elements import *

class Simulation_Top_Panel(Bg_Frame2):
    def __init__(self, master, width=200, height=200, corner_radius=None, border_width=1, bg_color="transparent", fg_color=..., border_color=..., background_corner_colors=None, overwrite_preferred_drawing_method=None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.master = master

        