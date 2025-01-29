from abc import ABC, abstractmethod
import math

class TrianguloRetangulo(ABC):
    @abstractmethod
    def cateto1(self, valor):
        """Define ou retorna o valor do primeiro cateto"""
        pass

    @abstractmethod
    def cateto2(self, valor):
        """Define ou retorna o valor do segundo cateto"""
        pass

    @abstractmethod
    def hipotenusa(self):
        """Calcula e retorna o valor da hipotenusa"""
        pass


class Soma(TrianguloRetangulo):
    def __init__(self):
        self._cateto1 = 0
        self._cateto2 = 0

    def cateto1(self, valor):
        self._cateto1 = valor
        return self._cateto1

    def cateto2(self, valor):
        self._cateto2 = valor
        return self._cateto2

    def hipotenusa(self):
        # Calcula a hipotenusa usando o Teorema de Pitágoras
        return math.sqrt(self._cateto1 ** 2 + self._cateto2 ** 2)



soma = Soma()

# Define os valores dos catetos
print(f"Cateto 1: {soma.cateto1(5)}")  # Define e retorna 5
print(f"Cateto 2: {soma.cateto2(12)}")  # Define e retorna 12

# Calcula e imprime a hipotenusa
print(f"Hipotenusa: {soma.hipotenusa():.2f}")  # Retorna 13.00