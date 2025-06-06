lista_funcionarios = []
for i in range (4) : 
    funcionario = {}
    funcionario ['nome'] = input("Digite o nome do funcionario : ")
    funcionario ['funcao'] = input("Digite a funcao ") 
    funcionario ['salario'] = float(input ("Digite o salario do funcionario : ")) 
    lista_funcionarios .append(funcionario) 

maior_salario = lista_funcionarios[0] 
for i in ranger (4) : 
    if lista_funcionarios[i] ['salario'] > maior_salario['salario'] :
        maior_salario + lista_funcionarios[i]

print(maior_salario)














