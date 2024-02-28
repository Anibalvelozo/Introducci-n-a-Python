import math as m

print("Este programa calcula la velocidad de escape de un planeta.")
print("Por favor, ingrese los siguientes datos:")

    # Solicitar al usuario que ingrese el radio en kilómetros
radio_km = float(input("Ingrese el radio del planeta en kilómetros: "))
    
    # Convertir el radio de kilómetros a metros
radio_m = radio_km * 1000
    
    # Solicitar al usuario que ingrese la constante gravitacional
g = float(input("Ingrese la constante gravitacional en m/s2: "))

    # Calcular la velocidad de escape
velocidad_escape = m.sqrt(2 * g * radio_m)

    # Mostrar el resultado
print(f"La velocidad de escape es {velocidad_escape:.1f} [m/s]")


