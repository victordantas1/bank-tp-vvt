from exceptions.conta_exceptions import ContaComSaldoError, SaldoNegativoError
from conta import Conta
from usuario import Usuario
from datetime import date
import pytest

class TestConta:

    def test_get_saldo_when_conta_com_saldo_then_retorne_saldo(self):
        # Arrange
        usuario = Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10))
        conta = Conta(1001, "1234-5", "001", "Banco VVT", usuario, 1000.0, date.today(), True)

        # Act
        saldo = conta.get_saldo()

        # Assert
        assert 1000.0 == saldo

    def test_deposito_when_conta_com_saldo_then_adiciona_valor_ao_saldo(self, conta_com_saldo):
        # Arrange
        valor = 100

        # Act
        conta_com_saldo.deposito(valor)

        assert 1100.0 == conta_com_saldo.get_saldo()
        
    def test_saque_when_conta_com_saldo_then_remove_valor_do_saldo(self, conta_com_saldo):
        # Arrange
        valor = 100

        # Act
        conta_com_saldo.saque(valor)

        assert 900.0 == conta_com_saldo.get_saldo()
        
    def test_transferir_when_conta_com_saldo_then_debita_na_conta_origem(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)

        # Act
        conta_com_saldo.transferir(200, conta_destino)

        # Assert
        assert 800.0 == conta_com_saldo.get_saldo()

    def test_tranferir_when_conta_com_saldo_then_transfere_credita_na_conta_destino(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)

        # Act
        conta_com_saldo.transferir(200, conta_destino)

        # Assert
        assert 2200.0 == conta_destino.get_saldo()

    def test_fechar_conta_when_conta_esta_com_saldo_then_raise_exception(self, conta_com_saldo):
        with pytest.raises(ContaComSaldoError, match=f"Conta com Saldo! Saldo atual: {conta_com_saldo.get_saldo()}"): # Assert
            # Act
            conta_com_saldo.fechar_conta()

    def test_fechar_conta_when_conta_esta_com_saldo_negativo_then_raise_exception(self, conta_com_saldo_negativo):
        with pytest.raises(SaldoNegativoError, match=f'Saldo Negativo! Saldo atual: {conta_com_saldo_negativo.get_saldo()}'): # Assert
            # Act
            conta_com_saldo_negativo.fechar_conta()

    def test_fechar_conta_when_conta_sem_saldo_then_usuario_conta_is_none(self, conta_sem_saldo):
        # Act
        conta_sem_saldo.fechar_conta()

        # Assert
        assert conta_sem_saldo.usuario is None

    def test_fechar_conta_when_conta_sem_saldo_then_conta_ativa_to_false(self, conta_sem_saldo):
       # Act
       conta_sem_saldo.fechar_conta()

       # Assert
       assert conta_sem_saldo.ativa == False
        
    def test_saldo_negativo_when_conta_esta_com_saldo(self, conta_com_saldo):
        # Act
        resposta = conta_com_saldo.saldo_negativo()

        # Assert
        assert resposta == False

    def test_saldo_negativo_when_conta_esta_sem_saldo(self, conta_sem_saldo):
        # Act
        resposta = conta_sem_saldo.saldo_negativo()

        # Assert
        assert resposta == False

    def test_saldo_negativo_when_conta_esta_com_saldo_negativo(self, conta_com_saldo_negativo):
        # Act
        resposta = conta_com_saldo_negativo.saldo_negativo()

        # Assert
        assert resposta == True

    def test_aplica_juros_when_conta_esta_com_saldo_then_aplique_juros_com_sucesso(self, conta_com_saldo):
        # Arrange
        porcentagem = .10
        saldo_antigo = conta_com_saldo.get_saldo()

        # Act
        saldo_atual = conta_com_saldo.aplica_juros(porcentagem)

        # Assert
        assert  saldo_atual == saldo_antigo * porcentagem

