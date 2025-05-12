from Model.BatteryModule import *
from Model.RepairModule import *
from Model.CollectModule import *

class CentralBase:
    def __init__(self, x, y):
        self.position = (x, y)
        self.modules = {
            "battery": [],
            "repair": [],
            "collect": []
        }
        self.outils = {"repair": 5, "collect": 5}  # Outils disponibles à la base
        self.budget = 1000000  # Budget initial en dollars

    def ajouter_module(self, module):
        """Ajouter un module au stock"""
        if isinstance(module, BatteryModule):
            self.modules["battery"].append(module)
        elif isinstance(module, RepairModule):
            self.modules["repair"].append(module)
        elif isinstance(module, CollectModule):
            self.modules["collect"].append(module)
        print(f"Module {module.type} ajouté à la base.")

    def fournir_module(self, module_type):
        """Fournir un module à un robot"""
        if self.modules[module_type]:
            return self.modules[module_type].pop()
        print(f"Aucun module de type {module_type} disponible.")
        return None

    def recharger_robot(self, robot):
        """Recharger un robot contre 5 000 $"""
        if robot.battery < 100 and self.budget >= 5000:
            robot.battery = 100
            self.budget -= 5000
            print(f"Robot {robot.id} rechargé. Budget restant : ${self.budget}")
        else:
            print(f"Rechargement impossible pour le robot {robot.id}.")

    def reparer_robot(self, robot):
        """Réparer un robot contre 50 000 $"""
        if robot.usure > 0 and self.budget >= 50000:
            robot.usure = 0
            self.budget -= 50000
            print(f"Robot {robot.id} réparé. Budget restant : ${self.budget}")
        else:
            print(f"Réparation impossible pour le robot {robot.id}.")

    def vider_module(self, module):
        """Vider le module de récolte à la base"""
        if isinstance(module, CollectModule):
            module.vider()
            print("Module de récolte vidé avec succès.")

    def afficher_etat(self):
        """Afficher l'état des modules et du budget"""
        print(f"Base Centrale à la position {self.position}")
        print(f"Budget actuel : ${self.budget}")
        print("Modules disponibles :")
        for module_type, liste_modules in self.modules.items():
            print(f"- {module_type.capitalize()} : {len(liste_modules)} unités")
        print("Outils disponibles :")
        for outil, quantite in self.outils.items():
            print(f"- {outil.capitalize()} : {quantite} unités")