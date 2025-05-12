import customtkinter as ctk
from tkinter import ttk
from IHM.utilities import *


#background frame
#Fond gris fonce et bord bleu
class Bg_Frame(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = 1, bg_color = "transparent", fg_color = colors["bg2"], border_color = colors["border"], background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        """Renvoie un frame en fond gris fonce semi-translucide selon la taille souhaitee."""
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

#BACKGROUND FRAME 2
class Bg_Frame2(ctk.CTkFrame):
    def __init__(self, master, width = 200, height = 200, corner_radius = None, border_width = 1, bg_color = "transparent", fg_color = colors["bg3"], border_color = colors["border"],background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        """Renvoie un frame en fond #003946 selon la taille souhaitee."""
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color,background_corner_colors, overwrite_preferred_drawing_method, **kwargs)

#BLUE BUTTON 
class Blue_Button(ctk.CTkButton):
    def __init__(self, master,width = 140, height = 28,text="mybutton"):
        """Renvoie un bouton fond #3EACC3 bord #8BE4F7 selon la taille souhaitee"""
        super().__init__(master, width, height,fg_color="#3EACC3",border_color="#8BE4F7",border_width=1,text=text)

#BLACK BUTTON
class Black_Button(ctk.CTkButton):
    def __init__(self, master,width = 140, height = 28,text="mybutton"):
        """Renvoie un bouton fond #1E1E1E bord #8BE4F7 selon la taille souhaitee"""
        super().__init__(master, width, height,fg_color="#1E1E1E",border_color="#8BE4F7",border_width=1,text=text)

#right arrow nav button
class Right_Arrow_Button(ctk.CTkButton):
    """Bouton quitter selon la taille souhaitee"""
    def __init__(self, master, width = 50, height = 50, corner_radius = None, border_width = 2, border_spacing = 2, bg_color = "transparent", fg_color = "Transparent", hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", **kwargs):
        self.right_icon = ctk.CTkImage(right_arrow_icon)
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, border_width=border_width, border_spacing=border_spacing, bg_color=bg_color, fg_color=colors["button_bg"], 
                        hover_color=hover_color, border_color=border_color, text_color=text_color, text_color_disabled=text_color_disabled, 
                        background_corner_colors=background_corner_colors, round_width_to_even_numbers=round_height_to_even_numbers, 
                        round_height_to_even_numbers=round_height_to_even_numbers, text=text, font=font, textvariable=textvariable, image=self.right_icon, state=state, hover=hover, command=command, compound=compound, anchor=anchor)
        
        self.master = master

#right arrow nav button
class Left_Arrow_Button(ctk.CTkButton):
    """Bouton quitter selon la taille souhaitee"""
    def __init__(self, master, width = 50, height = 50, corner_radius = None, border_width = 2, border_spacing = 2, bg_color = "transparent", fg_color = "Transparent", hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", **kwargs):
        self.left_icon = ctk.CTkImage(left_arrow_icon)
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, border_width=border_width, border_spacing=border_spacing, bg_color=bg_color, fg_color=colors["button_bg"], 
                        hover_color=hover_color, border_color=border_color, text_color=text_color, text_color_disabled=text_color_disabled, 
                        background_corner_colors=background_corner_colors, round_width_to_even_numbers=round_height_to_even_numbers, 
                        round_height_to_even_numbers=round_height_to_even_numbers, text=text, font=font, textvariable=textvariable, image=self.left_icon, state=state, hover=hover, command=command, compound=compound, anchor=anchor)
        
        self.master = master
        

#QUIT BUTTON
class Quit_Button(ctk.CTkButton):
    """Bouton quitter selon la taille souhaitee"""
    def __init__(self, master, width = 50, height = 50, corner_radius = None, border_width = 2, border_spacing = 2, bg_color = "transparent", fg_color = None, hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", **kwargs):
        self.power_icon = ctk.CTkImage(power_icon)
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, border_width=border_width, border_spacing=border_spacing, bg_color=bg_color, fg_color=colors["button_bg"], 
                        hover_color=hover_color, border_color=colors["border"], text_color=text_color, text_color_disabled=text_color_disabled, 
                        background_corner_colors=background_corner_colors, round_width_to_even_numbers=round_height_to_even_numbers, 
                        round_height_to_even_numbers=round_height_to_even_numbers, text=text, font=font, textvariable=textvariable, image=self.power_icon, state=state, hover=hover, command=command, compound=compound, anchor=anchor)
        
        self.master = master
        

#HOME BUTTON
class Home_Button(ctk.CTkButton):
    def __init__(self, master, width = 50, height = 50, corner_radius = None, border_width = 2, border_spacing = 2, bg_color = "transparent", fg_color = None, hover_color = None, border_color = None, text_color = None, text_color_disabled = None, background_corner_colors = None, round_width_to_even_numbers = True, round_height_to_even_numbers = True, text = "", font = None, textvariable = None, image = None, state = "normal", hover = True, command = None, compound = "left", anchor = "center", **kwargs):
        """Bouton quitter selon la taille souhaitee"""
        self.home_icon = ctk.CTkImage(home_icon)
        super().__init__(master=master, width=width, height=height, corner_radius=corner_radius, border_width=border_width, border_spacing=border_spacing, bg_color=bg_color, fg_color=colors["button_bg"], 
                        hover_color=hover_color, border_color=colors["border"], text_color=text_color, text_color_disabled=text_color_disabled, 
                        background_corner_colors=background_corner_colors, round_width_to_even_numbers=round_height_to_even_numbers, 
                        round_height_to_even_numbers=round_height_to_even_numbers, text=text, font=font, textvariable=textvariable, image=self.home_icon, state=state, hover=hover, command=command, compound=compound, anchor=anchor)
        
        self.master = master

#TITLE FRAME MARS EXPLORATION
class Title_Frame(ctk.CTkFrame):
    def __init__(self, master, width = 1150, height = 200, corner_radius = 10, border_width = 2, bg_color="transparent", fg_color = colors["bg2"], border_color = colors["border"], background_corner_colors = None, overwrite_preferred_drawing_method = None, **kwargs):
        super().__init__(master, width, height, corner_radius, border_width, bg_color, fg_color, border_color, background_corner_colors, overwrite_preferred_drawing_method, **kwargs)
        self.title_label = ctk.CTkLabel(self,corner_radius=10,anchor="center",fg_color="transparent",bg_color="transparent",text="M A R S  E X P L O R A T I O N",text_color="#8BE4F7",font=("Roboto",70))
        self.title_label.pack(expand="True",padx=20,pady=20)

#BLUE TEXT LABEL
class Blue_Text_Label(ctk.CTkLabel):
    def __init__(self, master, width = 0, height = 28, corner_radius = None, bg_color = "transparent", fg_color = None, text_color = colors["text1"], text_color_disabled = None, text = "CTkLabel", font = None, image = None, compound = "center", anchor = "center", wraplength = 0, **kwargs):
        super().__init__(master, width, height, corner_radius, bg_color, fg_color, text_color, text_color_disabled, text, font, image, compound, anchor, wraplength, **kwargs)


#Class segment dans le choix du nombre de robots par type
#TODO ajout controlleur pour recup valeur du slider et changer le label attache
class Robots_Choice_Segment(Bg_Frame2):
    def __init__(self, master,robottype:str, width=800, height=100):
        """Un segment contenant nom du type, le nombre choisi et le slider pour choisir. 0<=val<=100"""
        super().__init__(master, width, height)
        self.master = master
        self.robot_type = robottype

        self.main_frame = ctk.CTkFrame(self,fg_color="transparent",bg_color="transparent")
        self.main_frame.pack(expand=True,fill="both",padx=5,pady=5)

        self.col0_frame = ctk.CTkFrame(self.main_frame,width=650,fg_color="transparent")
        self.col0_frame.grid(row=0,column=0,sticky="nw",ipadx=5,ipady=5)
        self.col1_frame = ctk.CTkFrame(self.main_frame,width=50,fg_color="transparent")
        self.col1_frame.grid(row=0,column=1,sticky="nsew")

        self.row1_frame = ctk.CTkFrame(self.main_frame,width=700,fg_color="transparent")
        self.row1_frame.grid(row=1,columnspan=2,sticky="ne")

        #ROW 0
        #Type label
        self.type_label = Blue_Text_Label(self.col0_frame,text=self.robot_type,font=("Roboto",20),fg_color="transparent",anchor="w",width=30)
        self.type_label.pack(side="left",expand=True,anchor="nw")
        
        #datasheet icon
        self.datasheet_icon = ctk.CTkImage(datasheet_icon)
        self.datasheet_label = ctk.CTkLabel(self.col0_frame,image=self.datasheet_icon,text="",fg_color="transparent",bg_color="transparent",anchor="w")
        self.datasheet_label.pack(side="left",expand=True,anchor="nw")

        #SLIDER VALUE (cote droit)
        self.slider_value = Blue_Text_Label(self.col1_frame,text="00",font=("Roboto",20))
        self.slider_value.pack(side="right",anchor="e",expand=True)


        #ROW1
        self.slider = ctk.CTkSlider(self.row1_frame,width=680,from_=0,to=100,number_of_steps=100)
        self.slider.set(0)
        self.slider.pack(expand=True,anchor="center",side="top")



class Datasheet_Table(ttk.Treeview):
    def __init__(self,master = None, class_ = "", columns = "", cursor = "", displaycolumns = None, height = 10, name = None, padding = None, selectmode = "extended", show = "headings", style = "", takefocus = None, xscrollcommand = "", yscrollcommand = ""):
        """Datasheet stlise pour afficher les caracteristiques des robots"""
        super().__init__(master,class_=class_, columns=columns, cursor=cursor, displaycolumns=displaycolumns, height=height, name=name, padding=padding, selectmode=selectmode, show=show, style=style, takefocus=takefocus, xscrollcommand=xscrollcommand, yscrollcommand=yscrollcommand)
        
        #Appliquer le style
        #Style heading
        self.style=ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview.Heading",foreground="white",background="#132022",font=("Roboto",16,"bold"),relief="flat")
        for cellname in columns:
            self.heading(cellname,text=cellname,anchor="w")
        #bg = #3EACC3
        #STYLE Tableau
        self.style.configure("Custom.Treeview",background="3EACC3",
                             foreground="white",
                             fieldbackground = "#3EACC3",
                             rowheight=30,
                             font=("Roboto",14))

        self.configure(style="Custom.Treeview")



if __name__ == "__main__":
    root = ctk.CTk()
    root.geometry("1000x800")
    root.configure(fg_color="blue")
    #test frame
    frm = Bg_Frame(root,500,500)
    frm.pack(anchor="center",expand=True)
    #title = Title_Frame(root)
    #title.pack(side="top")
    
    #seg = Robots_Choice_Segment(frm,"Exploration")
    #seg.pack(expand=True)
    
    table = Datasheet_Table(frm,columns=("Attributes","Details"))
    table.pack()
    root.mainloop()