from datetime import date
from mongoengine import Document, StringField, DateTimeField

class Usuario(Document):
    nome = StringField()
    email = StringField()
    senha = StringField()
    cpf = StringField()
    data_nascimento = DateTimeField()