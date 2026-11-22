ANIO = "2026" 


def generar_codigo(codigos):
    if len (codigos) == 0:
        return ANIO + "-000001"

    ultimo = codigos[len(codigos) - 1] 
    numero = int(ultimo[5:]) + 1
    return ANIO + "-" + str(numero).zfill(6)



if __name__ == "__main__":
    print(generar_codigo(["2026-000001"]))
    print(generar_codigo(["2026-000001"]))
    print(generar_codigo(["2026-000001", "2026-000002", "2026-000009"]))
    print(generar_codigo(["2026-000099"]))