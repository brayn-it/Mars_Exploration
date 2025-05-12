import customtkinter as ctk

from IHM.customized_elements import *
from IHM.utilities import *

from Controllers.Robots_Choice_Panel_Ctrl import Robots_Choice_Panel_Ctrl

class Robots_Choice_Panel_GUI(Bg_Frame):
    def __init__(self, master, width=800, height=700):
        super().__init__(master, width, height)
        self.master=master

        #CONTROLLER
        self.controller = Robots_Choice_Panel_Ctrl(self.master.master)

        self.main_frame = ctk.CTkFrame(self,fg_color="transparent")
        self.main_frame.pack(expand=True,fill="both",pady=20,padx=10)
        #ROBOTS    ?   (ligne 1)
        self.frame_row1 = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.frame_row1.pack(side="top",expand=True,fill="x")
        self.rbts_label = Blue_Text_Label(self.frame_row1,text="R O B O T S",font=("Roboto",28),fg_color="transparent",anchor="nw")
        self.rbts_label.pack(side="left",expand=True,anchor="nw")

        self.help_label = Blue_Text_Label(self.frame_row1,text="?",font=("Roboto",28),fg_color="transparent",anchor="nw")
        self.help_label.pack(side="right",expand=True,anchor="e")

        self.seg_frame = ctk.CTkFrame(self.main_frame,width=720,fg_color="transparent")
        self.seg_frame.pack(side="top",expand=True,fill="x")
        #LES SEGMENTS DE CHOIX
        self.seg_exploration = self.create_segment("Exploration")
        self.seg_geological = self.create_segment("Geological")
        self.seg_reparation = self.create_segment("Reparation")
        self.seg_carrier = self.create_segment("Carrier")

        #ROW2
        self.button_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.button_frame.pack(side="top",fill="x",expand=True)

        #Cancel button
        self.cancel_button = Black_Button(self.button_frame,text="Cancel")
        self.cancel_button.pack(side="left")

        #Continue button
        self.continue_button = Blue_Button(self.button_frame,text="Continue")
        self.continue_button.pack(side="left")

        #Bind controller
        #To simulation main page
        self.continue_button.configure(command=self.controller.to_simulation_pg)



    def create_segment(self,robottype):
        """Cree le segment qui contient le label de type de robots et le scale de choix"""
        seg = Robots_Choice_Segment(self.seg_frame,robottype)
        seg.pack(side="top",pady=20)
        return seg

if __name__=="__main__":
    root = ctk.CTk(fg_color="black")
    root.geometry("1000x800")
    rbts = Robots_Choice_Panel_GUI(root)
    rbts.place(relx=0.2,rely=0.1,relwidth=0.7)
    root.mainloop()