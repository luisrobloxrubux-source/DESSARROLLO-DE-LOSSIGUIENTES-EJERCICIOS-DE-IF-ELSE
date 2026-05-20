n = int(input("Número: "))

# Positivo, negativo o cero
if n > 0:
    print("Positivo")
elif n < 0:
    print("Negativo")
else:
    print("Cero")

# Par o impar
if n % 2 == 0:
    print("Par")
else:
    print("Impar")

# Múltiplos
if n % 3 == 0 and n % 5 == 0:
    print("Múltiplo de 3 y 5")
elif n % 3 == 0:
    print("Múltiplo de 3")
elif n % 5 == 0:
    print("Múltiplo de 5")