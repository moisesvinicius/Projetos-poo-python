from abc import ABC, abstractmethod

"""
Desafio: Criar um sistema de cadastro de veículos onde diferentes tipos 
de veículos compartilham atributos básicos, mas possuem implementações 
próprias do método exibir_info().
"""

# Classe abstrata representando um veículo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @abstractmethod
    def exibir_info(self):
        """Método abstrato para exibir informações do veículo"""
        pass

# Subclasse representando um carro
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_info(self):
        return f"Carro: {self.marca} {self.modelo} ({self.ano}) - {self.portas} portas"

# Subclasse representando uma moto
class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_info(self):
        return f"Moto: {self.marca} {self.modelo} ({self.ano}) - {self.cilindradas}cc"

# Criando instâncias e exibindo informações
veiculos = [
    Carro("Toyota", "Corolla", 2022, 4),
    Moto("Honda", "CB500", 2021, 500)
]

for v in veiculos:
    print(v.exibir_info())