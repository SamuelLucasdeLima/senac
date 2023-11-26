#class CreeperMinecraft:
 #   def __init__(self, saude, raio_explosao, raio_perseguicao , velocidade, nome, habito, explosao_silenciosa):
  #      self.saude = saude
   #     self.raio_explosao = raio_explosao
    #    self.raio_perseguicao = raio_perseguicao
     #   self.velocidade = velocidade
      #  self.nome = nome
       # self.habito = habito
        #self.explosao_silenciosa = explosao_silenciosa

    #def __str__(self):
     #   return f"Nome: {self.nome}\nSaúde: {self.saude}\nRaio de Explosão: {self.raio_explosao}\nRaio de Perseguição: {self.raio_perseguicao}\nVelocidade: {self.velocidade}\nHábito: {self.habito}\nExplosão Silenciosa: {self.explosao_silenciosa}"

# Criando um Creeper do Minecraft
#creeper = CreeperMinecraft(20, "3 blocos"," 16 Blocos ", 2, "Creeper", "Dia, Noturno", False)

# Exibindo informações do Creeper
#print(creeper)


class EsqueletoMinecraft:
    def __init__(self, saude, arco, flechas, nome, habito, armadura, raio_perseguicao ,ataque_distancia):
        self.saude = saude
        self.arco = arco
        self.flechas = flechas
        self.nome = nome
        self.habito = habito
        self.armadura = armadura
        self.ataque_distancia = ataque_distancia
        self.raio_perseguicao = raio_perseguicao

    def __str__(self):
        return f"Nome: {self.nome}\nSaúde: {self.saude}\nArco: {self.arco}\nFlechas: {self.flechas}\nHábito: {self.habito}\nArmadura: {self.armadura}\nRaio de Perseguição: {self.raio_perseguicao}\nPrecisão de Ataque à Distância: {self.ataque_distancia}"

# Criando um Esqueleto do Minecraft
esqueleto = EsqueletoMinecraft(20, "Arco de Ferro", 10, "Esqueleto", "Noturno", "Nenhuma", "15 blocos" , "16 blocos")

# Exibindo informações do Esqueleto
print(esqueleto)



 