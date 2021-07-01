from typing import DefaultDict
import math



class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @property
    def Afficher (self):
        print('POINT(%d,%d)' % (self.x,self.y))

class Cercle(Point):
    def __init__(self,centre=None,rayon=None):
        super().__init__()
        self.centre=centre
        self.rayon=rayon
    @property
    def getPerimetre (self):
        return (2*math.pi*self.rayon)
    def getSurface(self):
        return (math.pi*self.rayon**2)
    
    


  