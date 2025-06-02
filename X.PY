# Datos normalizados
veterinarios = [
    "Neiner, Maximiliano",
    "Villegas, Octavio",
    "Cardozo, Marina",
    "Baus, Christian",
    "Luccheta, Giovanni",
    "Fernandez, David",
    "Ochoa, Gonzalo",
    "Gatto, Catriel",
    "Fernandez, Mariano",
    "Bustos Gil, Felipe"
]

servicios = [
    "Consulta General",
    "Vacunacion",
    "Control Post-Quirurgico"
]

precios = [15000, 20000, 30000]

# Matriz de turnos [10][3]
turnos = [
    [0, 0, 0],  # Neiner
    [0, 0, 0],  # Villegas
    [0, 0, 0],  # Cardozo
    [0, 0, 0],  # Baus
    [0, 0, 0],  # Luccheta
    [0, 0, 0],  # Fernandez D
    [0, 0, 0],  # Ochoa
    [0, 0, 0],  # Gatto
    [0, 0, 0],  # Fernandez M
    [0, 0, 0]   # Bustos
]

# --------------------- FUNCIONES ---------------------

def buscar_veterinario(nombre):
    i = 0
    while i < 10:
        if nombre == veterinarios[i]:
            return i
        i += 1
    return -1

def buscar_servicio(nombre_serv):
    i = 0
    while i < 3:
        if nombre_serv == servicios[i]:
            return i
        i += 1
    return -1

def registrar_turno():
    print("\n-- REGISTRO DE TURNOS --")
    nombre = input("Ingrese el nombre completo del veterinario (Ej: Fernandez, David): ")
    pos_vet = buscar_veterinario(nombre)
    if pos_vet == -1:
        print("Veterinario no encontrado.")
        return
    
    servicio = input("Ingrese el tipo de servicio (Consulta General, Vacunacion, Control Post-Quirurgico): ")
    pos_serv = buscar_servicio(servicio)
    if pos_serv == -1:
        print("Servicio no válido.")
        return

    cantidad = input("Ingrese la cantidad de turnos (1 a 10): ")
    if not cantidad.isdigit():
        print("Cantidad no válida.")
        return
    cantidad = int(cantidad)
    if cantidad < 1 or cantidad > 10:
        print("Cantidad fuera de rango.")
        return

    turnos[pos_vet][pos_serv] += cantidad
    total = cantidad * precios[pos_serv]
    print("Turno registrado. Total a pagar: $", total)

def ordenar_indices_por_nombre(indices):
    i = 0
    while i < 9:
        j = i + 1
        while j < 10:
            if veterinarios[indices[i]] > veterinarios[indices[j]]:
                aux = indices[i]
                indices[i] = indices[j]
                indices[j] = aux
            j += 1
        i += 1

def mostrar_datos_ordenados():
    print("-- DATOS DE TURNOS ORDENADOS A-Z --")
    print("Veterinario               Servicio                   Precio     Turnos")
    print("-----------------------------------------------------------------------")
    
    indices = [0,1,2,3,4,5,6,7,8,9]
    ordenar_indices_por_nombre(indices)

    i = 0
    while i < 10:
        vet = indices[i]
        j = 0
        while j < 3:
            print(f"{veterinarios[vet]:25} {servicios[j]:25} ${precios[j]:<10} {turnos[vet][j]}")
            j += 1
        i += 1

