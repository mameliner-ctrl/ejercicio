# Sistema de Gestión Eco-Camping

CAPACIDAD_MAXIMA = 15
vehiculos_acampando = 0

while True:
    print("\n===== ECO-CAMPING =====")
    print("1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Ver estado del camping")
    print("4. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))

        # REGISTRO DE INGRESO
        if opcion == 1:
            cantidad = int(input("¿Cuántos vehículos ingresan?: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor a cero.")

            elif vehiculos_acampando + cantidad > CAPACIDAD_MAXIMA:
                disponibles = CAPACIDAD_MAXIMA - vehiculos_acampando
                print(f"Error: capacidad excedida.")
                print(f"Solo quedan {disponibles} parcelas disponibles.")

            else:
                vehiculos_acampando += cantidad
                print(f"Ingreso registrado correctamente.")
                print(f"Vehículos acampando: {vehiculos_acampando}")

        # REGISTRO DE SALIDA
        elif opcion == 2:
            cantidad = int(input("¿Cuántos vehículos salen?: "))

            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor a cero.")

            elif cantidad > vehiculos_acampando:
                print("Error: no pueden salir más vehículos de los que hay.")

            else:
                vehiculos_acampando -= cantidad
                print("Salida registrada correctamente.")
                print(f"Vehículos acampando: {vehiculos_acampando}")

        # MOSTRAR ESTADO
        elif opcion == 3:
            disponibles = CAPACIDAD_MAXIMA - vehiculos_acampando

            print("\n===== ESTADO DEL CAMPING =====")
            print(f"Capacidad máxima: {CAPACIDAD_MAXIMA}")
            print(f"Parcelas ocupadas: {vehiculos_acampando}")
            print(f"Parcelas disponibles: {disponibles}")

        # SALIR
        elif opcion == 4:
            print("Gracias por usar el sistema Eco-Camping.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    # VALIDACIÓN ANTIERRORES
    except ValueError:
        print("Error: debe ingresar solo números.")