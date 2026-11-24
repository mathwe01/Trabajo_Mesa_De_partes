import os
from validaciones import validar_codigo, validar_dni

ARCHIVO = "expedientes.txt"


def guardar_expediente(codigo, dni, nombre, direccion, tramite, asunto, fecha):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        linea = codigo + "|" + dni + "|" + nombre + "|" + direccion + "|" + tramite + "|" + asunto + "|" + fecha
        f.write(linea + "\n")
def cargar_archivo():
    codigos = []
    dnis = []
    nombres = []
    direcciones = []
    tramites = []
    asuntos = []
    fechas = []


    if not os.path.exists(ARCHIVO):
        open (ARCHIVO, "w", encoding="utf-8").close()
        return codigos, dnis, nombres, direcciones, tramites, asuntos, fechas

    with open (ARCHIVO, "r", encoding="utf-8") as f: 
        for linea in f:
            if linea.strip() == "":
                continue
            partes = linea.strip().split("|")
            if len(partes) != 7:
                print ("Linea ignorada (datos dañados)")
                continue
            if not validar_codigo(partes[0]) or not validar_dni(partes[1]):
                print("Linea ignorada (datos dañados)")
                continue 
            codigos.append(partes[0])
            dnis.append(partes[1])
            nombres.append(partes[2])
            direcciones.append(partes[3])
            tramites.append(partes[4])
            asuntos.append(partes[5])
            fechas.append(partes[6])
    return codigos, dnis, nombres, direcciones, tramites, asuntos, fechas