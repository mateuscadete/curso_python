texto = input("informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha após o loop

# Exemplo utilizando a função range()
for numero in range(0, 51, 5):
    print(numero, end=" ")
