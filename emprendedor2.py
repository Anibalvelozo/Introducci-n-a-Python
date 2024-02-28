print("Este programa calcula las utilidades de un proyecto con usuarios normales y premium.")
print("Por favor, ingrese solo numeros")
print("Por favor, ingrese los siguientes datos:")

    # Solicitar al usuario que ingrese los precios de suscripción, número de usuarios normales y premium, y gastos totales
precio_suscripcion_normal = float(input("Ingrese el precio de suscripción para usuarios normales: "))
precio_suscripcion_premium = float(input("Ingrese el precio de suscripción para usuarios premium: "))
num_usuarios_normal = int(input("Ingrese el número de usuarios normales: "))
num_usuarios_premium = int(input("Ingrese el número de usuarios premium: "))
gastos_totales = float(input("Ingrese los gastos totales: "))

    # Calcular las utilidades
utilidades = (precio_suscripcion_normal * num_usuarios_normal + precio_suscripcion_premium * num_usuarios_premium) - gastos_totales

    # Mostrar el resultado
print(f"Las utilidades del proyecto son: {utilidades}")