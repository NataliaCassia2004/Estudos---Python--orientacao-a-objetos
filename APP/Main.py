class Main:
    pass

from Conta import Conta
from Cliente import Cliente

c1 = Cliente("Tabita","1148213800")

print(c1)
print(c1._nome,c1._telefone)

c2 = Conta(c1.get_nome(),"1111",1222)

c2.saque(2000)