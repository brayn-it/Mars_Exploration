from Model.Robot import *

# Classe Robot d'Exploration
class ExplorationRobot(Robot):
    def __init__(self, pos, base_pos):
        super().__init__(pos, 3, "exploration", base_pos)
        self.cout = 750

    def discover_map(self):
        self.envoyer_message("Génération de carte locale.")