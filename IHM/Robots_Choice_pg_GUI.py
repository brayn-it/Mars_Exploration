import customtkinter as ctk
import PIL.ImageTk
import PIL

from IHM.Robots_Choice_Panel_GUI import Robots_Choice_Panel_GUI
from IHM.customized_elements import *

class Choose_Rbts_GUI(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        """Page choix des robots"""
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.master = master
        self.pack(expand=True,fill="both")

        #canva for bg
        self.canva = ctk.CTkCanvas(self)
        #bg img
        self.bg_img = PIL.ImageTk.PhotoImage(bg_img)
        self.canva.create_image(0,0,image=self.bg_img,anchor="nw",tags="IMG")
        #place bg
        self.canva.place(x=0,y=0,relwidth=1,relheight=1)

        #Title Frame
        self.title_frame = Title_Frame(self.master)
        self.title_frame.place(relx=0.5,rely=0.1,relwidth=0.95,anchor="center")

        #Robots_choice_panel
        self.robots_choice_panel = Robots_Choice_Panel_GUI(self)
        self.robots_choice_panel.place(relx=0.1,rely=0.2,relwidth=0.8)
        

        
        #Bouton home
        self.home_button = Home_Button(self.master,fg_color="transparent",bg_color="transparent")
        self.home_button.place(relx=0.85,rely=0.9)

        #Quit button
        self.quit_button = Quit_Button(self.master,fg_color="transparent",bg_color="transparent")
        self.quit_button.place(relx=0.9,rely=0.9)

if __name__=="__main__":
    root=ctk.CTk()
    root.geometry("1000x800")
    pg = Choose_Rbts_GUI(root)
    pg.pack()
    root.mainloop()