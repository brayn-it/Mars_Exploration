import PIL.ImageTk
import customtkinter as ctk
import PIL
from IHM.Login_Panel_GUI import Login_Panel_GUI
from IHM.utilities import *
from IHM.customized_elements import *
from Controllers.Login_pg_Ctrl import Login_pg_Ctrl

class Login_pg_GUI(ctk.CTkFrame):
    def __init__(self, master, width=200, height=200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = None, border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.master = master

        self.controller = Login_pg_Ctrl(self.master)

        self.pack(expand=True,fill="both")
        #canva for bg
        self.canva = ctk.CTkCanvas(self)
        #bg img
        self.bg_img = PIL.ImageTk.PhotoImage(bg_img)
        self.canva.create_image(0,0,image=self.bg_img,anchor="nw",tags="IMG")
        #place bg
        self.canva.place(x=0,y=0,relwidth=1,relheight=1)
        #Title frame
        self.title_frame = Title_Frame(self.master)
        self.title_frame.place(relx=0.5,rely=0.1,relwidth=0.9,anchor="center")

        #Login panel form
        self.login_panel = Login_Panel_GUI(self)
        self.login_panel.place(rely=0.3,relwidth=0.6,relx=0.2)

        #Bouton home
        self.home_button = Home_Button(self.master)
        self.home_button.place(relx=0.85,rely=0.9)

        #Quit button
        self.quit_button = Quit_Button(self.master)
        self.quit_button.place(relx=0.9,rely=0.9)


        #BIND CONTROLLER
        self.home_button.configure(command=self.controller.to_home_pg)
        self.quit_button.configure(command=self.master.destroy)


if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1200x800+50")
    lg = Login_pg_GUI(root)
    root.mainloop()