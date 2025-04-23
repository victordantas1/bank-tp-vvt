import os
import time
from typing import List

import conta
from conta import Conta
from exceptions.conta_exceptions import SenhaInvalidaError
from utils import busca_conta, deletar_conta


def imprime_menu() -> None: # pragma: no cover
    print("\n === Menu Principal ===")
    print("1 - Criar Conta")
    print("2 - Acessar Conta")
    print("0 - Sair")

def imprime_menu_conta(conta: Conta) -> None: # pragma: no cover
    print(f"\n=== Menu de {conta.usuario.nome.upper()} ===")
    print(f"\nSaldo Atual: {conta.get_saldo()}")
    print("1 - Fazer Saque")
    print("2 - Fazer Deposito")
    print("3 - Fazer Tranferencia")
    print("4 - Verificar se Saldo esta negativo")
    print("5 - Deletar Conta")
    print("0 - Voltar")

def fluxo_saque(conta: Conta) -> None:
    valor = int(input("Digite o valor: "))
    try:
        saldo = conta.saque(valor)
        print(f"Saque de R$ {valor} realizado com sucesso.")
        print(f"Saldo restante: {saldo}")
    except Exception as error:
        print(error)
        

def fluxo_deposito(conta: Conta) -> None:
    valor = int(input("Digite o valor: "))
    try:
        saldo = conta.deposito(valor)
        print(f"Deposito de R$ {valor} realizado com sucesso.")
        print(f"Saldo Atual: {saldo}")
    except Exception as error:
        print(error)
        

def fluxo_transferencia(conta: Conta, lista_contas: List[Conta]) -> None:
    cpf_conta_destino = input("Digite o CPF do destinatario: ")
    conta_destino = busca_conta(lista_contas, cpf_conta_destino)
    if conta_destino:
        valor = float(input("Digite o valor da transferencia: "))
        try:
            saldo = conta.transferir(valor, conta_destino)
            print("Transferencia Realizada com sucesso.")
            print(f"Saldo Atual: {saldo}")
        except Exception as error:
            print(error)
            
    else:
        print("Conta não encontrada!".upper())
        

def fluxo_saldo_negativo(conta: Conta) -> None:
    print(f"Saldo negativo. Saldo Atual: {conta.get_saldo()}") if conta.saldo_negativo() else print(
        f"Saldo Positivo. Saldo Atual: {conta.get_saldo()}")
    

def fluxo_fechar_conta(conta: Conta, lista_contas: List[Conta]) -> int | None:
    opcao = int(input(f"Deseja mesmo fechar sua conta (1 - sim | 0 - nao)?  "))
    if opcao == 1:
        try:
            deletar_conta(conta, lista_contas)
            print('Conta fechada com sucesso.'.upper())
            return True
        except Exception as error:
            print(error)
            
    else:
        return False

def acessar_conta(lista_contas: List[Conta]) -> None: # pragma: no cover
    try:
        cpf = input("Digite o CPF: ")
        conta = busca_conta(lista_contas, cpf)
        senha = input("Digite sua senha: ")
        if conta and senha == conta.usuario.senha:
            if conta:
                print(f"\n Bem-vindo(a), {conta.usuario.nome.upper()} !")
                print(f" Conta: {conta.numero_conta}")
                while True:
                    imprime_menu_conta(conta)

                    opcao = int(input("Escolha uma opcao: "))
                    match opcao:
                        case 0:
                            limpar_console()
                            break
                        case 1:
                            fluxo_saque(conta)
                        case 2:
                            fluxo_deposito(conta)
                        case 3:
                            fluxo_transferencia(conta, lista_contas)
                        case 4:
                            fluxo_saldo_negativo(conta)
                        case 5:
                            if fluxo_fechar_conta(conta, lista_contas): break
                    time.sleep(2)
            else:
                print("Conta não encontrada!".upper())
        else:
            raise SenhaInvalidaError('SENHA INCORRETA!!')
    except Exception as error:
        print(error)
        time.sleep(2)


def limpar_console(): # pragma: no cover
    os.system('cls' if os.name == 'nt' else 'clear')