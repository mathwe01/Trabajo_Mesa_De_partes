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