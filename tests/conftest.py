import pytest
from usuario import Usuario
from conta import Conta
from datetime import datetime, date # ajuste o import conforme sua estrutura


@pytest.fixture
def usuario_conta_com_saldo():
    usuario = Usuario(
        nome="Ana Silva",
        email="ana.silva@example.com",
        senha="senha123",
        cpf="12345678901",
        data_nascimento=date(1990, 5, 10)
    )
    return usuario

@pytest.fixture
def conta_com_saldo(usuario_conta_com_saldo):
    conta = Conta(
        numero_conta=1001,
        agencia_conta="1234-5",
        numero_banco="001",
        nome_banco="Banco VVT",
        usuario=usuario_conta_com_saldo,
        saldo=1000.0,
        data_criacao=datetime.now(),
        ativa=True
    )
    return conta

@pytest.fixture
def usuario_conta_com_saldo_negativo():
    usuario = Usuario(
        nome="Carlos Martins",
        email="carlos.martins@example.com",
        senha="senha1234",
        cpf="03004508902",
        data_nascimento=date(1991, 6, 7)
    )
    return usuario

@pytest.fixture
def conta_com_saldo_negativo(usuario_conta_com_saldo_negativo):
    conta = Conta(
        numero_conta=1002,
        agencia_conta="1234-5",
        numero_banco="001",
        nome_banco="Banco VVT",
        usuario=usuario_conta_com_saldo_negativo,
        saldo=-2000.0,
        data_criacao=datetime.now(),
        ativa=True
    )
    return conta

@pytest.fixture
def usuario_conta_sem_saldo():
    usuario = Usuario(
        nome="Pedro Martins",
        email="pedro.martins@example.com",
        senha="senha1234",
        cpf="03004508912",
        data_nascimento=date(1989, 6, 7)
    )
    return usuario

@pytest.fixture
def conta_sem_saldo(usuario_conta_sem_saldo):
    conta = Conta(
        numero_conta=1003,
        agencia_conta="1234-5",
        numero_banco="001",
        nome_banco="Banco VVT",
        usuario=usuario_conta_sem_saldo,
        saldo=0.0,
        data_criacao=datetime.now(),
        ativa=True
    )
    return conta