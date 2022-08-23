a = float(input("DIGITE O VALOR DE A: "))
b = float(input("DIGITE O VALOR DE B: "))
c = float(input("DIGITE O VALOR DE C: "))

triangle = (a * c) / 2
circle = 3.14159 * (c**2)
trapez = ((a + b) * c) / 2
square = (b * b)
retangle = (a * b)

print(f"-> TRIANGULO: {round(triangle, 3)}")
print(f"-> CIRCULO: {round(circle, 3)}")
print(f"-> TRAPEZIO: {round(trapez, 3)}")
print(f"-> QUADRADO: {round(square, 3)}")
print(f"-> RETANGULO: {round(retangle, 3)}")
