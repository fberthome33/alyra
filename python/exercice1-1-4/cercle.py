import math;


class Cercle:

    def __init__(self, rayon):
        self.rayon = rayon

    def perimetre(self):
        return 2* math.pi * self.rayon;

    def aire(self):
        return math.pi * pow(self.rayon, 2);
