# Programa de clasificación de riesgo crediticio

try:
    ingreso = float(input("Ingrese el ingreso mensual: "))
    historial = input("Ingrese el historial crediticio (bueno, regular, malo): ").strip().lower()
    edad = int(input("Ingrese la edad: "))
except ValueError:
    print("Error: El ingreso y la edad deben ser valores numéricos.")
    exit()

if historial == "bueno":
    if ingreso >= 3000 and edad >= 25:
        riesgo = "Bajo"
    else:
        riesgo = "Medio"

elif historial == "regular":
    if ingreso >= 3000 and edad >= 30:
        riesgo = "Medio"
    else:
        riesgo = "Alto"

elif historial == "malo":
    if ingreso >= 5000 and edad >= 35:
        riesgo = "Medio"
    else:
        riesgo = "Alto"

else:
    riesgo = "Datos inválidos (historial no reconocido)"

print(f"El nivel de riesgo crediticio es: {riesgo}")
