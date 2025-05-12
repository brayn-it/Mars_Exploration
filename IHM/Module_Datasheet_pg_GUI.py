import customtkinter as ctk
from tkinter import ttk
from utilities import *
from customized_elements import *
from Module_Datasheet_GUI import *
import PIL.ImageTk

class Module_Datasheet_pg_GUI(ctk.CTkFrame):
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

        #Central frame

        self.central_frame = Bg_Frame(self,1000,600)
        self.central_frame.place(relwidth=0.9,relx=0.05,rely=0.2)
        self.central_frame_main_frame = ctk.CTkFrame(self.central_frame,fg_color="transparent",bg_color="transparent")
        self.central_frame_main_frame.pack(expand=True,fill="both",padx=10,pady=10)


        #IN Central Frame
        #row 0
        self.frame_row0 = ctk.CTkFrame(self.central_frame_main_frame,height=80,fg_color="transparent")
        self.frame_row0.pack(expand=True,fill="x",side="top")
        
        #Module Datasheets
        self.datasheet_title = ctk.CTkLabel(self.frame_row0,text="MODULES DATASHEET",font=("Roboto",30,"bold"),text_color="white",fg_color="transparent")
        self.datasheet_title.pack(expand=True,pady=15,anchor="center")

        #Frame pour mettre le tableau
        self.datasheet_frame = ctk.CTkFrame(self.central_frame_main_frame,height=400,fg_color="transparent")
        self.datasheet_frame.pack(side="top",expand=True,fill="x")

        #Prend le datasheet selon la navigation
        self.current_datasheet = Module_Datasheet_GUI(self.datasheet_frame)
        self.current_datasheet.pack(expand=True,fill="both")
        
        #Bouton home
        self.home_button = Home_Button(self.master,fg_color="transparent",bg_color="transparent")
        self.home_button.place(relx=0.85,rely=0.9)

        #Quit button
        self.quit_button = Quit_Button(self.master,fg_color="transparent",bg_color="transparent")
        self.quit_button.place(relx=0.9,rely=0.9)

if __name__=="__main__":
    root=ctk.CTk()
    root.geometry(("1200x800+5+5"))
    pg = Module_Datasheet_pg_GUI(root)
    pg.pack()
    root.mainloop()