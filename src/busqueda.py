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


if __name__ == "__main__":
    lista = ["2026-000001", "2026-000002", "2026-000003", "2026-000004", "2026-000005"]
    print (buscar_binaria(lista, "2026-000003"))
    print (buscar_binaria(lista, "2026-000001"))
    print (buscar_binaria(lista, "2026-000005"))
    print (buscar_binaria(lista, "2026-000009"))
    print (buscar_binaria([], "2026-000001"))