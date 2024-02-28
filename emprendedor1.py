print("Este programa calcula las utilidades de un proyecto.")
print("Por favor, ingrese solo numeros")
print("Por favor, ingrese los siguientes datos:")

    # Solicitar al usuario que ingrese el precio de suscripción, número de usuarios y gastos totales
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
num_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

    # Calcular las utilidades
utilidades = precio_suscripcion * num_usuarios - gastos_totales

    # Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades}")