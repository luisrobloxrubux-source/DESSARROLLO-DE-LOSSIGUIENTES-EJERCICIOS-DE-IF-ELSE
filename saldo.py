saldo = 1000
pin_correcto = "1234"
intentos = 0
limite = 500

while intentos < 3:
    pin = input("Ingrese PIN: ")
    if pin == pin_correcto:
        print("✅ Acceso concedido")
        op = input("1.Retirar 2.Ver saldo: ").strip()
        
        if op == "1":
            try:
                monto = float(input("Monto: "))
            except ValueError:
                print("Error: El monto debe ser un valor numérico.")
                break
                
            if monto <= 0:
                print("❌ Monto inválido")
            elif monto > limite:
                print("❌ Supera límite diario")
            elif monto > saldo:
                print("❌ Fondos insuficientes")
            else:
                saldo -= monto
                print(f"✅ Retiro exitoso. Saldo: {saldo}")
        elif op == "2":
            print(f"Saldo: {saldo}")
        break
    else:
        intentos += 1
        print(f"❌ PIN incorrecto. Intentos restantes: {3 - intentos}")

if intentos == 3:
    print("🚫 Cuenta bloqueada")
