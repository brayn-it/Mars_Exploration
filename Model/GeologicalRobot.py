from Model.Robot import *

# Classe Robot Géologique
class GeologicalRobot(Robot):
    def __init__(self, pos, base_pos):
        super().__init__(pos, 2, "geological", base_pos)
        self.cout = 500

    def collecter_echantillon(self):
        self.envoyer_message("Échantillon collecté et analysé.")