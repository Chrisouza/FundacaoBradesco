from Cliente import Cliente
from Conta import Conta


class Main:
    pass


c1 = Cliente("João", "114444-2222")
conta = Conta(c1._nome, 6565, 0)

conta.deposita(100)
conta.saque(50)
conta.extrato()
