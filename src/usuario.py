from __future__ import annotations

from datetime import date
from typing import List

from mongoengine import Document, StringField, DateTimeField, IntField


class Usuario(Document):
    nome = StringField(required=True)
    email = StringField(required=True, unique=True)
    senha = StringField(required=True) 
    cpf = StringField(required=True, unique=True)
    data_nascimento = DateTimeField(required=True)

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Email: {self.email}, CPF: {self.cpf}, Data: {self.data_nascimento}'

    @staticmethod
    def insert_all_users(usuarios: List[Usuario]):
        for usuario in usuarios:
            usuario.save()

    @staticmethod
    def get_all_users():
        return Usuario.objects.all()

    @staticmethod
    def get_by_cpf(cpf: str):
        return Usuario.objects.get(cpf=cpf)