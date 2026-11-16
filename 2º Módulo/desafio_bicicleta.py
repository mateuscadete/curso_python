class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Biiiiiiii")

    def parar(self):
        print("Parando a bicicleta")

    def correr(self):
        print("A bicicleta está correndo")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2020, 1000)
print(b1)
b1.buzinar()
b1.parar()
b1.correr()

print(b1.__str__())
