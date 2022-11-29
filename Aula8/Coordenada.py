from dataclasses import replace

def Erro1(Exception):
    raise "Numero de argumentos errado: 2"


class Coordenada:
    def __init__(self, coord = (0,0)):
        if(type(coord) != tuple):
            raise Erro1
        self.coordenada = coord

    def __str__(self):
        return f'{self.coordenada}'

    def distancia(self, coordenada2):
        c1 = list(str(self.coordenada).replace("(", "").replace(")","").split(","))
        c2 = list(str(coordenada2).replace("(", "").replace(")","").split(","))
        distancia = ((float(c1[0]) - float(c2[0]))**2 + (float(c1[1]) - float(c2[1]))**2)**0.5
        return distancia

