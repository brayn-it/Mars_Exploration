from math import sqrt
import customtkinter as ctk
import uuid

# Classe de base Robot
class Robot:
    def __init__(self, pos, speed=1, robot_type="exploration", base_pos=(0,0)):
        self.id = str(uuid.uuid4())  # Identifiant unique
        self.x = pos[0]
        self.y = pos[1]
        self.speed = speed
        self.batterie = 100  # Pourcentage
        self.usure = 0       # Pourcentage
        self.type = robot_type
        self.etat = "idle"  # idle, mission, return, oo (Out of Order)
        self.base_pos = base_pos
        self.mission_pos = None
        self.message = ""
        self.prev_state = None #Pour stocker l'etat precedent
        self.target_robot = None

    def move(self):
        """Déplacement vers la mission ou retour à la base"""
        if self.etat == "mission" and self.mission_pos:
            target_x, target_y = self.mission_pos
            self._step(target_x, target_y)
            if self._reach_target(target_x, target_y):
                self.etat = "return"
                self.mission_pos = self.base_pos
                self.prev_state = "mission"
        elif self.etat == "return":
            target_x, target_y = self.base_pos
            self._step(target_x, target_y)
            if self._reach_target(target_x, target_y):
                self.etat = "idle"
                self.prev_state = "return"
        if (self.etat == "oo" and self.batterie>0) or (self.etat == "oo" and self.usure<100):
            self.speed = 2
            self.etat = self.prev_state
            self.prev_state = "oo"

    def _reach_target(self, target_x, target_y):
        """Vérifie si la position cible est atteinte"""
        return abs(self.x - target_x) < self.speed and abs(self.y - target_y) < self.speed

    def _step(self, target_x, target_y):
        """Calcul de la direction et déplacement"""
        dx = target_x - self.x
        dy = target_y - self.y
        distance = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        self.x += (dx / distance) * self.speed
        self.y += (dy / distance) * self.speed
        self._consommer_energie()

    def _consommer_energie(self):
        """Consommer batterie et augmenter usure"""
        self.batterie -= 0.1
        self.usure += 0.5
        self.check_batterie()
        self.check_usure()

    def get_position(self):
        """Retourne la position actuelle du robot"""
        return self.x, self.y

    def set_target(self, target_robot):
        """Définit le robot cible à suivre"""
        self.target_robot = target_robot

    def follow_target(self):
        """Met à jour la mission pour suivre la cible"""
        if self.target_robot:
            self.mission_pos = self.target_robot.get_position()

    def set_mission(self,mission_pos):
        """Assigne une position de mission"""
        self.mission_pos = mission_pos

    def start_mission(self):
        self.etat = "mission"
        self.move()

    def send_message(self, contenu):
        """Envoyer un message à la base"""
        if contenu:
            self.message = f"Robot {self.id}: {contenu}"

    #def send_message(self):
        #return True
    
    def check_batterie(self):
        """Vérifie si la batterie est critique et diminue la vitesse de 20% tous les 5% de perte"""

        if self.batterie < 20:
            self.send_message("Batterie faible !")
        if self.batterie == 20:
            self.speed = self.speed * 0.8
        if self.batterie == 15:
            self.speed = self.speed * 0.8
        if self.batterie == 10:
            self.speed = self.speed * 0.8
        if self.batterie == 5:
            self.speed = self.speed * 0.8
        if self.batterie == 0:
            self.speed = 0
            self.prev_state = self.etat
            self.etat = "oo"
        
    def check_usure(self):
        """Vérifie si l'usure est critique"""
        if self.usure > 80:
            self.send_message("Usure critique !")
        if self.usure == 90:
            self.speed = self.speed * 0.7
        if self.usure == 100:
            self.speed = 0
            self.prev_state = self.etat
            self.etat = "oo"
    
    def affiche_info(self):
        """Affiche les informations du robot"""
        print(f"Robot id : {self.id}")
        print(f"Battery : {self.batterie}")
        print(f"Position : {self.x,self.y}")
        print(f"Usure : {self.usure}")
        print(f"State : {self.etat}")
        
#AJOUT : Diminution de 20% de speed tous les 5% de perte de batterie a partir de 20% ; puis 0 speed a 0%
# Diminution de 30% de speed a 90% d'usure puis 0 speed a 100%
#Etat 'oo' Out of Order quand batterie 0% ou usure 100% 
#Memorisation de l'etat precedent dans prev_state en cas de reprise apres reparation

if __name__=="__main__":
    root = ctk.CTk()
    rob = Robot((0,0),2,"Exploration")
    rob.set_mission((500,500))
    rob.start_mission()
    while(1):
        root.after(50,rob.move())
        rob.affiche_info()
    root.mainloop()