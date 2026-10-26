nome = "Mateus"
idade = 25
profissao = "Analista"
linguagem = "Python"
saldo = 45.435
dados = {"nome": "Mateus", "idade": 25, "profissao": "Analista", "linguagem": "Python"}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {1} Idade: {0} {0}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(idade=idade, nome=nome))

print("Nome: {name} Idade: {age} {age} {age}".format(age=idade, name=nome))

print("Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}".format(**dados))

print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem}")
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Profissão: {profissao} Linguagem: {linguagem} Saldo: {saldo:10.2f}")