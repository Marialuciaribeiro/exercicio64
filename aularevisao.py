"""
print("maria") # O print imprime valores no terminal
input("digite seu nome: ") # O input recebe os valores que o usuario digitar no terminal
print(10 ) 
"""
# Variáveis -> são as estruras do programa para salvar valores de diversos tipos 
"""
Os tipos são ?
int -> numeros inteiros 

"""
"""
numero = int(input("insira um numero"))
antecessor = numero - 1
sucessor = numero + 1

print("Antecessor:" ,antecessor,"\nSucessor:" ,sucessor)

if  numero > 0: 
    print("antecessor:",antecessor, "\nSucessor:" ,sucessor)

else:
    print("o numero invalido,pois o numero é negativo")
    
"""
'''
km = float(input("digite a distancia"))
litros = float(input("digite os litros"))   

media = km/litros

print(f"o consumo medio e:{media:.2f}")

'''
'''
altura = float(input("digite a altura"))
largura = float(input("digite a largura"))

area = altura*largura

print(f"a area do retangulo e:{area:.1f}")

'''

"""
fah = float(input("digite o fahrenheit"))

celsius = (5/9)*(fah-32)

print(f"o valor de celsius e:{celsius:.0f}")
"""
produto = input("digite o produto")
quantidade = input("digete a quantidade")
valor = float(input("digite o valor"))
desconto = input("digite o desconto")

valor_total_das_vendas = valor*quantidade
desconto = valor_total_das_vendas*desconto 
valor_com_desconto = valor_total_das_vendas - desconto

print(f"o valor total da venda e:{valor_total_das_vendas}")























