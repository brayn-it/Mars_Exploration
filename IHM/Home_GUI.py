import tkinter as tk
import PIL.ImageTk
import customtkinter as ctk
import PIL
from IHM.utilities import *
from IHM.customized_elements import *
from Controllers.Home_Ctrl import Home_Ctrl
from IHM.Login_pg_GUI import Login_pg_GUI

#HOMEGUI EST LA PAGE D'ACCUEIL

class Home_GUI(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,corner_radius=0,fg_color="#2B2B2B",bg_color="#2B2B2B")
        self.master = master
        #self.pack(expand=True,fill="both",side="top",anchor="center")

        #//Controller
        self.controller = Home_Ctrl(self.master)

        self.bg_img = PIL.ImageTk.PhotoImage(bg_img)
        self.bg_canva = tk.Canvas(self,background="#2B2B2B")
        self.bg_canva.place(x=0,y=0,relheight=1,relwidth=1)
        self.bg_canva.create_image(0,0,image=self.bg_img,anchor="nw",tags="IMG")
        self.top_frame = ctk.CTkFrame(self,fg_color="#2B2B2B",bg_color="#2B2B2B",height=180)
        self.left_frame = ctk.CTkFrame(self,fg_color="#2B2B2B",width=400,corner_radius=0)
        self.top_frame.pack(side="top",fill="x")
        self.left_frame.pack(side="left",fill="y")
        self.bg_canva.lift(1)
        #self.bg_canva.create_window(0,0,window=self.top_frame,anchor="nw")
        
        #widgets

        self.create_title_frame()
        #START SIMULATION BUTTON
        self.sim_button = self.create_button("Start Simulation")
        
        #ROBOT DATASHEET BUTTON
        self.rbt_ds_button = self.create_button("Robots datasheets")

        #MODULE DATASHEET BUTTTON
        self.mod_ds_button = self.create_button("Module datasheets")

        #USERS INFO BUTTON
        self.user_info_button = self.create_button("Users Information")

        #QUIT Button
        self.quit_button = self.create_quit_button()

        #//////////////BIND AVEC LE CONTROLLER
        #Start Simulation
        self.sim_button.configure(command=self.controller.to_login_pg)

    def create_title_frame(self):
        self.title_frame = Title_Frame(self.top_frame)
        self.title_frame.pack(anchor="center",expand=True,ipadx=40,ipady=40,pady=20)


    def create_button(self,text,width=380,height=60):
        """Renvoie les boutons de la page d'accueil"""
        bt = ctk.CTkButton(self.left_frame,text=text,text_color="white",font=("Roboto",28),fg_color=colors["button_bg"],border_width=2,border_color=colors["border"],width=width,height=height)
        bt.pack(side="top",padx=10,pady=30,ipadx=50,ipady=5)
        return bt
    
    def create_quit_button(self):
        """Renvoie le boutton pour quitter"""
        self.power_icon = ctk.CTkImage(power_icon)
        bt = Quit_Button(self.master)
        bt.place(x=1100,y=700)
        return bt
    
    def quit_app(self,event=None):
        self.master.destroy()