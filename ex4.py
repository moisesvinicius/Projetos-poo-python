from abc import ABC, abstractmethod

"""
Desafio: Criar um sistema de autenticação onde diferentes métodos de login 
podem ser usados (senha, biometria, autenticação de dois fatores).
"""

# Classe abstrata representando um sistema de autenticação
class Autenticacao(ABC):
    @abstractmethod
    def autenticar(self, credenciais):
        """Método abstrato para autenticação"""
        pass

# Autenticação por senha
class AutenticacaoSenha(Autenticacao):
    def __init__(self, senha_correta):
        self.senha_correta = senha_correta

    def autenticar(self, credenciais):
        return credenciais == self.senha_correta

# Autenticação por biometria (simulada)
class AutenticacaoBiometrica(Autenticacao):
    def autenticar(self, credenciais):
        return credenciais == "impressao_digital_valida"

# Autenticação de dois fatores (simulada)
class AutenticacaoDoisFatores(Autenticacao):
    def autenticar(self, credenciais):
        senha, codigo = credenciais
        return senha == "senha123" and codigo == "123456"

# Testando autenticação
auth_methods = [
    AutenticacaoSenha("senha123"),
    AutenticacaoBiometrica(),
    AutenticacaoDoisFatores()
]

print(auth_methods[0].autenticar("senha123"))  # True
print(auth_methods[1].autenticar("impressao_digital_errada"))  # False
print(auth_methods[2].autenticar(("senha123", "123456")))  # True