try:
    promedio = float(input("Promedio: "))
    ingresos_bajos = input("¿Ingresos bajos? (si/no): ").strip().lower()
    cursos = int(input("Cursos desaprobados: "))
except ValueError:
    print("Error: El promedio y los cursos deben ser valores numéricos.")
    exit()

if promedio >= 16 and ingresos_bajos == "si" and cursos <= 2:
    print("✅ Beca completa")
elif promedio >= 16 and (ingresos_bajos == "si" or cursos <= 1):
    print("⚠️ Media beca")
else:
    print("❌ No aplica")