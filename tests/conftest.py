import pytest
from usuario import Usuario
from conta import Conta
from datetime import date

from utils import cria_usuarios, cria_contas


@pytest.fixture
def usuario_conta_com_saldo():
    return Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10))

@pytest.fixture
def conta_com_saldo(usuario_conta_com_saldo):
    return Conta(1001, "1234-5", "001", "Banco VVT", usuario_conta_com_saldo, 1000.0, date.today(), True)

@pytest.fixture
def usuario_conta_com_saldo_negativo():
    return Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))

@pytest.fixture
def conta_com_saldo_negativo(usuario_conta_com_saldo_negativo):
    return Conta(1002, "1234-5", "001", "Banco VVT", usuario_conta_com_saldo_negativo, -2000.0, date.today(), True)

@pytest.fixture
def usuario_conta_sem_saldo():
    return Usuario("Pedro Martins", "pedro.martins@example.com", "senha1234", "03004508912", date(1989, 6, 7))

@pytest.fixture
def conta_sem_saldo(usuario_conta_sem_saldo):
    return Conta(1003, "1234-5", "001", "Banco VVT", usuario_conta_sem_saldo, 0, date.today(), True)

@pytest.fixture
def lista_usuarios():
    return cria_usuarios()

@pytest.fixture
def lista_contas(lista_usuarios):
    return cria_contas(lista_usuarios)