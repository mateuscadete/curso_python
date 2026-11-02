MAIOR_IDADE = 18

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Menor de idade, não pode tirar a CNH.")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar a CNH.")
   