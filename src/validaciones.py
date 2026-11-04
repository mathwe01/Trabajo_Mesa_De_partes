def validar_dni(texto):
    if len(texto) != 8:
        return False
    if not texto.isdigit():
        return False
    return True

def validar_texto(texto, minimo, maximo):
    texto = texto.strip()
    if len(texto) < minimo or len(texto) > maximo:
        return False
    if "|" in texto:
        return False
    return True

def validar_nombre(texto):
    texto = texto.strip()
    if len(texto) < 3 or len(texto) > 60:
        return False
    for letra in texto:
        if not letra.isalpha() and letra != " ":
            return False
    return True
