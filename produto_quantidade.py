produto = input("digite o produto: ")
valor = float(input("digite o valor do produto: "))
quantidade = int(input("digite a quantidade : "))
desconto = float(input("digite o desconto do produto: "))

pagamento = (valor * (100 - desconto) /100) * quantidade

print(f"o valor da compra do {produto} ficou:{pagamento:.2f}")