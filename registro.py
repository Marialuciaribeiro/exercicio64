frase = input("frase : ")
palavra = frase.split()
conta = {}

for i in palavra :
    if i in conta :
        conta[i] += 1 

    else: 
        conta[i] = 1

for palavra, valor in conta.iteams():
    print(f"{palavra}: {valor}")