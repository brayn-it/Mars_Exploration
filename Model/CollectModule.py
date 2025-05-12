from Model.Module import *

# Module de Récolte
class CollectModule(Module):
    def __init__(self):
        super().__init__("recolte", 2)
        self.sample = []

    def add_sample(self, echantillon):
        """Ajouter un échantillon"""
        if len(self.sample) < 2:
            self.sample.append(echantillon)
            print(f"Échantillon ajouté : {echantillon}")
            return True
        print("Module de récolte plein.")
        return False
    
    def empty(self):
        """Vider le module à la base"""
        self.sample = []
        print("Module de récolte vidé à la base.")