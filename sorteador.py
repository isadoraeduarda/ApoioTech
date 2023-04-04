from random import choice

pessoas = []

quantidade_de_pessoas_sorteadas = int(input("Digite o numero de pessoas que deseja sortear: "))

count = 0 

while True: 
    pessoa = input ("Digite o nome de uma pessoa: ")

    count = count + 1

    if pessoa == "finalizei":
        break

    pessoas.append(pessoa)

for _ in range (quantidade_de_pessoas_sorteadas):
    pessoa_sorteada = choice(pessoas)
    print (pessoa_sorteada)

#melhorar: sortear pessoas diferentes.

