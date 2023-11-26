class Pokemon:
    def __init__(self, hp, iv, nome, tipos, ataqueRapido, ataquesCarregados):
        self.__hp = hp
        self.__iv = iv
        self.__tipos = tipos
        self.__nome = nome
        self.__ataqueRapido = ataqueRapido
        self.__ataquesCarregados = ataquesCarregados
        self.__energiaAcumulada = 0

    # Getters
    def get_hp(self):
        return self.__hp

    def get_iv(self):
        return self.__iv

    def get_tipos(self):
        return self.__tipos

    def get_nome(self):
        return self.__nome

    def get_ataqueRapido(self):
        return self.__ataqueRapido

    def get_ataquesCarregados(self):
        return self.__ataquesCarregados

    def get_energiaAcumulada(self):
        return self.__energiaAcumulada

    # Setters
    def set_hp(self, hp):
        self.__hp = hp

    def set_iv(self, iv):
        self.__iv = iv

    def set_tipos(self, tipos):
        self.__tipos = tipos

    def set_nome(self, nome):
        self.__nome = nome

    def set_ataqueRapido(self, ataqueRapido):
        self.__ataqueRapido = ataqueRapido

    def set_ataquesCarregados(self, ataquesCarregados):
        self.__ataquesCarregados = ataquesCarregados

    def set_energiaAcumulada(self, energiaAcumulada):
        self.__energiaAcumulada = energiaAcumulada

    # métodos
    def toString(self):
        return print(f"{self.__nome}, {self.__hp}, {self.__iv}, {self.__tipos}, {self.__ataqueRapido.toString()}, {self.__ataquesCarregados.toString()}, {self.__energiaAcumulada}.")

    def atacar(self):
        dano = (self.__ataqueRapido.get_dano() * self.__iv) / 65
        print(f"O {self.__nome} atacou e deu {round(dano, 2)} de dano ao oponente!!")
        self.__energiaAcumulada += self.__ataqueRapido.get_geraEnergia()
        print(f"E acumulou {self.__energiaAcumulada}")
        return dano


class Ataque:
    def __init__(self, nome, dano, tipo):
        self.__nome = nome
        self.__dano = dano
        self.__tipo = tipo

    # Getters
    def get_nome(self):
        return self.__nome

    def get_dano(self):
        return self.__dano

    def get_tipo(self):
        return self.__tipo

    def toString(self):
        return f"HYYYYAAA!!!!"

class AtaqueRapido(Ataque):
    def __init__(self, geraEnergia, nome, dano, tipo):
        Ataque.__init__(self, nome, dano, tipo)
        self.__geraEnergia = geraEnergia

    # Getters

    def get_geraEnergia(self):
        return self.__geraEnergia

    # métodos
    def toString(self):
        return f"{self._Ataque__nome}, {self._Ataque__dano}, {self._Ataque__tipo}, {self.__geraEnergia}"


class AtaqueCarregado(Ataque):
    def __init__(self, energiaAtivacao, nome, dano, tipo):
        Ataque.__init__(self, nome, dano, tipo)
        self.__energiaAtivacao = energiaAtivacao

    # Getters
    def get_energiaAtivacao(self):
        return self.__energiaAtivacao

    # métodos
    def toString(self):
        return f"{self._Ataque__nome}, {self._Ataque__dano}, {self._Ataque__tipo}, {self.__energiaAtivacao}"


class BatalhaPvP:
    def __init__(self, pokemon):
        self.__pokemon = pokemon

    # Getters
    def get_pokemon(self):
        return self.__pokemon

    # método
    def battle(self):
        while self.__pokemon[1].get_hp() >= 0 or self.__pokemon[0].get_hp() <= 0:
            # Acumulando o dano dado pelo Pokémon adversário
            self.__pokemon[1].set_hp(self.__pokemon[1].get_hp() - self.__pokemon[0].atacar())
            # print(round(self.__pokemon[1].get_hp(), 2))
            if self.__pokemon[1].get_hp() <= 0:
                print(f"O vencedor da batalha é {self.__pokemon[0].get_nome()}")
                break

            self.__pokemon[0].set_hp(self.__pokemon[0].get_hp() - self.__pokemon[1].atacar())
            # print(round(self.__pokemon[0].get_hp(), 2))
            if self.__pokemon[0].get_hp() <= 0:
                print(f"O vencedor da batalha é {self.__pokemon[1].get_nome()}")
                break


#ataques rápidos
pds = AtaqueRapido(11, "Projétil de semente", 8, "Planta")
abis = AtaqueRapido(10, "Abismar", 8, "Fantasma")
cZen = AtaqueRapido(20, "Cabeçada Zen", 12, "Psíquico")
ros = AtaqueRapido(15, "Rosnado", 12, "Sombrio")

#ataques carregados
pdd = AtaqueCarregado(45, "Pulso do Dragão", 90, "Dragão")
vo = AtaqueCarregado(30, "Vento Ominoso", 40, "Fantasma")
trr = AtaqueCarregado(100, "Terremoto", 140, "Terra")
gdd = AtaqueCarregado(50, "Garra de Dragão", 50, "Dragão")

#pokemons
shuppet = Pokemon(73, 39, "Shuppet", ["Fantasma"], abis, vo)
exeggutor = Pokemon(106, 30, "Exeggutor", ["Planta", "Dragão"], pds, pdd)
meta = Pokemon(142, 43, "Metagross", ["Aço", "Psíquico"], cZen, trr)
guzz = Pokemon(302, 37, "Guzzlord", ["Sombrio", "Dragão"], ros, gdd)

#batalhas
primeiraBatalha = BatalhaPvP([exeggutor, shuppet])
segundaBatalha = BatalhaPvP([exeggutor, meta])
terceiraBatalha = BatalhaPvP([shuppet, meta])
quartaBatalha =BatalhaPvP([meta, guzz])
quintaBatalha =BatalhaPvP([shuppet, guzz])
sextaBatalha =BatalhaPvP([exeggutor, guzz])

# metodos
quartaBatalha.battle()
# meta.toString()
# meta.atacar()