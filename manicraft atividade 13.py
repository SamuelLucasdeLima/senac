import math

class Jogador:
    def __init__(self, nome, saude, habito, posicaoX, posicaoY):
        self.nome = nome
        self.saude = saude
        self.habito = habito
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nHábito: {self.habito}\nPosição X: {self.posicaoX}\nPosição Y: {self.posicaoY}"

    def mover(self, nova_posicaoX, nova_posicaoY):
        self.posicaoX = nova_posicaoX
        self.posicaoY = nova_posicaoY
        print(f"{self.nome} moveu-se para a posição ({nova_posicaoX}, {nova_posicaoY}).")

class CreeperMinecraft:
    def __init__(self, saude, raio_explosao, raio_perseguicao, velocidade, nome, habito, explosao_silenciosa, posicaoX, posicaoY):
        self.saude = saude
        self.raio_explosao = raio_explosao
        self.raio_perseguicao = raio_perseguicao
        self.velocidade = velocidade
        self.nome = nome
        self.habito = habito
        self.explosao_silenciosa = explosao_silenciosa
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nRaio de Explosão: {self.raio_explosao}\nRaio de Perseguição: {self.raio_perseguicao}\nVelocidade: {self.velocidade}\nHábito: {self.habito}\nExplosão Silenciosa: {self.explosao_silenciosa}\nPosição X: {self.posicaoX}\nPosição Y: {self.posicaoY}"

    def correr_em_direcao_do_jogador(self, jogador):
        distancia = math.sqrt((self.posicaoX - jogador.posicaoX) ** 2 + (self.posicaoY - jogador.posicaoY) ** 2)
        if distancia > 0 and distancia <= float(self.raio_perseguicao.replace(" blocos", "")):
            deslocamento_X = jogador.posicaoX - self.posicaoX
            deslocamento_Y = jogador.posicaoY - self.posicaoY
            comprimento = math.sqrt(deslocamento_X ** 2 + deslocamento_Y ** 2)
            deslocamento_X /= comprimento
            deslocamento_Y /= comprimento
            self.posicaoX += self.velocidade * deslocamento_X
            self.posicaoY += self.velocidade * deslocamento_Y
            print(f"{self.nome} está correndo em direção ao jogador!")
        elif distancia <= 0:
            print(f"{self.nome} já está na mesma posição que o jogador!")
        else:
            print(f"{self.nome} está fora do alcance do jogador!")

class EsqueletoMinecraft:
    def __init__(self, saude, arco, flechas, nome, habito, armadura, raio_perseguicao, ataque_distancia, posicaoX, posicaoY):
        self.saude = saude
        self.arco = arco
        self.flechas = flechas
        self.nome = nome
        self.habito = habito
        self.armadura = armadura
        self.ataque_distancia = ataque_distancia
        self.raio_perseguicao = raio_perseguicao
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nArco: {self.arco}\nFlechas: {self.flechas}\nHábito: {self.habito}\nArmadura: {self.armadura}\nRaio de Perseguição: {self.raio_perseguicao}\nPrecisão de Ataque à Distância: {self.ataque_distancia}\nPosição X: {self.posicaoX}\nPosição Y: {self.posicaoY}"

    def atirar_no_jogador(self, jogador):
        distancia = math.sqrt((self.posicaoX - jogador.posicaoX) ** 2 + (self.posicaoY - jogador.posicaoY) ** 2)
        if distancia > 0 and distancia <= float(self.raio_perseguicao.replace(" blocos", "")):
            print(f"{self.nome} atirou uma flecha no jogador!")

# Exemplo de uso dos métodos
jogador = Jogador("Judeuson", 100, "Dia e Noite", 10, 5)
creeper = CreeperMinecraft(20, "3 blocos", "16 blocos", 2, "Creeper", "Dia, Noturno", False, 10, 5)
esqueleto = EsqueletoMinecraft(20, "Arco de Ferro", 10, "Esqueleto", "Noturno", "Nenhuma", "15 blocos", "16 blocos", 15, 8)

# Simulando a ação de correr em direção ao jogador pelo Creeper
creeper.correr_em_direcao_do_jogador(jogador)

# Simulando a ação de atirar no jogador pelo Esqueleto
esqueleto.atirar_no_jogador(jogador)

# Simulando a ação de movimentação do jogador
jogador.mover(12, 7)