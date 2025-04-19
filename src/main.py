from conta import Conta
from usuario import Usuario
from datetime import date

usuarios = [
    Usuario("Ana Silva", 1500.0, "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10)),
    Usuario("Bruno Souza", 800.5, "bruno.souza@example.com", "senha456", "23456789012", date(1985, 8, 22)),
    Usuario("Carlos Lima", 120.0, "carlos.lima@example.com", "abc12345", "34567890123", date(1992, 2, 28)),
    Usuario("Daniela Rocha", 2500.75, "daniela.rocha@example.com", "minhasenha", "45678901234", date(1988, 11, 3)),
    Usuario("Eduardo Mendes", 0.0, "eduardo.mendes@example.com", "segredo789", "56789012345", date(1995, 1, 15)),
    Usuario("Fernanda Dias", 934.40, "fernanda.dias@example.com", "123senha", "67890123456", date(1993, 7, 19)),
    Usuario("Gabriel Torres", 3120.90, "gabriel.torres@example.com", "senha321", "78901234567", date(1991, 4, 2)),
    Usuario("Helena Costa", 1040.30, "helena.costa@example.com", "super1234", "89012345678", date(1989, 12, 8)),
    Usuario("Igor Barbosa", 160.0, "igor.barbosa@example.com", "meusegredo", "90123456789", date(1994, 6, 25)),
    Usuario("Julia Fernandes", 720.55, "julia.fernandes@example.com", "senha777", "01234567890", date(1996, 9, 12)),
]

contas = []

for i, usuario in enumerate(usuarios):
    conta = Conta(
        numero_conta=1001 + i,
        agencia_conta="1234-5",
        numero_branco="001",
        nome_branco="Banco VVT",
        usuario=usuario,
        saldo=usuario.saldo,
        data_criacao=date.today(),
        ativa=True
    )
    contas.append(conta)

def main():
        pass

if __name__ == "__main__":
    main()
