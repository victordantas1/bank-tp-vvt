from datetime import date


class Usuario:
    def __init__(self, nome: str, saldo: float, email: str, senha: str, cpf: str, data_nascimento: date):
        self.nome = nome
        self.saldo = saldo
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.data_nascimento = data_nascimento