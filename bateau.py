class Bateau:
    def __init__(self, nom : str):
        self.nom = nom


class BlackPearl(Bateau):
    def __init__(self, nom, longeur : int = 5):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        return self.longeur

    @property
    def getNom(self) -> str:
        return "Black Pearl"

class QueenAnneRevenge(Bateau):
    def __init__(self, nom: str, longeur : int = 4):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        return self.longeur

    @property
    def getNom(self) -> str:
        return "Queen Anne's Revenge"


class SilentMary(Bateau):
    def __init__(self, nom, longeur : int = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        return self.longeur

    @property
    def getNom(self) -> str:
        return "Silent Mary"


class HmsIntercepteur(Bateau):
    def __init__(self, nom, longeur : int = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        return self.longeur

    @property
    def getNom(self) -> str:
        return "HMS Intercepteur"


class TheDyingGull(Bateau):
    def __init__(self, nom, longeur : int = 2):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        return self.longeur

    @property
    def getNom(self) -> str:
        return "The Dying Gull"
