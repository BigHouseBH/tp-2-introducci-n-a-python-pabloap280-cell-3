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
    sinDuplicados = list(lista)
    i = 0  # Índice manual en lugar de for elemento
    
    while i < len(sinDuplicados):
        elemento = sinDuplicados[i]
        cantidad = sinDuplicados.count(elemento)
        
        while cantidad > 1:
            # Buscar hacia ADELANTE (desde i+1 hasta el final)
            for j in range(i + 1, len(sinDuplicados)):
                if sinDuplicados[j] == elemento:
                    sinDuplicados.pop(j)  # Eliminar por índice
                    cantidad -= 1
                    break  # Salgo del for, vuelvo al while
        else:
            i += 1  # Solo avanzo si no eliminé nada
    
    return sinDuplicados

            


def aplanar_lista(lista: list) -> list:
    resultado = []
    for sublista in lista:
        resultado.extend(sublista)
    return resultado