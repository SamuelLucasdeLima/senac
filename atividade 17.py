class AreaBase:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calculo(self):
        return print(self.__base * self.__altura)

class AreaBase2:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calculo(self):
        return print((self.__base*self.__altura)/2)

# Classes derivadas
class Retangulo(AreaBase):
    def __init__(self, base, altura):
        super().__init__(base, altura)

class Paralelogramo(AreaBase):
    def __init__(self, base, altura):
        super().__init__(base, altura)

class Triangulo(AreaBase2):
    def __init__(self, base, altura):
        super().__init__(base, altura)

class Losango(AreaBase2):
    def __init__(self, diagonalMaior, diagonalMenor):
        super().__init__(diagonalMaior, diagonalMenor)

class Trapezio(AreaBase2):
    def __init__(self, baseMenor, baseMaior, altura):
        super().__init__(baseMaior, altura)
        self.__baseMenor = baseMenor

    def calculo(self):
        return print(((self._AreaBase2__base+self.__baseMenor)*self._AreaBase2__altura)/2)

class Circulo(AreaBase):
    def __init__(self, raio):
        super().__init__(raio, 0)

    def calculo(self):
        return print((self._AreaBase__base * self._AreaBase__base)*3.14)


# instanciando objs
retantan = Retangulo(2,9)
parara = Paralelogramo(3,7)
trianan = Triangulo(12,8)
tratrape = Trapezio(3,7,6)
losansan = Losango(20,10)
ciiirculo = Circulo(15)

# chamando metodos
retantan.calculo()
parara.calculo()
trianan.calculo()
tratrape.calculo()
losansan.calculo()
ciiirculo.calculo()