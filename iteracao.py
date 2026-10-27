#Exercícios de fixação

#Escreva um programa que peça uma palavra ao usuário e imprima cada letra em uma linha separada.
def imprime_letras(palavra):
    for letra in palavra:
        print(letra)

palavra = input("Digite uma palavra: ")

imprime_letras(palavra)


# Escreva um programa que peça uma palavra ao usuário e conte quantas vezes a letra a aparece nela (maiúscula ou minúscula).

def conta_letra(palavra, letra):
    contador = 0
    for char in palavra:
        if char.lower() == letra.lower():
            contador += 1
    return contador

palavra = input("Digite uma palavra: ")
letra = input("Digite a letra que deseja contar: ")

print(f"A letra '{letra}' aparece {conta_letra(palavra, letra)} vez(es).")

# Escreva um programa que peça uma frase ao usuário e conte quantas palavras ela tem, 
# sem usar .split(). Mas aqui vai uma pista de raciocínio: se você contar os espaços (" ")
# na frase, quantas palavras existem em relação ao número de espaços?

def conta_palavras(frase):
    contador = 0
    for char in frase:
        if char == " ":
            contador += 1
        
    return contador + 1

frase = input("Digite uma frase: ")
print(f"A frase digitada possui {conta_palavras(frase)} palavra(s).")