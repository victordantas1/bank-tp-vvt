from utils import cria_usuarios, cria_contas, busca_conta, acessar_conta, cria_conta
import pytest
from usuario import Usuario
from conta import Conta  
from datetime import date

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
    conta = busca_conta(contas, "00000000000")
    assert conta is None

def teste_busca_conta_quando_cpf_existe_entao_retorne_a_conta(lista_contas):
    cpf = "12345678901"
    conta = busca_conta(lista_contas, cpf=cpf)
    assert conta is not None

def teste_busca_conta_quando_cpf_nao_existe_entao_retorne_none(lista_contas):
    cpf = "1234567890112"
    conta = busca_conta(lista_contas, cpf=cpf)
    assert conta is None
