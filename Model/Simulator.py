import PIL.Image
import customtkinter as ctk
import PIL.ImageTk
import customtkinter as ctk
import PIL
import rasterio
import os
import random
import time


from Model.Robot import Robot
from Model.ExplorationRobot import ExplorationRobot
from Model.GeologicalRobot import GeologicalRobot
from Model.RepairRobot import RepairRobot
from Model.CarrierRobot import CarrierRobot
from Model.RobotGroup import RobotGroup

from Model.Module import Module
from Model.RepairModule import *
from Model.BatteryModule import *
from Model.CollectModule import *
from Model.CentralBase import *

#PAS DE LIMITE CARTE MOLA DE TRES HAUTE RESOLUTION
PIL.Image.MAX_IMAGE_PIXELS = None

class Simulator():
    def __init__(self,canvas,root):
        """Gère les intéractions entre toutes les entités et effectue l'avancement de la simulation"""
        self.root = root
        #self.canvas = ctk.CTkCanvas(root, width=800, height=600, bg="black")
        #self.canvas.pack(fill="both", expand=True)
        self.canvas = canvas

        #Repertoire des tuiles
        self.tile_dir = "tiles_tiff"
        self.tile_size = 1024
        #///////POUR LA CARTE////////////
        #self.original_map = PIL.Image.open("BD/mars_mola_map.tif")
        #self.original_map = PIL.Image.open("BD/mola_color_N-30_270.png")

        self.echelle = 1.0
        self.offset_x = 0
        self.offset_y = 0

        # Chargement dynamique des tuiles
        self.tiles = {}
        #self.charger_tuile(223)
        self.render_tuile()
        #self.centrer_carte()
        #self.map_render()
        #self.creer_boutons()

        #Tous les robots dispo
        self.robots = []
        self.groupes = []
        self.base = None
        
        self.state = "running" #pause, #stop

        # Boutons pour ajouter des robots
        #add_button = ctk.CTkButton(root, text="Ajouter Robot", command=self.add_robot)
        #add_button.pack(side="left", padx=5)

        # Bouton pour afficher l'état de la base
        #base_button = ctk.CTkButton(root, text="Afficher Base", command=self.afficher_base)
        #base_button.pack(side="left", padx=5)

        # Placement de la base
        #self.canvas.bind("<Button-1>", self.place_base)

        # Mise à jour de la simulation
        self.start_simulation()
        self.update()
    

    def place_base(self, event):
        """Placer la base centrale sur la carte"""
        if not self.base:
            self.base = CentralBase(event.x, event.y)
            print(f"Base centrale placée à {event.x}, {event.y}")
            self.canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10, fill="yellow")
    
    def create_group(self):
        """Créer un groupe de robots"""
        nom = f"Groupe_{len(self.groupes) + 1}"
        groupe = RobotGroup(nom)
        # Ajouter quelques robots pour le test
        for robot in self.robots[:4]:
            groupe.add_robot(robot)
        self.groupes.append(groupe)
        print(f"Nouveau groupe créé : {nom}")

    def start_mission_group(self):
        """Lancer une mission collective pour un groupe"""
        if self.groupes:
            groupe = self.groupes[0]  # Choisir le premier groupe pour le test
            mission_pos = (random.randint(50, 750), random.randint(50, 550))
            groupe.assign_mission(mission_pos)
            groupe.start_mission()
            print(f"Mission collective lancée pour {groupe.nom}")

    def add_robot(self,robot):
        """Ajouter un robot à la base"""
        if self.base:
            x, y = self.base.position
            self.robots.append(robot)
            print(f"Robot {robot.id} ajouté à la base")

    def afficher_base(self):
        """Afficher les informations de la base centrale"""
        if self.base:
            print(f"Base Centrale : Position {self.base.position}, Budget ${self.base.budget}")
            print(f"Modules : {self.base.modules}")

    def update(self):
        """Mettre à jour la simulation"""
        self.canvas.delete("simulation")
        
        # Affichage de la base
        if self.base:
            self.base_render(self.base)
        self.check_global_behavior()
        # Déplacement et affichage des robots
        for robot in self.robots:
            robot.move()
            self.robot_render(robot)

        # Mise à jour de la boucle
        self.root.after(50, self.update)

    def send_message(self,message):
        """Faire apparaitre le message dans la zone de message"""
        print(message)

    #/////////COMPORTEMENTS DES ROBOTS/////////////////////////

    def check_general_behavior(self,robot:Robot):
        if robot.batterie in (20,15,10,5,0):
            self.send_message(f"R-{robot.id} : Low battery !")
        if robot.usure in (80,85,90,95,100):
            self.send_message(f"R-{robot.id} : Damage is high!")
        #if robot.send_message():
            #self.send_message(robot.message)

    def check_exploration_behavior(self,robot:ExplorationRobot):
        pass
        #Revele carte

    def check_carrier_behavior(self,robot:CarrierRobot):
        """Quand le mule a atteint sa cible pour rechargement ou reparation ou les deux"""
        if robot.target_robot and robot._reach_target(robot.mission_pos[0],robot.mission_pos[1]):
            if robot.target_robot.usure>90:
                if robot.repair_module.capacity > 1:
                    robot.repair_module.repair_robot(robot.target_robot)
            if robot.target_robot.battery<20:
                if robot.repair_module.capacity > 1:
                    robot.repair_module.recharge_robot(robot.target_robot)

    def check_global_behavior(self):
        """Comportement de tout le groupe """
        for group in self.groupes:
            for robot in group.robots:
                self.check_general_behavior(robot)
                if isinstance(robot,ExplorationRobot):
                    self.check_exploration_behavior(robot)
                if isinstance(robot,CarrierRobot):
                    self.check_carrier_behavior(robot)
                if robot.usure == 90:
                    group.assign_repair_mission(robot)
                    group.start_repair_mission()
            
    def find_robot_in_group(self,group,type):
        for robot in group:
            if robot.type == type:
                return robot


    #///////////RENDERING///////////////////
    def base_render(self,base:CentralBase):
        x, y = base.position
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="yellow",tags="simulation")

    def robot_render(self,robot):
        if isinstance(robot,ExplorationRobot):
            self.canvas.create_oval(robot.x - 5, robot.y - 5, robot.x + 5, robot.y + 5, fill="blue",tags="simulation")
        if isinstance(robot,GeologicalRobot):
            self.canvas.create_polygon(robot.x - 5, robot.y - 5, robot.x + 5, robot.y + 5, robot.x, robot.y + 5, fill="green",tags="simulation")
        if isinstance(robot,RepairRobot):
            self.canvas.create_polygon(robot.x, robot.y - 5, robot.x + 5, robot.y + 5, robot.x -5, robot.y + 5, fill="orange",tags="simulation")
        if isinstance(robot,CarrierRobot):
            self.canvas.create_rectangle(robot.x -5, robot.y - 5, robot.x + 5, robot.y + 5, fill="black",tags="simulation")
        
        self.canvas.create_text(robot.x, robot.y - 10, text=robot.id, fill="white",tags="simulation")

    # Chargement et affichage de la carte
    def map_render(self):
        # Redimensionner l'image en fonction de l'échelle
        #width = int(self.original_map.width * self.echelle)
        #height = int(self.original_map.height * self.echelle)
        #self.image_resized = self.original_map.resize((width,height),PIL.Image.Resampling.NEAREST)
        #self.tk_image = PIL.ImageTk.PhotoImage(self.image_resized)

        # Dessiner l'image sur le canvas
        self.canvas.delete("all")
        #self.canvas.create_image(self.offset_x, self.offset_y, anchor=ctk.NW, image=self.tk_image)
        #self.charger_tuiles_visibles()
        self.render_tuile()
        
        # Afficher les robots
        #self.dessiner_robots()
        #self.afficher_echelle()

    #Création des boutons de contrôle
    def creer_boutons(self):
        """Créer les boutons pour le zoom et le déplacement."""
        self.btn_frame =ctk.CTkFrame(self.frame)
        self.btn_frame.place(relx=0.1,rely=0.7)

        # Boutons de zoom
        self.zoom_in_btn =ctk.CTkButton(self.btn_frame, text="+", command=lambda: self.zoom(1.2))
        self.zoom_in_btn.pack(side="left", padx=2)

        self.zoom_out_btn =ctk.CTkButton(self.btn_frame, text="-", command=lambda: self.zoom(0.8))
        self.zoom_out_btn.pack(side="left", padx=2)

        # Boutons de déplacement
        self.move_left_btn =ctk.CTkButton(self.btn_frame, text="←", command=lambda: self.move(-self.tile_size // 2, 0))
        self.move_left_btn.pack(side="left", padx=2)

        self.move_right_btn =ctk.CTkButton(self.btn_frame, text="→", command=lambda: self.move(self.tile_size // 2, 0))
        self.move_right_btn.pack(side="left", padx=2)

        self.move_up_btn =ctk.CTkButton(self.btn_frame, text="↑", command=lambda: self.move(0, -self.tile_size // 2))
        self.move_up_btn.pack(side="left", padx=2)

        self.move_down_btn =ctk.CTkButton(self.btn_frame, text="↓", command=lambda: self.move(0, self.tile_size // 2))
        self.move_down_btn.pack(side="left", padx=2)


    #///////////POUR LA CARTE////////////////

    def charger_tuile(self, tile_id):
        """Charge une tuile depuis un fichier TIFF."""
        try:
            tile_path = f"{self.tile_dir}/tile_{tile_id}.tif"
            with rasterio.open(tile_path) as src:
                # Lire l'image en tant que tableau
                image = PIL.Image.fromarray(src.read(1), mode="L")
                return image
        except Exception as e:
            print(f"Erreur de chargement de la tuile {tile_id}: {e}")
            return None
        
    def redimensionner_tuile(self, image):
        """Redimensionner l'image en fonction de l'échelle actuelle."""
        taille = int(self.tile_size * self.echelle)
        image = image.resize((taille, taille))
        return PIL.ImageTk.PhotoImage(image)
    
    def render_tuile(self):
        image_tk = self.redimensionner_tuile(self.charger_tuile(223))
        self.canvas.create_image(0, 0, anchor=ctk.NW, image=image_tk,tags="tuile")
        self.canvas.image = image_tk
    
    def charger_tuiles_visibles(self):
        """Charge les tuiles visibles en fonction de la position actuelle."""
        self.canvas.delete("tile")  # Effacer le canvas avant de redessiner

        # Calcul du nombre de tuiles nécessaires
        largeur_canvas = self.canvas.winfo_width()
        hauteur_canvas = self.canvas.winfo_height()

        nb_tuiles_x = int((largeur_canvas / (self.tile_size * self.echelle)) + 2)
        nb_tuiles_y = int((hauteur_canvas / (self.tile_size * self.echelle)) + 2)

        # Calcul des indices de tuiles à afficher
        x_start = int(-self.offset_x / (self.tile_size * self.echelle))
        y_start = int(-self.offset_y / (self.tile_size * self.echelle))

        for j in range(nb_tuiles_y):
            for i in range(nb_tuiles_x):
                tile_id = (y_start + j) * 100 + (x_start + i)

                if tile_id not in self.tiles:
                    image = self.charger_tuile(tile_id)
                    if image:
                        self.tiles[tile_id] = image

                if tile_id in self.tiles:
                    image_tk = self.redimensionner_tuile(self.tiles[tile_id])
                    # Calcul correct des coordonnées en fonction de l'offset
                    x_affiche = (x_start + i) * self.tile_size * self.echelle + self.offset_x
                    y_affiche = (y_start + j) * self.tile_size * self.echelle + self.offset_y
                    self.canvas.create_image(x_affiche, y_affiche, image=image_tk)
                    self.canvas.image = image_tk
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

        print(self.tiles)

    def centrer_carte(self):
        """Calculer l'offset pour centrer la carte au démarrage."""
        largeur_canvas = self.canvas.winfo_width()
        hauteur_canvas = self.canvas.winfo_height()

        # Calcul de l'offset pour centrer la carte
        self.offset_x = (largeur_canvas - self.tile_size * self.echelle) / 2
        self.offset_y = (hauteur_canvas - self.tile_size * self.echelle) / 2
        
    def zoom(self, facteur):
        """Zoom qui conserve l'ancrage"""
        # Coordonnées du centre de l'écran avant zoom
        centre_x = self.canvas.winfo_width() // 2
        centre_y = self.canvas.winfo_height() // 2

        # Coordonnées réelles au centre avant zoom
        centre_reel_x = (centre_x - self.offset_x) / self.echelle
        centre_reel_y = (centre_y - self.offset_y) / self.echelle

        # Appliquer le facteur de zoom
        self.echelle *= facteur

        # Coordonnées après zoom pour recentrer
        new_offset_x = centre_x - centre_reel_x * self.echelle
        new_offset_y = centre_y - centre_reel_y * self.echelle

        # Mettre à jour l'offset pour garder le centre fixe
        #self.offset_x = self.offset_x*self.echelle
        #self.offset_y = self.offset_y*self.echelle

        #self.charger_tuiles_visibles()

    def deplacer(self, dx, dy):
        """Déplacer la vue sur la carte."""
        # Appliquer le déplacement
        self.offset_x += dx
        self.offset_y += dy

        # Recalcul de l'offset pour garder l'ancrage correct
        #self.offset_x = centre_x - centre_reel_x * self.echelle
        #self.offset_y = centre_y - centre_reel_y * self.echelle

        #self.charger_tuiles_visibles()

    #/////////////FIN CARTE///////////////////////////////////

    def start_simulation(self):
        self.base = CentralBase(100,100)
        self.add_robot(ExplorationRobot(self.base.position,self.base.position))
        self.add_robot(GeologicalRobot(self.base.position,self.base.position))
        self.add_robot(CarrierRobot(self.base.position,self.base.position))
        self.add_robot(RepairRobot(self.base.position,self.base.position))

        self.create_group()

        self.groupes[0].assign_exploration_mission((500,500))
        self.groupes[0].start_exploration_mission()

        self.root.after(2000)
        
        self.groupes[0].assign_geological_mission((500,500))
        self.groupes[0].start_geological_mission()

if __name__=="__main__":
    root = ctk.CTk()
    root.geometry("1280x800")
    sim = Simulator()

    #////////Init simulation//////


    #sim.run()

    root.mainloop()