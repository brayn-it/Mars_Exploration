from Model.Robot import *

# Classe de base Module
class Module:
    def __init__(self, module_type, capacity):
        self.type = module_type
        self.capacity = capacity
        self.state = "available"

    def use(self):
        """Utiliser le module"""
        if self.capacity > 0:
            self.capacity -= 1
            print(f"Module {self.type} utilisé. Capacité restante : {self.capacity}")
            if self.capacity == 0:
                self.state = "unavailable"
            return True
        print(f"Module {self.type} unavailable.")
        return False

    def recharge(self, montant):
        """Recharger le module à la base"""
        self.capacity += montant
        self.state = "disponible"
        print(f"Module {self.type} rechargé. Nouvelle capacité : {self.capacity}")