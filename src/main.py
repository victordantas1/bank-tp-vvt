from utils import *


def main():
    lista_usuarios = cria_usuarios()
    lista_contas = cria_contas(lista_usuarios)

    while True:
        print("\n === Menu Principal ===")
        print("1 - Criar Conta")
        print("2 - Acessar Conta")
        print("3 - Deletar Conta")
        print("0 - Sair")
        opcao = int(input("Escolha uma opcao: "))

        match opcao:
            case 1:
                cria_conta(lista_usuarios, lista_contas)
            case 2:
                cpf = input("Digite o CPF: ")
                conta_encontrada = next((c for c in lista_contas if c.usuario.cpf == cpf), None)
                if conta_encontrada:
                    print(f"\n Bem-vindo(a), {conta_encontrada.usuario.nome.upper()} !")
                    print(f" Conta: {conta_encontrada.numero_conta}")
                    acessar_conta(conta_encontrada)

                else:
                    print("Conta não encontrada!")
            case 3:
                print("Saindo...")
                break

if __name__ == "__main__":
    main()