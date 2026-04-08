# ============================================================
# MÓDULO 4: Diccionarios
# ============================================================


def contar_palabras(texto: str) -> dict:
    palabras = texto.lower().split()
    contador = {}  
    for palabra in palabras:
        if palabra in contador:     # ¿Ya existe?
            contador[palabra] += 1  # Sí → sumo 1
        else:
            contador[palabra] = 1   # No → la creo con valor 1
    
    return contador


def invertir_diccionario(d: dict) -> dict:
    invertido = {}
    for clave, valor in d.items():
        invertido[valor] = clave
    return invertido

def merge_diccionarios(d1: dict, d2: dict) -> dict:
    """
    Combina dos diccionarios. Si hay claves repetidas, prevalece d2.
    """
    resultado = d1.copy()  # Copia d1
    resultado.update(d2)   # Agrega d2 (sobreescribe claves repetidas)
    return resultado

def filtrar_por_valor(d: dict, minimo: int) -> dict:
    """
    Retorna un nuevo diccionario con solo los pares
    cuyo valor sea >= minimo.
    """
    resultado = {}
    for clave, valor in d.items():
        if valor >= minimo:
            resultado[clave] = valor
    return resultado
