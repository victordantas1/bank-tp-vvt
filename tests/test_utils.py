from utils import cria_usuarios, cria_contas, busca_conta, acessar_conta, cria_conta
import pytest
from usuario import Usuario
from conta import Conta  
from datetime import date

class TestUtils:
    def test_cria_usuarios(self):
        usuarios = cria_usuarios()
        assert isinstance(usuarios, list)
        assert all(isinstance(u, Usuario) for u in usuarios)
        assert len(usuarios) == 10

    def teste_cria_contas_quando_lista_usuarios_eh_valida_entao_retorne_lista_de_contas(self, lista_usuarios):
        contas = cria_contas(lista_usuarios)
        assert isinstance(contas, list)
        assert all(isinstance(c, Conta) for c in contas)

    def teste_cria_contas_quando_lista_usuarios_eh_valida_entao_crie_contas_com_numero_conta_incremental(self, lista_usuarios):
        # Arrange
        numeros_contas_esperados = range(1001, 1011)

        # Act
        contas = cria_contas(lista_usuarios)

        # Assert
        assert numeros_contas_esperados == [conta.numero_conta for conta in contas]

    def teste_busca_conta_quando_cpf_existe_entao_retorne_a_conta(self, lista_contas):
        cpf = "12345678901"
        conta = busca_conta(lista_contas, cpf=cpf)
        assert conta is not None
        assert conta.usuario.nome == "Ana Silva"

    def teste_busca_conta_quando_cpf_nao_existe_entao_retorne_none(self, lista_contas):
        cpf = "1234567890112"
        conta = busca_conta(lista_contas, cpf=cpf)
        assert conta is None
