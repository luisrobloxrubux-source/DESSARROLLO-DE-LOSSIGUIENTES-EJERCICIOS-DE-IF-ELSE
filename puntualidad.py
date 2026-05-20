puntualidad = int(input("Puntualidad (0-10): "))
productividad = int(input("Productividad (0-10): "))
cumplimiento = int(input("Cumplimiento (0-10): "))

prom = (puntualidad + productividad + cumplimiento) / 3

if prom >= 9:
    print("Excelente")
elif prom >= 7:
    print("Bueno")
elif prom >= 5:
    print("Regular")
else:
    print("Deficiente")