import random
from Rota import Rota
from Coordenada import Coordenada
import time
from matplotlib import pyplot

# Ainda não é para entregar. Em grupo de 3 pessoas.
# Vai ser pedido para entregar futuramente, junto
# com o conteúdo da aula 11.


class Otimizador:
    # Este é o construtor do otimizador. Você pode adicionar código aqui
    # se julgar necessário.
    def __init__(self):
        self.plt = pyplot

    # Este método de otimização já está implementado.
    # Toda vez que o comprimento for atualizado para um valor menor, é
    # necessário salvar o comprimento e o tempo gasto na função
    # para fazer o gráfico.
    # Ao final da execução, é necessário usar o matplotlib (pyplot)
    # para gerar o gráfico (comprimento X tempo).
    # Deve ser feito o mesmo para a função de otimização 'aleatório'
    # e 'otimizadorGrupo1'
    # As três séries temporais devem ser salvas em um mesmo gráfico,
    # conforme figuras 'Resultado_10x.py'
    # Seu grupo pode adicionar código nesta função se julgar necessário.
    # O mesmo para os outros dois otimizadores.
    # A linha do gráfico referente ao 'SingleSwap' deve estar em preto.
    # A linha do gráfico referente ao 'Aleatório' deve estar em verde.
    # A linha do gráfico referente ao 'otimizadorGrupo1' deve estar em azul
    # e deve ser mais grossa que a linha dos outros algoritmos.
    # Todas as linhas devem iniciar no tempo zero e terminar no tempo final.
    def singleSwap(self, rota: Rota, time_ms: int):
        timeArr = []
        comprimentoArr = []
        # Inicia a partir de uma rota não otimizada
        rota.shuffle()
        # Tempo de entrada na função.
        tin = round(time.time() * 1000)
        # Tempo gasto na função.
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            # atualiza delta
            delta_ms = round(time.time() * 1000) - tin
            size_rota = len(rota.coords)
            pos1 = random.randrange(0, size_rota)
            pos2 = random.randrange(0, size_rota)
            swap(rota, pos1, pos2)
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
            else:
                # desfaz o swap
                swap(rota, pos1, pos2)
            timeArr.append(delta_ms)
            comprimentoArr.append(minComprimento)
        resp = {
            "x": timeArr,
            "y": comprimentoArr,
            "min": minComprimento,
            "color": "#f00",
            "label" : "Swap",
            "linewidth" : 3
        }
        return resp


    def aleatorio(self, rota: Rota, time_ms: int):
        timeArr = []
        comprimentoArr = []
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            rotaAux = rota.copy()
            rotaAux.shuffle()
            if rotaAux.comprimento() < minComprimento:
                rota.coords = rotaAux.coords
                minComprimento = rota.comprimento()
            timeArr.append(delta_ms)
            comprimentoArr.append(minComprimento)
        resp = {
            "x": timeArr,
            "y": comprimentoArr,
            "min": minComprimento,
            "color": "#0f0",
            "label" : "Aleatorio",
            "linewidth" : 3
        }
        return resp

    # Aqui você deve usar sua criatividade e propor um algoritmo de
    # otimização. O algoritmo deixado é apenas um exemplo.
    # Ao fixar um label para o seu grupo
    # dê um nome para o seu grupo que o diferencie dos demais.
    # Veja a Figura Resultado_10x.png. No lugar de 'Algoritmo do Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso

    def otimizadorGrupo_Felipe_Leo(self, rota: Rota, time_ms: int):
        timeArr = []
        comprimentoArr = []
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        comprimento = rota.comprimento()
        minComprimento = comprimento
        timeArr.append(delta_ms)
        comprimentoArr.append(comprimento)
        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            rota.otimiza()
            if(rota.comprimento() < minComprimento):
                minComprimento = rota.comprimento()
            comprimento = rota.comprimento()
            timeArr.append(delta_ms)
            comprimentoArr.append(comprimento)
        self.plt.bar(
            timeArr, 
            comprimentoArr,
            width=1000, 
            color="#00f", 
            label="Felipe_Leo", 
            linewidth=5
            )
        
        self.plt.tight_layout()
        self.plt.legend()
        self.plt.savefig("Otimizacao_Felipe_Leo.png")
        resp = {
            "x": timeArr,
            "y": comprimentoArr,
            "min": minComprimento,
            "color": "#00f",
            "label" : "Felipe_Leo",
            "linewidth" : 5
        }
        return resp

    # Esta função deve salvar o gráfico. A função não deve ser alterada.
    # O objetivo final é colocar vários algoritmos vindos de grupos diferentes
    # num mesmo gráfico e depois esta função irá salvar a solução com todos os gráficos.
    def salvaFigura(self, filename):
        self.plt.tight_layout()
        self.plt.legend()
        #self.plt.grid(True)
        #self.plt.show()
        self.plt.savefig(filename)


def swap(rota: Rota, pos1: int, pos2: int):
    aux = rota.coords[pos1]
    rota.coords[pos1] = rota.coords[pos2]
    rota.coords[pos2] = aux


# Cria uma rota Vazia.
r = Rota()
# Número de coordenadas da rota
size = int(input("Digite o número de vértices:"))
# valor máximo x e y para a coordenada
r.randomCoords(size, 400)
# Cria o otimizador
opt = Otimizador()
# Tempo de otimização em ms
time_ms = int(input("Digite o tempo em ms:"))
# Otimiza por single swap
opt.singleSwap(r, time_ms)
# Otimização aleatório
opt.aleatorio(r, time_ms)
# Otimização feita por seu grupo
opt.otimizadorGrupo_Felipe_Leo(r, time_ms)
opt.salvaFigura("Resultado_" + str(size) + ".png")
