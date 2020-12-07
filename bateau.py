class Bateau:
    def __init__(self, nom):
        self.nom = nom


class BlackPearl(Bateau):
    def __init__(self, nom, longeur=5):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur

    @property
    def getNom(self):
        return "Black Pearl"


class QueenAnneRevenge(Bateau):
    def __init__(self, nom: str, longeur=4):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur

    @property
    def getNom(self):
        return "Queen Anne's Revenge"


class SilentMary(Bateau):
    def __init__(self, nom, longeur=3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur

    @property
    def getNom(self):
        return "Silent Mary"


class HmsIntercepteur(Bateau):
    def __init__(self, nom, longeur=3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur

    @property
    def getNom(self):
        return "HMS Intercepteur"


class TheDyingGull(Bateau):
    def __init__(self, nom, longeur=2):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self):
        return self.longeur

    @property
    def getNom(self):
        return "The Dying Gull"
