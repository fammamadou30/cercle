from typing import DefaultDict
from math import *

#PARTIE A
#Création de la classe Point
class Point:
    x : float
    y : float
    #Constructeur de la classe Point
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    #Methode afficher() de la classe Point
    def afficher (self):
        print('POINT(%d,%d)' % (self.x,self.y))

#Création de la classe Cercle
class Cercle:
    centre : Point
    rayon : float
    def __init__(self,centre:Point,rayon:float):
        self.centre=centre
        self.rayon=rayon
    #Création des Methodes de la classe Cercle
    @property
    def getPerimetre (self):
        return (2*pi*self.rayon)
    def getSurface(self):
        return (pi*(self.rayon**2))
    def afficher(self):
        print('CERCLE(%d,%d,%d)' % (self.centre.x,self.centre.y,self.rayon))
    def appartient(self, p:Point):
        if(sqrt(pow(self.centre.x - p.x, 2) + pow(self.centre.y - p.y, 2)) == self.rayon):
            return True
        else:
            return False
    def afficher(self):
        print("Le centre du cercle a pour abcisse x = " + str(self.centre.x) + ', ordonnee y = ' + str(self.centre.y) + ' et le rayon du cercle est de r = ' +  str(self.rayon) )
#PARTIE B
#Création de la classe Cylindre
class Cylindre(Cercle):
    def __init__(self, centre, rayon, hauteur):
        Cercle.__init__(self, centre, rayon)
        self.hauteur=hauteur
    #Création methode getVolume() permettant de retourner le volume du cylindre
    def getVolume(self):
        return pi*pow(self.rayon, 2)*self.hauteur
#Fonction principale main
if __name__ == '__main__':
    print("TP PYTHON DE MAMADOU FAM\n")
    x=float(input("Entre l'abscisse du centre de ton cercle: "))
    y=float(input("Entre l'ordonnée du centre de ton cercle: "))
    A=Point(x, y)

    r=float(input("Entre le rayon du cercle: "))
    C=Cercle(A, r)
    C.afficher()
    print("Le périmètre de ton cercle est: %d m" % C.getPerimetre)
    print("Sa surface est: %d m2" % C.getSurface())

    print("Vérifions l'appartenance d'un point à votre cercle \n\n")
    a=float(input("Entre l'abscisse de ce point: "))
    b=float(input("Entre l'ordonnée de ce point: "))
    B=Point(a, b)
    if (C.appartient(B)==True):
        print("le point appartient au cercle")
    else:
        print("Le point n'appartient pas au cercle")

    print("Un cylindre est un cercle avec un hauteur \n\n")
    h=float(input("Entre la hauteur de ton cylindre :"))
    CylindreA=Cylindre(A, r, h)
    print("Le volume de ton  cylindre est: %d m3" % CylindreA.getVolume() )


  