from typing import List

from conta import Conta
from usuario import Usuario
from datetime import date

numero_conta_atual = 1011
AGENCIA_CONTA = "1234-5"
NUMERO_BANCO = "001"
NOME_BANCO = "Banco VVT"


def cria_usuarios() -> List[Usuario]:
    return [
        Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10)),
        Usuario("Bruno Souza", "bruno.souza@example.com", "senha456", "23456789012", date(1985, 7, 22)),
        Usuario("Carlos Lima", "carlos.lima@example.com", "abc12345", "34567890123", date(1992, 2, 28)),
        Usuario("Daniela Rocha", "daniela.rocha@example.com", "minhasenha", "45678901234", date(1988, 11, 3)),
        Usuario("Eduardo Mendes", "eduardo.mendes@example.com", "segredo789", "56789012345", date(1995, 1, 15)),
        Usuario("Fernanda Dias", "fernanda.dias@example.com", "123senha", "67890123456", date(1993, 7, 19)),
        Usuario("Gabriel Torres", "gabriel.torres@example.com", "senha321", "78901234567", date(1991, 4, 2)),
        Usuario("Helena Costa", "helena.costa@example.com", "super1234", "89012345678", date(1989, 12, 8)),
        Usuario("Igor Barbosa", "igor.barbosa@example.com", "meusegredo", "90123456789", date(1994, 6, 25)),
        Usuario("Julia Fernandes", "julia.fernandes@example.com", "senha777", "01234567890", date(1996, 9, 12)),
    ]


def cria_contas(usuarios: List[Usuario]) -> List[Conta]:
    return [
        Conta(
            numero_conta=numero_conta_atual + i,
            agencia_conta="1234-5",
            numero_banco="001",
            nome_banco="Banco VVT",
            usuario=usuario,
            saldo=1000,
            data_criacao=date.today(),
            ativa=True
        )
        for i, usuario in enumerate(usuarios)
    ]

def imprime_menu(): # pragma: no cover
    print("\n === Menu Principal ===")
    print("1 - Criar Conta")
    print("2 - Acessar Conta")
    print("3 - Deletar Conta")
    print("0 - Sair")

def imprime_menu_conta(conta: Conta) -> None: # pragma: no cover
    print(f"\n=== Menu de {conta.usuario.nome.upper()} ===")
    print(f"\nSaldo Atual: {conta.get_saldo()}")
    print("1 - Fazer Saque")
    print("2 - Fazer Deposito")
    print("3 - Fazer Tranferencia")
    print("4 - Verificar se Saldo esta negativo")
    print("0 - Voltar")

def busca_conta(lista_contas: List[Conta], cpf: str) -> Conta:
    return next((c for c in lista_contas if c.usuario.cpf == cpf), None)

def acessar_conta(conta: Conta, lista_contas: List[Conta]) -> None:  # pragma: no cover
    while True:
        imprime_menu_conta(conta)
        opcao = int(input("Escolha uma opcao: "))
        match opcao:
            case 0:
                break
            case 1:
                valor = int(input("Digite o valor: "))
                try:
                    saldo = conta.saque(valor)
                    print(f"Saque de R$ {valor} realizado com sucesso.")
                    print(f"Saldo restante: {saldo}")
                except Exception as error:
                    print(error)
            case 2:
                valor = int(input("Digite o valor: "))
                try:
                    saldo = conta.deposito(valor)
                    print(f"Deposito de R$ {valor} realizado com sucesso.")
                    print(f"Saldo Atual: {saldo}")
                except Exception as error:
                    print(error)
            case 3:
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
            case 4:
                print(f"Saldo negativo. Saldo Atual: {conta.get_saldo()}") if conta.saldo_negativo() else print(f"Saldo Positivo. Saldo Atual: {conta.get_saldo()}")


def cria_conta(lista_usuarios: List[Usuario], lista_contas: List[Conta]) -> Conta: # pragma: no cover
    global numero_conta_atual
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

    return nova_conta