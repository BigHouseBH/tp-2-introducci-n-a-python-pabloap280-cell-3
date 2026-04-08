# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    frase = "Hola, " + nombre+"!"
    return frase;


def suma_enteros(a: int, b: int) -> int:

    return a + b;


def es_mayor_de_edad(edad: int) -> bool:
    if(edad>=18):
        return True;
    return False;


def tipo_de_dato(valor) -> str:

    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    return float(valor);
