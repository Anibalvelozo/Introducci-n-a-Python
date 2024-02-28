print("Este programa calcula las utilidades de un proyecto comparadas con el año anterior.")
print("Por favor, ingrese solo numeros")
print("Por favor, ingrese los siguientes datos:")

    # Solicitar al usuario que ingrese el precio de suscripción, número de usuarios, gastos totales y utilidades del año anterior
precio_suscripcion = float(input("Ingrese el precio de suscripción: "))
num_usuarios = int(input("Ingrese el número de usuarios: "))
gastos_totales = float(input("Ingrese los gastos totales: "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior: "))

    # Calcular las utilidades actuales
utilidades_actuales = precio_suscripcion * num_usuarios - gastos_totales

    # Calcular la razón entre las utilidades actuales y las del año anterior
razon_utilidades = utilidades_actuales / utilidades_anterior

    # Mostrar el resultado
print(f"Las utilidades del proyecto este año son: {utilidades_actuales}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")