def mostrar_submenu_consultas():
    while True:
        print("\n-- CONSULTAS --")
        print("1. Total de turnos por veterinario")
        print("2. Promedio de turnos por tipo de servicio")
        print("3. Recaudación total")
        print("4. Veterinarios ordenados alfabéticamente con recaudación")
        print("5. Porcentaje de cada tipo de servicio respecto al total de turnos")
        print("6. Veterinario con menor cantidad total de turnos")
        print("7. Porcentaje de turnos por veterinario respecto al total")
        print("8. Servicio(s) más solicitado(s) por cada veterinario")
        print("9. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Turnos por veterinario:")
            i = 0
            while i < 10:
                total = turnos[i][0] + turnos[i][1] + turnos[i][2]
                print(f"{veterinarios[i]:25}: {total} turnos")
                i += 1

        elif opcion == "2":
            print("\nPromedio de turnos por tipo de servicio:")
            totales_serv = [0,0,0]
            i = 0
            while i < 10:
                j = 0
                while j < 3:
                    totales_serv[j] += turnos[i][j]
                    j += 1
                i += 1
            j = 0
            while j < 3:
                promedio = totales_serv[j] / 10
                print(f"{servicios[j]:25}: {promedio:.2f}")
                j += 1

        elif opcion == "3":
            total_recaudado = 0
            i = 0
            while i < 10:
                j = 0
                while j < 3:
                    total_recaudado += turnos[i][j] * precios[j]
                    j += 1
                i += 1
            print(f"\nRecaudación total: ${total_recaudado}")

        elif opcion == "4":
            print("\nVeterinarios ordenados alfabéticamente con recaudación:")
            indices = [0,1,2,3,4,5,6,7,8,9]
            ordenar_indices_por_nombre(indices)
            i = 0
            while i < 10:
                vet = indices[i]
                recaudacion_vet = 0
                j = 0
                while j < 3:
                    recaudacion_vet += turnos[vet][j] * precios[j]
                    j += 1
                print(f"{veterinarios[vet]:25}: ${recaudacion_vet}")
                i += 1

        elif opcion == "5":
            print("\nPorcentaje de cada tipo de servicio respecto al total de turnos:")
            totales_serv = [0,0,0]
            total_general = 0
            i = 0
            while i < 10:
                j = 0
                while j < 3:
                    totales_serv[j] += turnos[i][j]
                    total_general += turnos[i][j]
                    j += 1
                i += 1
            j = 0
            while j < 3:
                if total_general == 0:
                    porcentaje = 0
                else:
                    porcentaje = (totales_serv[j] * 100) / total_general
                print(f"{servicios[j]:25}: {porcentaje:.2f}%")
                j += 1

        elif opcion == "6":
            print("\nVeterinario con menor cantidad total de turnos:")
            menor = None
            menor_idx = -1
            i = 0
            while i < 10:
                total = turnos[i][0] + turnos[i][1] + turnos[i][2]
                if menor is None or total < menor:
                    menor = total
                    menor_idx = i
                i += 1
            print(f"{veterinarios[menor_idx]:25} con {menor} turnos")

        elif opcion == "7":
            print("\nPorcentaje de turnos por veterinario respecto al total:")
            total_general = 0
            i = 0
            while i < 10:
                total_general += turnos[i][0] + turnos[i][1] + turnos[i][2]
                i += 1
            i = 0
            while i < 10:
                total_vet = turnos[i][0] + turnos[i][1] + turnos[i][2]
                if total_general == 0:
                    porcentaje = 0
                else:
                    porcentaje = (total_vet * 100) / total_general
                print(f"{veterinarios[i]:25}: {porcentaje:.2f}%")
                i += 1

        elif opcion == "8":
            print("\nServicio(s) más solicitado(s) por cada veterinario:")
            i = 0
            while i < 10:
                max_turnos = turnos[i][0]
                servicios_max = [0]  # índices de servicios más solicitados, inicial con el primero
                j = 1
                while j < 3:
                    if turnos[i][j] > max_turnos:
                        max_turnos = turnos[i][j]
                        servicios_max = [j]
                    elif turnos[i][j] == max_turnos:
                        servicios_max += [j]
                    j += 1

                print(f"{veterinarios[i]:25}: ", end="")
                if max_turnos == 0:
                    print("No tiene turnos registrados")
                else:
                    k = 0
                    while k < len(servicios_max):
                        idx_serv = servicios_max[k]
                        print(f"{servicios[idx_serv]}", end="")
                        if k < len(servicios_max) - 1:
                            print(", ", end="")
                        k += 1
                    print(f" ({max_turnos} turnos)")
                i += 1

        elif opcion == "9":
            break
        else:
            print("Opción inválida. Intente nuevamente.")


# --------------------- MENÚ PRINCIPAL ---------------------

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar un turno")
        print("2. Visualizar todos los datos")
        print("3. Consultas")
        print("4. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            registrar_turno()
        elif opcion == "2":
            mostrar_datos_ordenados()
        elif opcion == "3":
            mostrar_submenu_consultas()
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

# --------------------- EJECUCIÓN ---------------------

menu()

