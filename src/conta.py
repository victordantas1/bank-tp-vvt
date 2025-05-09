from __future__ import annotations

from datetime import date
from exceptions.conta_exceptions import SaldoNegativoError, ContaComSaldoError, ValorInvalidoError, SaldoInsuficienteError
from usuario import Usuario


class Conta:
    def __init__(self, numero_conta: int, agencia_conta: str, numero_banco: str, nome_banco: str, usuario: Usuario, saldo: float, data_criacao: date, ativa: bool):
        self.numero_conta = numero_conta
        self.agencia_conta = agencia_conta
        self.numero_banco = numero_banco
        self.nome_banco = nome_banco
        self.usuario = usuario
        self.__saldo = saldo
        self.data_criacao = data_criacao
        self.ativa = ativa

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numero_conta})"

    def get_saldo(self) -> float:
        """
        Retorna o saldo da conta
        Returns: saldo da conta
        """
        return self.__saldo

    def deposito(self, valor: float) -> float:
        """
        Deposita o valor no saldo da conta
        Args:
            valor: valor a depositar

        Returns: novo saldo da conta

        """
        if valor > 0:
            self.__saldo = self.__saldo + valor
        else:
            raise ValorInvalidoError("Valor invalido!!!".upper())
        return self.get_saldo()

    def saque(self, valor: int) -> float:
        """
        Sacar um valor no saldo da conta
        Args:
            valor: valor a sacar

        Returns: novo saldo da conta

        """
        if valor <= 0:
            raise ValorInvalidoError("Valor invalido".upper())
        elif self.__saldo >= valor:
            self.__saldo = self.__saldo - valor
        else:
            raise SaldoInsuficienteError(f"Valor superior ao saldo da conta!! Saldo Atual: {self.__saldo}".upper())

        return self.get_saldo()


    def transferir(self, valor: float, conta: Conta) -> float:
        """
        Transferir um valor do saldo da conta
        Args:
            valor: valor a transferir
            conta: Conta para transferir

        Returns: novo saldo da conta

        """
        if valor <= 0:
            raise ValorInvalidoError("Valor invalido!!!".upper())
        elif self.__saldo < valor:
            raise SaldoInsuficienteError(f"Valor superior ao saldo da conta!! Saldo Atual: {self.__saldo}".upper())
        else:
            self.__saldo = self.__saldo - valor
            conta.deposito(valor)
            return self.get_saldo()

    def fechar_conta(self) -> str:
        """
        Fecha a conta
        Returns: String com mensagem de fechamento da conta

        """
        if self.__saldo < 0:
            raise SaldoNegativoError(f'Saldo Negativo!! Saldo atual: {self.__saldo}'.upper())
        elif self.__saldo > 0:
            raise ContaComSaldoError(f'Conta com Saldo!! Saldo atual: {self.__saldo}'.upper())
        else:
            self.usuario = None
            self.ativa = False
            return 'Conta fechada'


    def saldo_negativo(self) -> bool:
        """
        Verifica se o saldo esta negativo
        Returns: true se o saldo esta negativo, false se o saldo nao esta negativo

        """
        return True if self.__saldo < 0 else False

    def aplica_juros(self, porcentagem: float) -> float:
        """
        Aplica uma porcentagem de juros no saldo da conta
        Args:
            porcentagem: porcentagem de juros a ser aplicado

        Returns: novo saldo da conta

        """
        self.__saldo = self.__saldo * porcentagem
        return self.get_saldo()
