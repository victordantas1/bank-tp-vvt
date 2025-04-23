from utils import *

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
                cpf = input("Digite o CPF: ")
                conta_encontrada = busca_conta(lista_contas, cpf)
                if conta_encontrada:
                    print(f"\n Bem-vindo(a), {conta_encontrada.usuario.nome.upper()} !")
                    print(f" Conta: {conta_encontrada.numero_conta}")
                    acessar_conta(conta_encontrada, lista_contas)
                else:
                    print("Conta não encontrada!")


if __name__ == "__main__":
    main()