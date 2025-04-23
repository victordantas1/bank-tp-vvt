from utils import *
import pytest
from usuario import Usuario
from conta import Conta  
from datetime import date
from exceptions.conta_exceptions import *

def test_cria_usuarios():
    usuarios = cria_usuarios()
    assert isinstance(usuarios, list)
    assert all(isinstance(u, Usuario) for u in usuarios)
    assert usuarios[0].nome == "Ana Silva"
    assert usuarios[-1].cpf == "01234567890"
    assert len(usuarios) == 10
    assert usuarios[0].email == "ana.silva@example.com"

def test_cria_contas():
    usuarios = cria_usuarios()
    contas = cria_contas(usuarios)
    assert isinstance(contas, list)
    assert all(isinstance(c, Conta) for c in contas)
    assert contas[0].get_saldo() == 1000
    assert contas[0].usuario.nome == "Ana Silva"
    assert contas[-1].usuario.nome == "Julia Fernandes"

def test_busca_conta_encontra():
    usuarios = cria_usuarios()
    contas = cria_contas(usuarios)
    conta = busca_conta(contas, "23456789012")
    assert conta is not None
    assert conta.usuario.nome == "Bruno Souza"

def test_busca_conta_nao_encontra():
    usuarios = cria_usuarios()
    contas = cria_contas(usuarios)
    with pytest.raises(ContaNaoEncontradaError, match='CONTA NAO ENCONTRADA!!'):
        conta = busca_conta(contas, "00000000000")


def teste_deletar_conta_quando_conta_existente_na_lista_entao_remove_conta():
    # Arrange
    usuarios = [ Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10)),
                 Usuario("Bruno Souza", "bruno.souza@example.com", "senha456", "23456789012", date(1985, 8, 22)) ]
    contas = cria_contas(usuarios)
    conta = contas[1]
    conta.saque(1000)

    # Act
    deletar_conta(conta, contas)

    # Assert
    assert len(contas) == 1