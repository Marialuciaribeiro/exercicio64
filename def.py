def exibeMenu ():
    print("### menu ###") 
    print("0_sair\n")
    print("1_somar\n")
    print("2_subtrair\n")
    print("3_multiplicar\n")
    print("4_dividir\n1") 
    opcao = int (input("escolha uma opcao : ")) 
    return opcao

def somar (numero1, numero2): 
    resultado = numero1+numero2
    return resultado 

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado 

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    resultado = num1 / num2
    return resultado


i=0
opcao=1
num1=0
num2=0
resultado=0

while opcao !=0: 
    opcao = exibeMenu()
    if opcao <= 0:
        break

    num1= float(input("Informe o primeiro numero para a operacao: ")) 
    num2= float(input('Informe o segundo numero para a operacao: '))
    if opcao == 1: 
        resultado = somar(num1, num2) 
    elif opcao == 2:
        resultado = subtrair(num1, num2)
    elif opcao == 3:
        resultado = multiplicar(num1, num2)
    elif opcao == 4:
        resultado = dividir(num1, num2)
    print ("Resultado : %f\n\n" %resultado)

    
