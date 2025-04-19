import pytest
from datetime import date
from src.usuario import Usuario
from src.conta import Conta

class TestConta:

    @pytest.fixture
    def usuario_exemplo(self):
        return Usuario("Ana Silva", "ana.silva@example.com", "senha123", "12345678901", date(1990, 5, 10))

    @pytest.fixture
    def conta_exemplo(self, usuario_exemplo):
        return Conta(1001, "1234-5", "001", "Banco Exemplo", usuario_exemplo, 1000.0, date.today(), True)

    def test_get_saldo(self, conta_exemplo):
        assert 1000.0 == conta_exemplo.get_saldo()

