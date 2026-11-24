import matplotlib.pyplot as plt

# FUNCIONES -------------------------------------------------------

def generar_aritmetica(primer_termino, diferencia, cantidad):
    sucesion = []
    for n in range(1, cantidad + 1):
        termino = primer_termino + diferencia * (n-1)
        sucesion.append(termino)
    return sucesion

def generar_geometrica(primer_termino, razon, cantidad):
    sucesion = []
    for n in range(1, cantidad + 1):
        termino = primer_termino * razon ** (n - 1)
        sucesion.append(termino)
    return sucesion

def generar_recurrente(primer_termino, segundo_termino, cantidad):
    sucesion = [primer_termino, segundo_termino]
    if cantidad == 1:
        return [primer_termino]
    for n in range(2, cantidad):
        termino = sucesion[n - 1] + sucesion[n - 2]
        sucesion.append(termino)
    return sucesion

def mostrar_tabla(sucesion):
    acumulado = 0
    n = 1
    print()
    print(" n\tTérmino\tSuma acumulada")
    print("--------------------------------")

    for termino in sucesion:
        acumulado = acumulado + termino
        print(n, termino, acumulado, sep="\t")
        n = n + 1

    print("--------------------------------")
    print("Suma total:", acumulado)


# MENÚ INTERACTIVO ------------------------------------------------------------------------------------

print("¡Bienvenido a la graficadora de patrones!")

cantidad = int(input("Cantidad de términos (1-100): "))

if cantidad < 1 or cantidad > 100:
    print("Error: la cantidad debe estar entre 1 y 100.")
    exit()

if cantidad <= 0:
    print("La cantidad de términos debe ser mayor que cero.")

else:
    sucesiones = []
    nombres = []

    for numero in range(1, 4):
        print()
        print("Configuración de la sucesión", numero)

        print("1. Aritmética")
        print("2. Geométrica")
        print("3. Recurrente")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            nombre = "Aritmética"
            primer_termino = float(input("Primer término: "))
            diferencia = float(input("Diferencia: "))
            sucesion = generar_aritmetica(primer_termino, diferencia, cantidad)

        elif opcion == 2:
            nombre = "Geométrica"
            primer_termino = float(input("Primer término: "))
            razon = float(input("Razón: "))
            sucesion = generar_geometrica(primer_termino, razon, cantidad)

        elif opcion == 3:
            nombre = "Recurrente"
            primer_termino = float(input("Primer término: "))
            segundo_termino = float(input("Segundo término: "))
            sucesion = generar_recurrente(primer_termino, segundo_termino, cantidad)

        else:
            print("Opción no válida.")
            continue

        nombres.append(nombre)
        sucesiones.append(sucesion)

        print()
        print("Tabla de la sucesión", numero)
        mostrar_tabla(sucesion)

# TABLA COMPARATIVA ----------------------------------------------------------------------------------------------------------
    
    print()
    print("COMPARACIÓN DE SUCESIONES")
    print()

    print("n", nombres[0], "Suma acumulada 1", nombres[1], "Suma acumulada 2", nombres[2], "Suma acumulada 3", sep="\t")

    acumulados = [0, 0, 0]

    sumas_sucesion1 = []
    sumas_sucesion2 = []
    sumas_sucesion3 = []

    for n in range(cantidad):

        termino1 = sucesiones[0][n]
        termino2 = sucesiones[1][n]
        termino3 = sucesiones[2][n]

        acumulados[0] = acumulados[0] + termino1
        acumulados[1] = acumulados[1] + termino2
        acumulados[2] = acumulados[2] + termino3

        sumas_sucesion1.append(acumulados[0])
        sumas_sucesion2.append(acumulados[1])
        sumas_sucesion3.append(acumulados[2])

        print(n + 1, termino1, acumulados[0], termino2, acumulados[1], termino3, acumulados[2], sep="\t")

    print()
    print("Las tres sucesiones se han generado.")

# RESUMEN ---------------------------------------------------------------------------------------------------------------------

    print()
    print("RESUMEN DE RESULTADOS")
    print()

    for i in range(3):
        ultimo_termino = sucesiones[i][-1]
        suma_total = acumulados[i]

        print("Sucesión", i + 1)
        print("Tipo:", nombres[i])
        print("Último término:", ultimo_termino)
        print("Suma acumulada:", suma_total)
        print()

    mayor_suma = max(acumulados)

    print("Mayor suma acumulada:", mayor_suma)
    print("Obtenida en:")

    for i in range(3):
        if acumulados[i] == mayor_suma:
            print("Sucesión", i + 1, "-", nombres[i])

# GENERAR LA GRÁFICA -----------------------------------------------------------------------------------------------------------

    n = list(range(1, cantidad + 1))

    plt.plot(n, sucesiones[0], marker="o", label="Sucesión 1 (" + nombres[0] + ")")
    plt.plot(n, sucesiones[1], marker="o", label="Sucesión 2 (" + nombres[1] + ")")
    plt.plot(n, sucesiones[2], marker="o",label="Sucesión 3 (" + nombres[2] + ")")

    plt.plot(n, sumas_sucesion1, marker="s", linestyle="--", label="Suma Sucesión 1")
    plt.plot(n, sumas_sucesion2, marker="s", linestyle="--", label="Suma Sucesión 2")
    plt.plot(n, sumas_sucesion3, marker="s", linestyle="--", label="Suma Sucesión 3")
    
    plt.title("Comparación del crecimiento de sucesiones")
    plt.xlabel("Número de término")
    plt.ylabel("Valor del término")

    plt.grid(True)

    plt.legend()

    plt.show()
