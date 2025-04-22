from conta import Conta
from src.exceptions.conta_exceptions import SaldoInsuficienteError, ValorInvalidoError
from usuario import Usuario
from datetime import date

numero_conta_atual = 1011
AGENCIA_CONTA ="1234-5"
NUMERO_BANCO ="001"
NOME_BANCO ="Banco VVT"

def cria_usuarios():
    return [
        Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10)),
        Usuario("Bruno Souza", "bruno.souza@example.com", "senha456", "23456789012", date(1985, 8, 22)),
        Usuario("Carlos Lima", "carlos.lima@example.com", "abc12345", "34567890123", date(1992, 2, 28)),
        Usuario("Daniela Rocha", "daniela.rocha@example.com", "minhasenha", "45678901234", date(1988, 11, 3)),
        Usuario("Eduardo Mendes", "eduardo.mendes@example.com", "segredo789", "56789012345", date(1995, 1, 15)),
        Usuario("Fernanda Dias", "fernanda.dias@example.com", "123senha", "67890123456", date(1993, 7, 19)),
        Usuario("Gabriel Torres", "gabriel.torres@example.com", "senha321", "78901234567", date(1991, 4, 2)),
        Usuario("Helena Costa", "helena.costa@example.com", "super1234", "89012345678", date(1989, 12, 8)),
        Usuario("Igor Barbosa", "igor.barbosa@example.com", "meusegredo", "90123456789", date(1994, 6, 25)),
        Usuario("Julia Fernandes", "julia.fernandes@example.com", "senha777", "01234567890", date(1996, 9, 12)),
    ]


def cria_contas(cria_usuarios):
    return [
        Conta(
            numero_conta= numero_conta_atual + i,
            agencia_conta="1234-5",
            numero_banco="001",
            nome_banco="Banco VVT",
            usuario=usuario,
            saldo=1000,
            data_criacao=date.today(),
            ativa=True
        )
        for i, usuario in enumerate(cria_usuarios)
    ]


def acessar_conta(conta_encontrada):
    while True:
        print(f"\n === Menu Usuário de {conta_encontrada.usuario.nome} ===")
        print(f"\nSaldo Atual: {conta_encontrada.get_saldo()}")
        print("1 - Fazer Saque")
        print("2 - Fazer Deposito")
        print("0 - Voltar")
        opcaoConta = input("Escolha uma opcao: ")

        if opcaoConta == "1":
            valor = int(input("Digite o valor: "))
            try:
                saldo = conta_encontrada.saque(valor)
                print(f"Saque de R$ {valor} realizado com sucesso.")
                print(f"Saldo restante: {saldo}")
            except Exception as error:
                print(error)
        if opcaoConta == "2":
            valor = int(input("Digite o valor: "))
            try:
                saldo = conta_encontrada.deposito(valor)
                print(f"Deposito de R$ {valor} realizado com sucesso.")
                print(f"Saldo Atual: {saldo}")
            except Exception as error:
                print(error)
        if opcaoConta == "0":
            break


def cria_conta(lista_usuarios, lista_contas):
    nome = input("Digite seu nome: ")
    email = input("Digite sua e-mail: ")

    data_nascimento = date.fromisoformat(input("Digite sua data de nascimento: (ano-mes-dia): "))
    senha = input("Digite sua senha: ")
    cpf = input("Digite sua cpf: ")

    novo_usuario = Usuario(nome, email, senha, cpf, data_nascimento)
    lista_usuarios.append(novo_usuario)
    nova_conta = Conta(numero_conta_atual, AGENCIA_CONTA, NUMERO_BANCO, NOME_BANCO, novo_usuario, 0, date.today(), True)
    lista_contas.append(nova_conta)
    numero_conta_atual += 1

    print(f"\nConta criada com sucesso.\n")


def main():
    lista_usuarios = cria_usuarios()
    lista_contas = cria_contas(lista_usuarios)

    while True:
        print("\n === Menu Principal ===")
        print("1 - Criar Conta")
        print("2 - Acessar Conta")
        print("3 - Deletar Conta")
        print("0 - Sair")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            cria_conta(lista_usuarios, lista_contas)

        if opcao == "2":
            cpf = input("Digite o CPF: ")
            conta_encontrada = next((c for c in lista_contas if c.usuario.cpf == cpf), None)
            if conta_encontrada:
                print(f"\n Bem-vindo(a), {conta_encontrada.usuario.nome} !")
                print(f" Conta: {conta_encontrada.numero_conta}")
                acessar_conta(conta_encontrada)

            else:
                print("Conta não encontrada!")
        if opcao == "0":
            print("Saindo...")
            break

if __name__ == "__main__":
    main()