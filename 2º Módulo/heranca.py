class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor do veículo")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto = Motocicleta("vermelha", "ABC1234", 2)
moto.ligar_motor()

carro = Carro("azul", "XYZ5678", 4)
carro.ligar_motor()

caminhao = Caminhao("preto", "LMN9012", 6)
caminhao.ligar_motor()