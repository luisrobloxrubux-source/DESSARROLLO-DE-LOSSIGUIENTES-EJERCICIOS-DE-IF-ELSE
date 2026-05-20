try:
    ingreso = float(input("Ingreso: "))
except ValueError:
    print("Error: El ingreso debe ser un valor numérico.")
    exit()

if ingreso < 0:
    print("❌ Ingreso inválido")
else:
    if ingreso <= 1000:
        impuesto = ingreso * 0.05
    elif ingreso <= 5000:
        impuesto = ingreso * 0.10
    else:
        impuesto = ingreso * 0.20

    print(f"Impuesto: {impuesto}")
