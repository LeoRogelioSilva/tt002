from Coordenada import Coordenada
from copy import deepcopy
import random

class Rota:
    
    def __init__(self):
        self.listCoordenadas = []
    
    def addCoord(self, coord):
        self.listCoordenadas.append(coord)
    
    def comprimento(self):
        comprimento = 0
        for c in range(1,len(self.listCoordenadas)):
            comprimento += self.listCoordenadas[c].distancia(self.listCoordenadas[c-1])
        comprimento += self.listCoordenadas[-1].distancia(self.listCoordenadas[0])
        return comprimento

    def copy(self):
        rota = deepcopy(self)
        return (rota)

    def __str__(self):
        strRota = ""
        for a in self.listCoordenadas:
            strRota += str(a)
            strRota += "->"
        strRota += str(self.listCoordenadas[0])
        return strRota

    def shuffle(self):
        random.shuffle(self.listCoordenadas)
    
    def getListCoordenadas(self):
        return self.listCoordenadas

    def otimiza(self):
        listaFinal = []
        listaOriginal = self.getListCoordenadas()
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
        
        for a in range(len(self.listCoordenadas)):
            self.listCoordenadas[a] = listaFinal[a]
