class Fracao:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, outra):
        novo_numerador = (self.numerador * outra.denominador) + (
            outra.numerador * self.denominador
        )
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __sub__(self, outra):
        novo_numerador = (self.numerador * outra.denominador) - (
            outra.numerador * self.denominador
        )
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __mul__(self, outra):
        novo_numerador = self.numerador * outra.numerador
        novo_denominador = self.denominador * outra.denominador
        return Fracao(novo_numerador, novo_denominador)

    def __truediv__(self, outra):
        novo_numerador = self.numerador * outra.denominador
        novo_denominador = self.denominador * outra.numerador
        return Fracao(novo_numerador, novo_denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"


f1 = Fracao(1, 2)
f2 = Fracao(3, 4)
print("Soma:", f1 + f2)
