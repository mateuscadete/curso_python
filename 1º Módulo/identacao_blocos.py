def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    print("Valor depositado!")
    print("Seu saldo é de:", saldo)

sacar(1000)
depositar(500)