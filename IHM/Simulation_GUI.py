import PIL.ImageTk
import customtkinter as ctk
import PIL
from IHM.utilities import *
from IHM.customized_elements import *
from Model.Simulator import Simulator

class Simulation_GUI(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = None, bg_color = "transparent", fg_color = "#0C1B1E", border_color = None, background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.root = master


        self.main_frame = ctk.CTkFrame(self,fg_color = "#0C1B1E")
        self.main_frame.pack(fill="both",expand=True)

        #TOP FRAME
        self.top_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.top_frame.place(rely=0,relheight=0.15,relwidth=1)

        #LEFT FRAME 
        self.left_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.left_frame.place(rely=0.15,relheight=0.85,relwidth=0.6)

        #CanvaFrame
        self.canvas_frame = ctk.CTkFrame(self.left_frame,fg_color="transparent")
        self.canvas_frame.place(relheight=0.8,relwidth=1)
        self.canvas = ctk.CTkCanvas(self.canvas_frame)
        self.canvas.pack(expand=True,fill="both")
        
        #Attached Simulator
        self.simulator = Simulator(self.canvas,self.root)

        #RIGHT FRAME 
        self.right_frame = ctk.CTkFrame(self.main_frame,fg_color="transparent")
        self.right_frame.place(relheight=0.85,relx=0.6,rely=0.15,relwidth=0.4)

        

    def update_canvas(self, robots):
        """Mettre à jour l'affichage des robots"""
        self.canvas.delete("simulation")
        for robot in robots:
            x, y = robot.get_position()
            couleur = {
                "exploration": "blue",
                "geological": "green",
                "reparair": "red",
                "carrrier": "orange"
            }.get(robot.type, "white")
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=couleur)
            self.canvas.create_text(x, y - 10, text=f"{robot.id}", fill="white")

    def log_message(self, message):
        """Afficher un message dans la zone des logs"""
        self.message_box.insert("end", f"{message}\n")
        self.message_box.see("end")

if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1280x720")
    pg = Simulation_GUI(root)
    pg.pack(fill="both",expand=True)
    root.mainloop()