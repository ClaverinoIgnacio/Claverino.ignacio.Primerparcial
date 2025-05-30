# Matriz con la cantidad de turnos brindados por cada veterinario para cada tipo de servicio
# Columnas: [Consulta General, Vacunación, Control Post-quirúrgico]
matriz_turnos = [
    [5, 3, 2],
    [7, 4, 1],
    [6, 5, 3],
    [4, 2, 1],
    [8, 6, 2],
    [3, 1, 0],
    [5, 4, 2],
    [6, 2, 1],
    [7, 3, 2],
    [4, 2, 2]
]

# Lista de nombres de veterinarios
veterinarios = [
    "Neiner, Maximiliano",
    "Villegas, Octavio",
    "Cardozo, Marina",
    "Baus, Christian",
    "Luccheta, Giovanni",
    "Fernández, David",
    "Ochoa, Gonzalo",
    "Gatto, Catriel",
    "Fernández, Mariano",
    "Bustos Gil, Felipe"
]

# Lista de servicios
servicios = ["Consulta General", "Vacunación", "Control Post-quirúrgico"]

# Precios por servicio
precios = [1500, 1000, 2000]

# Funciones

def mostrar_menu_consultas():
    print("\n--- Submenú de Consultas ---")
    print("1. Listado con la cantidad total de turnos por veterinario")
    print("2. Promedio de turnos por tipo de servicio")
    print("3. Recaudación total acumulada")
    print("4. Veterinarios ordenados A-Z con recaudación total")
    print("5. Porcentaje de cada tipo de servicio respecto al total")
    print("6. Veterinario con menor cantidad total de turnos")
    print("7. Registrar nuevo turno")
    print("8. Porcentaje de turnos por veterinario respecto al total")
    print("9. Servicio/s más solicitado/s por cada veterinario")
    print("10. Volver al menú principal")

def calcular_total_turnos_por_veterinario():
    for i in range(len(veterinarios)):
        total = sum(matriz_turnos[i])
        print(f"{veterinarios[i]}: {total} turnos")

def calcular_promedio_por_servicio():
    print("\nPromedio por tipo de servicio:")
    total_veterinarios = len(matriz_turnos)
    for j in range(len(servicios)):
        total = 0
        i = 0
        while i < total_veterinarios:
            total = total + matriz_turnos[i][j]
            i = i + 1
        promedio = total / total_veterinarios
        print(f"{servicios[j]}: {promedio:.2f} turnos")

def calcular_recaudacion_total():
    total = 0
    for i in range(len(matriz_turnos)):
        for j in range(len(servicios)):
            total = total + matriz_turnos[i][j] * precios[j]
    print(f"\nRecaudación total: ${total}")

def veterinarios_ordenados_con_recaudacion():
    datos = []
    i = 0
    while i < len(veterinarios):
        recaudado = 0
        j = 0
        while j < len(servicios):
            recaudado = recaudado + matriz_turnos[i][j] * precios[j]
            j = j + 1
        datos.append([veterinarios[i], recaudado])
        i = i + 1

    # Ordenar con burbuja
    n = len(datos)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - 1 - i:
            if datos[j][0] > datos[j + 1][0]:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux
            j = j + 1
        i = i + 1

    k = 0
    while k < len(datos):
        print(datos[k][0], ": $", datos[k][1])
        k = k + 1

def porcentaje_por_tipo_de_servicio():
    total_general = 0
    for fila in matriz_turnos:
        for val in fila:
            total_general = total_general + val

    print("\nPorcentaje por tipo de servicio:")
    j = 0
    while j < len(servicios):
        subtotal = 0
        i = 0
        while i < len(matriz_turnos):
            subtotal = subtotal + matriz_turnos[i][j]
            i = i + 1
        porcentaje = (subtotal / total_general) * 100
        print(f"{servicios[j]}: {porcentaje:.2f}%")
        j = j + 1

def veterinario_con_menos_turnos():
    min_turnos = None
    nombre_min = ""
    i = 0
    while i < len(matriz_turnos):
        total = sum(matriz_turnos[i])
        if min_turnos is None or total < min_turnos:
            min_turnos = total
            nombre_min = veterinarios[i]
        i = i + 1
    print(f"\nVeterinario con menos turnos: {nombre_min} con {min_turnos} turnos")

def registrar_turno():
    print("\nRegistro de nuevo turno")
    nombre = input("Ingrese el nombre completo del veterinario: ")

    if nombre not in veterinarios:
        print("Veterinario encontrado.")
        return
    else:
        print("Veterinario no encontrado.")

    print("Tipos de servicios:")
    i = 0
    while i < len(servicios):
        print(f"{i + 1}. {servicios[i]}")
        i = i + 1

    servicio = input("Ingrese el tipo de servicio: ")

    if servicio not in servicios:
        print("Servicio válido.")
        return
    else:
        print("Servicio no válido.")

    cantidad = input("Ingrese cantidad de turnos (1 a 10): ")
    if (cantidad >= "0" and cantidad <= "9") or cantidad == "10":
        cantidad = int(cantidad)
        if cantidad >= 1 and cantidad <= 10:
            print("Cantidad válida.")
        else:
            print("Cantidad inválida.")
            return
    else:
        print("Cantidad inválida.")
        return

    # Buscar índice del veterinario
    i = 0
    while i < len(veterinarios):
        if nombre == veterinarios[i]:
            break
        i = i + 1

    # Buscar índice del servicio
    j = 0
    while j < len(servicios):
        if servicio == servicios[j]:
            break
        j = j + 1

    matriz_turnos[i][j] = matriz_turnos[i][j] + cantidad
    total = precios[j] * cantidad
    print("Turno registrado. Total a pagar: $", total)

def porcentaje_por_veterinario():
    total_general = 0
    for fila in matriz_turnos:
        for val in fila:
            total_general = total_general + val

    print("\nPorcentaje de turnos por veterinario:")
    i = 0
    while i < len(veterinarios):
        total = sum(matriz_turnos[i])
        porcentaje = (total / total_general) * 100
        print(f"{veterinarios[i]}: {porcentaje:.2f}%")
        i = i + 1

def servicio_mas_solicitado_por_veterinario():
    print("\nServicio/s más solicitado/s por cada veterinario:")
    i = 0
    while i < len(veterinarios):
        maximo = 0
        j = 0
        while j < len(servicios):
            if matriz_turnos[i][j] > maximo:
                maximo = matriz_turnos[i][j]
            j = j + 1

        j = 0
        servicios_max = []
        while j < len(servicios):
            if matriz_turnos[i][j] == maximo:
                servicios_max.append(servicios[j])
            j = j + 1

        print(f"{veterinarios[i]}: {', '.join(servicios_max)} ({maximo} turnos)")
        i = i + 1

# Ciclo del submenú
while True:
    mostrar_menu_consultas()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        calcular_total_turnos_por_veterinario()
    elif opcion == "2":
        calcular_promedio_por_servicio()
    elif opcion == "3":
        calcular_recaudacion_total()
    elif opcion == "4":
        veterinarios_ordenados_con_recaudacion()
    elif opcion == "5":
        porcentaje_por_tipo_de_servicio()
    elif opcion == "6":
        veterinario_con_menos_turnos()
    elif opcion == "7":
        registrar_turno()
    elif opcion == "8":
        porcentaje_por_veterinario()
    elif opcion == "9":
        servicio_mas_solicitado_por_veterinario()
    elif opcion == "10":
        print("Volviendo al menú principal...")
        break
    else:
        print("Opción inválida. Intente nuevamente.")

