class Bateau:
    def __init__(self, nom : str):
        """Nom du bateau"""
        self.nom = nom

#Herite de la classe Bateau
class BlackPearl(Bateau):
    def __init__(self, nom, longeur : int = 5):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        """getter qui permet d'obtenir la longeur du bateau"""
        return self.longeur

    @property
    def getNom(self) -> str:
        "getter qui permet d'obtenir le nom du bateau"
        return "Black Pearl"

#Herite de la classe Bateau
class QueenAnneRevenge(Bateau):
    def __init__(self, nom: str, longeur : int = 4):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        """getter qui permet d'obtenir la longeur du bateau"""
        return self.longeur

    @property
    def getNom(self) -> str:
        "getter qui permet d'obtenir le nom du bateau"
        return "Queen Anne's Revenge"

#Herite de la classe Bateau
class SilentMary(Bateau):
    def __init__(self, nom, longeur : int = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        """getter qui permet d'obtenir la longeur du bateau"""
        return self.longeur

    @property
    def getNom(self) -> str:
        "getter qui permet d'obtenir le nom du bateau"
        return "Silent Mary"

#Herite de la classe Bateau
class HmsIntercepteur(Bateau):
    def __init__(self, nom, longeur : int = 3):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        """getter qui permet d'obtenir la longeur du bateau"""
        return self.longeur

    @property
    def getNom(self) -> str:
        "getter qui permet d'obtenir le nom du bateau"
        return "HMS Intercepteur"

#Herite de la classe Bateau
class TheDyingGull(Bateau):
    def __init__(self, nom, longeur : int = 2):
        Bateau.__init__(self, nom)
        self.longeur = longeur

    @property
    def length(self) -> int:
        """getter qui permet d'obtenir la longeur du bateau"""
        return self.longeur

    @property
    def getNom(self) -> str:
        "getter qui permet d'obtenir le nom du bateau"
        return "The Dying Gull"

t= TheDyingGull("The Dying Gull")
t.length
t.getNom

h = HmsIntercepteur('HMS Intercepteur')
h.getNom
h.length

s = SilentMary("Silent Mary")
s.getNom
s.length

b = BlackPearl('Black Pearl')
b.getNom
b.length

q= QueenAnneRevenge("Queen Anne's Revenge")
q.getNom
q.length