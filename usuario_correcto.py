usuario_correcto = "admin"
clave_correcta = "1234"
intentos = 0

while intentos < 3:
    u = input("Usuario: ")
    c = input("Contraseña: ")

    if u == usuario_correcto and c == clave_correcta:
        print("✅ Bienvenido")
        break
    else:
        intentos += 1
        print("❌ Datos incorrectos")

if intentos == 3:
    print("🚫 Cuenta bloqueada")