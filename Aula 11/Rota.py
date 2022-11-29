from Coordenada import Coordenada
from copy import deepcopy
import random

class Rota:
    
    def __init__(self):
        self.coords = []
    
    def addCoord(self, coord):
        self.coords.append(coord)
    
    def comprimento(self):
        comprimento = 0
        for c in range(1,len(self.coords)):
            comprimento += self.coords[c].distancia(self.coords[c-1])
        comprimento += self.coords[-1].distancia(self.coords[0])
        return comprimento

    def copy(self):
        rota = deepcopy(self)
        return (rota)

    def __str__(self):
        strRota = ""
        for a in self.coords:
            strRota += str(a)
            strRota += "->"
        strRota += str(self.coords[0])
        return strRota

    def shuffle(self):
        random.shuffle(self.coords)
    
    def getcoords(self):
        return self.coords

    def otimiza(self):
        listaFinal = []
        listaOriginal = self.getcoords()
        listaFinal.append(listaOriginal[0])
        
        for i in range(1,len(listaOriginal)):
            min_dist = -1
            coodAlvo = Coordenada()
            for c in range(i, len(listaOriginal)):
                if(min_dist < 0):
                    min_dist = listaOriginal[i-1].distancia(listaOriginal[c])
                    coodAlvo = listaOriginal[c]
                else:
                    if(listaOriginal[i-1].distancia(listaOriginal[c]) < min_dist):
                        coodAlvo = listaOriginal[c]
            listaFinal.append(coodAlvo)
        
        for a in range(len(self.coords)):
            self.coords[a] = listaFinal[a]
    
    def randomCoords(self, size = 1, maxValueCoord = 100):
        for i in range(size):
            n1 = random.randint(0, maxValueCoord)
            n2 = random.randint(0, maxValueCoord)
            coordenada = Coordenada((n1,n2))
            self.addCoord(coordenada)
