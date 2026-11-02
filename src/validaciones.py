def validar_dni(texto):
    if len(texto) != 8:
        return False
    if not texto.isdigit():
        return False
    return True

