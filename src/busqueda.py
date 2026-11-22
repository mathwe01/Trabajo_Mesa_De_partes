from validaciones import validar_codigo

def buscar_binaria(codigos, codigo):
    inicio = 0
    fin = len(codigos) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2 
        if codigos[medio] == codigo:
            return medio
        elif codigos[medio] < codigo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1

def buscar_expediente(codigos, dnis, nombres, direcciones, tramites, asuntos, fechas, codigo):
    if not validar_codigo(codigo):
        print("Código no válido, use el formato AAAA-NNNNNN") 
        return 

    posicion = buscar_binaria(codigos, codigo)

    if posicion == -1:
        print("No se encontró el expediente")
    else:
        print("Código:", codigos[posicion])
        print("DNI:", dnis[posicion])
        print("Nombre:", nombres[posicion])
        print("Dirección:", direcciones[posicion])
        print("Trámite:", tramites[posicion])
        print("Asunto:", asuntos[posicion])
        print("Fecha:", fechas[posicion])



if __name__ == "__main__":
    lista = ["2026-000001", "2026-000002", "2026-000003", "2026-000004", "2026-000005"]
    print (buscar_binaria(lista, "2026-000003"))
    print (buscar_binaria(lista, "2026-000001"))
    print (buscar_binaria(lista, "2026-000005"))
    print (buscar_binaria(lista, "2026-000009"))
    print (buscar_binaria([], "2026-000001"))

    codigos = ["2026-000001", "2026-000002"]
    dnis = ["12345678", "87456123"]
    nombres = ["DIANA CARMEN FLORES CASTILLO", "CARLOS LOPEZ DIAZ"]
    direciones = ["Jr. los jardines 220", "Av. Templo del sol 220"]
    tramites = ["Constancia de no adeudo", "Registro de predios"]
    asuntos = ["Solicito constancia de no adeudo", "Registro de predio nuevo"]
    fechas = ["14/11/2026", "14/11/2026"]

    buscar_expediente(codigos, dnis, nombres, direciones, tramites, asuntos, fechas, "2026-000002")
    buscar_expediente(codigos, dnis, nombres, direciones, tramites, asuntos, fechas, "2026-000009")
    buscar_expediente(codigos, dnis, nombres, direciones, tramites, asuntos, fechas, "ABC")
