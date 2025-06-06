
cal = float(input("digite o numero: "))
calculo = float(input("digite o numero: "))
operacao = input( "+,-,*,/ : ")

if operacao == "+":
    print(f"resultado {cal + calculo:.2f}" )
elif operacao == "-" :
    print(f"resultado {cal - calculo:.2f}" )
elif operacao == "*":
    print(f"resultado {cal*calculo:.2f}")
elif operacao == "/":
    if calculo != 0:
        print(f"resultado {cal/calculo:.2f}" )
    else:
        print ("nao pode dividir por zero." )
    




















