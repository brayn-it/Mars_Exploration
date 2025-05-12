import customtkinter as ctk
from IHM.utilities import *
from IHM.customized_elements import *
from Controllers.Login_Panel_Ctrl import Login_Panel_Ctrl

class Login_Panel_GUI(Bg_Frame):
    def __init__(self, master, width=500, height=400):
        super().__init__(master, width, height)

        self.root = master.master
        #login label
        self.label = Blue_Text_Label(self,text="L O G I N")
        self.label.pack(side="top", padx=30, pady=5, anchor="w")

        #username entry
        self.username_entry = ctk.CTkEntry(self,width=720,placeholder_text="Username")
        self.username_entry.pack(side="top",anchor="center",expand=True,padx=30, pady=10)

        #password entry
        self.password_entry = ctk.CTkEntry(self,width=720,placeholder_text="Password",show="*")
        self.password_entry.pack(side="top",anchor="center",expand=True,padx=30, pady=10)

        #Cancel button
        self.cancel_button = Black_Button(self,text="Cancel")
        self.cancel_button.pack(side="left",padx=30,pady=5)

        #Connect button
        self.connect_button = Blue_Button(self,text="Connect")
        self.connect_button.pack(side="left",pady=5)

        #new account label
        self.nw_acc_label = Blue_Text_Label(self,text="Create a new account")
        self.nw_acc_label.pack(side="top",anchor="se",padx=10,pady=30,expand=True)


        #//////Controller///////////

        self.controller = Login_Panel_Ctrl(self.root)
        self.connect_button.configure(command=self.controller.to_choose_robots_pg)

if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("700x700")
    lg = Login_Panel_GUI(root)
    lg.pack()
    root.mainloop()