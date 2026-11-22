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