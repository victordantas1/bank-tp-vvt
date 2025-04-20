from __future__ import annotations

from datetime import date
from exceptions.conta_exceptions import SaldoNegativoError, ContaComSaldoError
from usuario import Usuario
from mongoengine import Document, StringField, DateTimeField, BooleanField, IntField, ReferenceField, FloatField


class Conta(Document):
    numero_conta = IntField()
    agencia_conta = StringField()
    numero_banco = StringField()
    nome_banco = StringField()
    usuario = ReferenceField(Usuario)
    saldo = FloatField(db_field='saldo')
    data_criacao = DateTimeField()
    ativa = BooleanField()

    def __repr__(self):
        return f"Usuario: {self.usuario.nome}, Conta: {self.agencia_conta}, {self.numero_conta}"

    def get_saldo(self) -> float:
        """
        Retorna o saldo da conta
        Returns: saldo da conta
        """
        return self.saldo

    def deposito(self, valor: float) -> float:
        """
        Deposita o valor no saldo da conta
        Args:
            valor: valor a depositar

        Returns: novo saldo da conta

        """
        self.saldo = self.saldo + valor
        return self.get_saldo()

    def saque(self, valor: float) -> float:
        """
        Sacar um valor no saldo da conta
        Args:
            valor: valor a sacar

        Returns: novo saldo da conta

        """
        self.saldo = self.saldo - valor
        return self.get_saldo()

    def transferir(self, valor: float, conta: Conta) -> float:
        """
        Transferir um valor do saldo da conta
        Args:
            valor: valor a transferir
            conta: Conta para transferir

        Returns: novo saldo da conta

        """
        self.saldo -= valor
        conta.deposito(valor)
        return self.get_saldo()

    def fechar_conta(self) -> str:
        """
        Fecha a conta
        Returns: String com mensagem de fechamento da conta

        """
        if self.saldo < 0:
            raise SaldoNegativoError(f'Saldo Negativo! Saldo atual: {self.saldo}')
        elif self.saldo > 0:
            raise ContaComSaldoError(f'Conta com Saldo! Saldo atual: {self.saldo}')
        else:
            self.usuario = None
            self.ativa = False
            return 'Conta fechada'


    def saldo_negativo(self) -> bool:
        """
        Verifica se o saldo esta negativo
        Returns: true se o saldo esta negativo, false se o saldo nao esta negativo

        """
        return True if self.saldo < 0 else False

    def aplica_juros(self, porcentagem: float) -> float:
        """
        Aplica uma porcentagem de juros no saldo da conta
        Args:
            porcentagem: porcentagem de juros a ser aplicado

        Returns: novo saldo da conta

        """
        self.saldo = self.saldo * porcentagem
        return self.get_saldo()
