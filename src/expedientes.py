ANIO = "2026" 


def generar_codigo(codigos):
    if len (codigos) == 0:
        return ANIO + "-000001"

    ultimo = codigos[len(codigos) - 1] 
    numero = int(ultimo[5:]) + 1
    return ANIO + "-" + str(numero).zfill(6)

def mostrar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas, posicion):
    print("Código:", codigos[posicion])
    print("DNI:", dnis[posicion])
    print("Nombre:", nombres[posicion])
    print("Dirección:", direcciones[posicion])
    print("Trámite:", tramites[posicion])
    print("Asunto:", asuntos[posicion])
    print("Fecha:", fechas[posicion])
    
def ordenar_indices(indices, valores):
    for i in range(1, len(indices)):
        actual = indices[i]
        j = i - 1
        while j >= 0 and valores[indices[j]] > valores[actual]:
            indices[j + 1] = indices[j]
            j = j - 1
        indices[j + 1] = actual

def listar_expedientes(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas):
    if len(codigos) == 0:
        print("No hay expedientes registrados")
        return

    print("Ordenar por: 1. Código 2. Nombres 3.DNI")
    clave = input("Eliga una opción: ")
    while clave != "1" and clave != "2" and clave != "3":
        print("Opción no válida, Elija 1, 2 o 3")
        clave = input("Elija una opción: ")

    if clave == "1":
        valores = codigos
    elif clave == "2":
        valores = nombres
    else:
        valores = dnis

    indices = []
    for i in range(len(codigos)):
        indices.append(i)

    ordenar_indices(indices, valores)

    print()
    print("Total de expedientes:", len(indices))
    print()
    for k in range(len(indices)):
        mostrar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas, indices[k])
        print() 




if __name__ == "__main__":
    print(generar_codigo([]))
    print(generar_codigo(["2026-000001"]))
    print(generar_codigo(["2026-000001", "2026-000002", "2026-000009"]))
    print(generar_codigo(["2026-000099"]))

    codigos = ["2026-000001", "2026-000002"]
    dnis = ["12345678", "87456123"]
    nombres = ["DIANA CARMEN FLORES CASTILLO", "CARLOS LOPEZ DIAZ"]
    direcciones = ["Jr. los jardines 220", "Av. Templo del sol 220"]
    tramites = ["Constancia de no adeudo", "Registro de predios"]
    asuntos = ["Solicito constancia de no adeudo", "Registro de predio nuevo"]
    fechas = ["14/11/2026", "14/11/2026"]

    mostrar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas, 0)
    print()
    mostrar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas, 1)

    indices = [0, 1, 2]
    ordenar_indices(indices, ["C", "A", "B"])
    print(indices)

    indices = [0, 1, 2]
    ordenar_indices(indices, ["A", "B", "C"])
    print(indices)

    indices = [0, 1, 2]
    ordenar_indices(indices, ["C", "B", "A"])
    print(indices)

    indices = [0]
    ordenar_indices(indices, ["A"])
    print(indices)

    codigos.append("2026-000003")
    dnis.append("45871236")
    nombres.append("ANA TORRES RUIZ")
    direcciones.append("Calle Los Pinos 100")
    tramites.append("Solicitud simple")
    asuntos.append("Solicito una copia simple")
    fechas.append("20/11/2026")

    listar_expedientes(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas)
    listar_expedientes(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas)
    listar_expedientes(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas)
    listar_expedientes([], [], [], [], [], [], [])
