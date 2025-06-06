"""
def boasVindas(nome):
    print(f"ola,{nome}!")

boasVindas("Felipe")
"""

def multiplo_de (numero, multiplo) :
    resultado = numero % multiplo == 0
    print(F"{numero} é multiplo de {multiplo} ?", end = " ")
    print(resultado)

    multiplo_de (16,8)
    multiplo_de (15,3)
    multiplo_de (353,7)
