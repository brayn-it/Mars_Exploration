import customtkinter as ctk
from IHM.Simulation_GUI import Simulation_GUI

if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1280x720+50+50")
    pg = Simulation_GUI(root)
    pg.pack(fill="both",expand=True)
    root.mainloop()