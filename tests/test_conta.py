from exceptions.conta_exceptions import ContaComSaldoError, SaldoNegativoError, ValorInvalidoError
from conta import Conta
from usuario import Usuario
from datetime import date
import pytest

class TesteConta:

    def teste_get_saldo_quando_conta_tem_saldo_entao_retorne_saldo(self):
        # Arrange
        usuario = Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10))
        conta = Conta(1001, "1234-5", "001", "Banco VVT", usuario, 1000.0, date.today(), True)

        # Act
        saldo = conta.get_saldo()

        # Assert
        assert 1000.0 == saldo

    def teste_deposito_quando_conta_com_saldo_entao_adiciona_valor_ao_saldo(self, conta_com_saldo):
        # Arrange
        valor = 100

        # Act
        conta_com_saldo.deposito(valor)

        assert 1100.0 == conta_com_saldo.get_saldo()

    def teste_deposito_quando_valor_inserido_igual_a_zero_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        valor = 0

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()): # Assert
            conta_com_saldo.deposito(valor) # Act

    def teste_deposito_quando_valor_inserido_eh_negativo_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        valor = -100

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()): # Assert
            conta_com_saldo.deposito(valor) # Act
        
    def teste_saque_quando_conta_com_saldo_entao_debita_valor_do_saldo(self, conta_com_saldo):
        # Arrange
        valor = 100

        # Act
        conta_com_saldo.saque(valor)

        # Assert
        assert 900.0 == conta_com_saldo.get_saldo()

    def teste_saque_quando_valor_inserido_igual_a_zero_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        valor = 0

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()):  # Assert
            conta_com_saldo.saque(valor)  # Act

    def teste_saque_quando_valor_inserido_eh_negativo_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        valor = -100

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()):  # Assert
            conta_com_saldo.saque(valor)  # Act

    def teste_transferir_quando_conta_com_saldo_entao_debita_na_conta_origem(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)

        # Act
        conta_com_saldo.transferir(200, conta_destino)

        # Assert
        assert 800.0 == conta_com_saldo.get_saldo()

    def teste_tranferir_quando_conta_com_saldo_entao_credita_na_conta_destino(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)

        # Act
        conta_com_saldo.transferir(200, conta_destino)

        # Assert
        assert 2200.0 == conta_destino.get_saldo()

    def teste_tranferir_quando_valor_inserido_igual_a_zero_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)
        valor = 0

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()): # Assert
            conta_com_saldo.transferir(valor, conta_destino) # Act

    def teste_tranferir_quando_valor_inserido_menor_que_zero_entao_lanca_excecao(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902", date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)
        valor = -100

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()): # Assert
            conta_com_saldo.transferir(valor, conta_destino) # Act

    def teste_transferir_quando_valor_inserido_menor_igual_a_zero_entao_cancela_operacao(self, conta_com_saldo):
        # Arrange
        usuario_destino = Usuario("Carlos Martins", "carlos.martins@example.com", "senha1234", "03004508902",
                                  date(1991, 6, 7))
        conta_destino = Conta(1002, "1234-5", "001", "Banco VVT", usuario_destino, 2000.0, date.today(), True)
        valor = -100
        saldo_fonte = conta_com_saldo.get_saldo()
        saldo_destino = conta_destino.get_saldo()

        with pytest.raises(ValorInvalidoError, match='Valor invalido'.upper()):
            conta_com_saldo.transferir(valor, conta_destino) # Act

        # Assert
        assert conta_com_saldo.get_saldo() == saldo_fonte
        assert conta_destino.get_saldo() == saldo_destino

    def teste_fechar_conta_quando_conta_esta_com_saldo_entao_raise_exception(self, conta_com_saldo):
        with pytest.raises(ContaComSaldoError, match=f"Conta com Saldo!! Saldo atual: {conta_com_saldo.get_saldo()}".upper()): # Assert
            # Act
            conta_com_saldo.fechar_conta()

    def teste_fechar_conta_quando_conta_esta_com_saldo_negativo_entao_raise_exception(self, conta_com_saldo_negativo):
        with pytest.raises(SaldoNegativoError, match=f'Saldo Negativo!! Saldo atual: {conta_com_saldo_negativo.get_saldo()}'.upper()): # Assert
            # Act
            conta_com_saldo_negativo.fechar_conta()

    def teste_fechar_conta_quando_conta_sem_saldo_entao_usuario_conta_is_none(self, conta_sem_saldo):
        # Act
        conta_sem_saldo.fechar_conta()

        # Assert
        assert conta_sem_saldo.usuario is None

    def teste_fechar_conta_quando_conta_sem_saldo_entao_conta_ativa_to_false(self, conta_sem_saldo):
       # Act
       conta_sem_saldo.fechar_conta()

       # Assert
       assert conta_sem_saldo.ativa == False
        
    def teste_saldo_negativo_quando_conta_esta_com_saldo_entao_retorne_falso(self, conta_com_saldo):
        # Act
        resposta = conta_com_saldo.saldo_negativo()

        # Assert
        assert resposta == False

    def teste_saldo_negativo_quando_conta_esta_sem_saldo_entao_retorne_falso(self, conta_sem_saldo):
        # Act
        resposta = conta_sem_saldo.saldo_negativo()

        # Assert
        assert resposta == False

    def teste_saldo_negativo_quando_conta_esta_com_saldo_negativo_entao_retorne_true(self, conta_com_saldo_negativo):
        # Act
        resposta = conta_com_saldo_negativo.saldo_negativo()

        # Assert
        assert resposta == True

    def teste_aplica_juros_quando_conta_esta_com_saldo_entao_aplique_juros_com_sucesso(self, conta_com_saldo):
        # Arrange
        porcentagem = .10
        saldo_antigo = conta_com_saldo.get_saldo()

        # Act
        saldo_atual = conta_com_saldo.aplica_juros(porcentagem)

        # Assert
        assert  saldo_atual == saldo_antigo * porcentagem

