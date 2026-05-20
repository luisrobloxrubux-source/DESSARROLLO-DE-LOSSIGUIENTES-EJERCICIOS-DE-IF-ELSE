clave = input("Contraseña: ")

if len(clave) < 8:
    print("❌ Debe tener al menos 8 caracteres")
elif not any(c.isupper() for c in clave):
    print("❌ Falta mayúscula")
elif not any(c.isdigit() for c in clave):
    print("❌ Falta número")
elif not any(not c.isalnum() for c in clave):
    print("❌ Falta símbolo")
else:
    print("✅ Contraseña segura")
