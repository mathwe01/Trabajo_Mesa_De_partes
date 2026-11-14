import os
from validaciones import validar_codigo, validar_dni

ARCHIVO = "expedientes.txt"


def guardar_expediente(codigo, dni, nombre, direccion, tramite, asunto, fecha):
    with open(ARCHIVO, "a", encoding="utf-8") as f:
        linea = codigo + "|" + dni + "|" + nombre + "|" + direccion + "|" + tramite + "|" + asunto + "|" + fecha
        f.write(linea + "\n")

if __name__ == "__main__":
    guardar_expediente("2026-000001", "12345678", "MARIA CARMEN QUISPE HUAMAN", "jr. los jardines 220", "constacia de no adeudo", "solicito constancia de no adeudo", "14/11/2026")
    guardar_expediente("2026-000002", "87456123", "CARLOS LOPEZ DIAZ", "av. templo del sol 220", "registro de predios", "registro de predio nuevo", "14/11/2026")