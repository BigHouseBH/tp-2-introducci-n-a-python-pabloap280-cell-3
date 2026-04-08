# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    texto_limpio = texto.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    palabras = texto.split()
    palabras_capitalizadas = [palabra.capitalize() for palabra in palabras]
    return " ".join(palabras_capitalizadas)


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiouáéíóú"
    texto_minuscula = texto.lower()
    contador = 0
    for letra in texto_minuscula:
        if letra in vocales:
            contador += 1
    return contador


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = []
    
    for caracter in texto:
        if caracter.isupper():
            # Letra mayúscula
            nuevo = chr((ord(caracter) - ord('A') + desplazamiento) % 26 + ord('A'))
            resultado.append(nuevo)
        elif caracter.islower():
            # Letra minúscula
            nuevo = chr((ord(caracter) - ord('a') + desplazamiento) % 26 + ord('a'))
            resultado.append(nuevo)
        else:
            # No es letra
            resultado.append(caracter)
    
    return "".join(resultado)