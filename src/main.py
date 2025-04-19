from conta import Conta
from usuario import Usuario
from datetime import date

def usuarios(self):
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


def contas(self, usuarios):
    return [
        Conta(
            numero_conta=1001 + i,
            agencia_conta="1234-5",
            numero_banco="001",
            nome_banco="Banco VVT",
            usuario=usuario,
            saldo=0,
            data_criacao=date.today(),
            ativa=True
        )
        for i, usuario in enumerate(usuarios)
    ]

def main():
        pass

if __name__ == "__main__":
    main()
