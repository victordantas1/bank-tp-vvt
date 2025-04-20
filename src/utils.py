from datetime import datetime, date
from typing import List
from mongoengine import connect

from conta import Conta
from usuario import Usuario

def connect_to_db(db_uri: str) -> None:
    connect(host=db_uri)


def cria_usuarios() -> List[Usuario]:
    return [
        Usuario(nome="Ana Silva", email="ana.silva@example.com", senha="senha123", cpf="12345678901", data_nascimento=date.today()),
        Usuario(nome="Bruno Souza", email="bruno.souza@example.com", senha="senha456", cpf="23456789012", data_nascimento=date.today()),
        Usuario(nome="Carlos Lima", email="carlos.lima@example.com", senha="abc12345", cpf="34567890123", data_nascimento=date.today()),
        Usuario(nome="Daniela Rocha", email="daniela.rocha@example.com", senha="minhasenha", cpf="45678901234", data_nascimento=date.today()),
        Usuario(nome="Eduardo Mendes", email="eduardo.mendes@example.com", senha="segredo789", cpf="56789012345", data_nascimento=date.today()),
        Usuario(nome="Fernanda Dias", email="fernanda.dias@example.com", senha="123senha", cpf="67890123456", data_nascimento=date.today()),
        Usuario(nome="Gabriel Torres", email="gabriel.torres@example.com", senha="senha321", cpf="78901234567", data_nascimento=date.today()),
        Usuario(nome="Helena Costa", email="helena.costa@example.com", senha="super1234", cpf="89012345678", data_nascimento=date.today()),
        Usuario(nome="Igor Barbosa", email="igor.barbosa@example.com", senha="meusegredo", cpf="90123456789", data_nascimento=date.today()),
        Usuario(nome="Julia Fernandes", email="julia.fernandes@example.com", senha="senha777", cpf="01234567890", data_nascimento=date.today())
    ]


def cria_contas(usuarios: List[Usuario]) -> List[Conta]:
    return [
        Conta(
            numero_conta=1001 + i,
            agencia_conta="1234-5",
            numero_banco="001",
            nome_banco="Banco VVT",
            usuario=usuario,
            saldo=0,
            data_criacao=datetime.now(),
            ativa=True
        )
        for i, usuario in enumerate(usuarios)
    ]


if __name__ == '__main__':
    db_uri = 'mongodb://localhost:27018/bank-vvt'
    connect_to_db(db_uri)
    usuarios = cria_usuarios()
    Usuario.insert_all_users(usuarios)
    Conta.insert_all_contas(cria_contas(usuarios))
    