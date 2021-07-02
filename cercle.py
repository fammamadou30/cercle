from typing import DefaultDict
import math

#PARTIE A
#Création de la classe Point
class Point:
    #Constructeur de la classe Point
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    #Methode Afficher() de la classe Point
    def Afficher (self):
        print('POINT(%d,%d)' % (self.x,self.y))

#Création de la classe Cercle
class Cercle(Point):
    def __init__(self,centre=Point,rayon=float):
        super().__init__()
        self.centre=centre
        self.rayon=rayon
    #Création des Methodes de la classe Cercle
    @property
    def getPerimetre (self):
        return (2*math.pi*self.rayon)
    def getSurface(self):
        return (math.pi*(self.rayon**2))
    def Afficher(self):
        print('CERCLE(%d,%d,%d)' % (self.centre.x,self.centre.y,self.rayon))
    
#PARTIE B
#Création de la classe Cylindre
class Cylindre(Cercle):
    def __init__(self,cercleA=Cercle,hauteur=float):
        super().__init__()
        self.cercleA=cercleA
        self.hauteur=hauteur
    #Création methode getVolume() permettant de retourner le volume du cylindre
        def getVolume(self):
            return math.pi*(self.rayon**2)*self.hauteur

A=Point(2,4)
A.Afficher
cercleDeCentreA=Cercle(A,5)
cercleDeCentreA.Afficher


  