import time

from utils import *
import os


def main():
    lista_usuarios = cria_usuarios()
    lista_contas = cria_contas(lista_usuarios)

    while True:
        imprime_menu()
        opcao = int(input("Escolha uma opcao: "))
        match opcao:
            case 0:
                print("Saindo...")
                break
            case 1:
                cria_conta(lista_usuarios, lista_contas)
            case 2:
                acessar_conta(lista_contas)

if __name__ == "__main__":
    main()