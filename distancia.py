distancia = float(input("Distancia (km): "))
tipo = input("Tipo (estudiante/adulto/mayor): ").lower()
horario = input("Horario (normal/nocturno): ").lower()

costo = distancia * 2

if tipo == "estudiante":
    costo *= 0.5
elif tipo == "mayor":
    costo *= 0.7

if horario == "nocturno":
    costo *= 1.2

print("Costo:", costo)