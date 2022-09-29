codA =int(input("DIGITE O CODIGO D0 PRODUTO 1: "))
unitA = int(input("DIGITE O NUMERO DE UNIDADES D0 PRODUTO 1: "))
priceA = float(input("DIGITE O PREÇO DE UMA UNIDADE DO PRODUTO 1: "))

codB =int(input("DIGITE O CODIGO D0 PRODUTO 2: "))
unitB = int(input("DIGITE O NUMERO DE UNIDADES D0 PRODUTO 2: "))
priceB = float(input("DIGITE O PREÇO DE UMA UNIDADE DO PRODUTO 2: "))

result = (unitA * priceA) + (unitB * priceB)
print (f"VALOR A PAGAR: R$ {result}")