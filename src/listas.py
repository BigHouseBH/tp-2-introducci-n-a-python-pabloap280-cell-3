# ============================================================
# MÓDULO 3: Listas
# ============================================================


def suma_lista(numeros: list) -> int | float:
    sumatoria = 0;
    """el for de pyton se piensa semejante a un for each de java, Ej: por cada elemento X de la coleccion Lista: ejecuta lo siguiente..."""
    for num in numeros:
        sumatoria+=num;
    return sumatoria;


def filtrar_pares(numeros: list) -> list:
   pares=list();   """en pyton solo existe las listas, pero se puede declarar semejante a un arreglo Ej: x=[] o bien x=list() """
   for num in numeros:
    if num%2==0:
        pares.append(num);
            
   return pares;


def invertir_lista(lista: list) -> list:
    """
En este caso podria hacer un algoritmo mas tradicional solicictando la longitud de la lista y a aprtir de ahi recorrerla de forma opuesta pero pyton posee una funcion elegante que voy a emplear:    """
    reverseList=list(reversed(lista));
    return reverseList;


def eliminar_duplicados(lista: list) -> list:
    """
    Retorna una nueva lista sin elementos duplicados,
    manteniendo el orden de primera aparición.
    """
    # TU CÓDIGO AQUÍ
    pass


def aplanar_lista(lista: list) -> list:
    """
    Dada una lista de listas, retorna todos los elementos en una sola lista.
    Ejemplo: aplanar_lista([[1,2],[3,4]]) -> [1, 2, 3, 4]
    """
    # TU CÓDIGO AQUÍ
    pass
