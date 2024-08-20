class Cliente:
    def get_desconto(self):
        return 0.0


class ClienteRegular(Cliente):
    def get_desconto(self):
        return 0.1

class ClientePremium(Cliente):
    def get_desconto(self):
        return 0.1


class ClientePromocional(Cliente):
    def get_desconto(self):
        return 0.15



c1 = ClienteRegular()
c2 = ClientePremium()
c3 = Cliente()
c4 = ClientePromocional()

print(c1.get_desconto())
print(c2.get_desconto())
print(c3.get_desconto())
print(c4.get_desconto())