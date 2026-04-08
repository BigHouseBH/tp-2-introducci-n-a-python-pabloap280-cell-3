# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py


**Herramienta**: Deepseek

Funcion:tipo_de_dato

**Prompt usado**:

def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    # TU CÓDIGO AQUÍ
    pass aca como ariamos? acaso existe un metodo que deduce el tipo de valor?
> 

**Resultado obtenido**:
¡Sí! Python tiene una función **incorporada** que hace exactamente eso: `type()`.

## Solución para `tipo_de_dato`:

```python
def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    return type(valor).__name__
```

---

## Explicación:

| Código | Qué hace |
|--------|----------|
| `type(valor)` | Te dice el tipo (ej: `<class 'int'>`) |
| `.__name__` | Te da solo el nombre (ej: `"int"`) |

### Ejemplo en acción:
```python
print(type(42))        # <class 'int'>
print(type(42).__name__)  # "int"

print(type(3.14).__name__)   # "float"
print(type([1,2,3]).__name__) # "list"
print(type(True).__name__)    # "bool"
```

---

## ¿Qué tipos puede detectar?

- `int` (enteros)
- `float` (decimales)
- `str` (texto)
- `bool` (True/False)
- `list` (listas)
- `dict` (diccionarios)
- `tuple` (tuplas)
- `NoneType` (para `None`)

---

## Código completo para poner en el archivo:

```python
def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    """
    return type(valor).__name__
```

**Borrá el `pass` y poné eso.** ✅

---

## ¿Era ese el ejercicio o hay más funciones en ese archivo?

Si es `variables.py` completo, debería tener también `armar_mensaje`. ¿Me mostrás el archivo completo?

**¿Lo usaste tal cual o lo modificaste?**
en este caso lo use tal cual

---

Funcion: convertir_a_float

Prompt usado:
def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    # TU CÓDIGO AQUÍ
    pass
seria correcto hacer lo siguiente?
def convertir_a_float(valor: str) -> float:
   return valor;


Resultado obtenido:
¡Casi! Pero hay un detalle importante: **no es lo mismo un string que un float**.

## Tu código:
```python
def convertir_a_float(valor: str) -> float:
    return valor  # ❌ Esto devuelve un string, pero la función dice que devuelve float
```

## Código correcto:
```python
def convertir_a_float(valor: str) -> float:
    return float(valor)  # ✅ Convierte "3.14" → 3.14
```

---

## Explicación:

| Entrada (string) | `float(valor)` | Sale (float) |
|------------------|----------------|--------------|
| `"3.14"` | → | `3.14` |
| `"42"` | → | `42.0` |
| `"-5.5"` | → | `-5.5` |

---

## ¿Qué pasa si le pasás algo que no es número?

```python
convertir_a_float("hola")  # ❌ ERROR: ValueError
```

Pero por ahora asumimos que siempre recibe strings numéricos válidos.

---

## Código final para esa función:

```python
def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    """
    return float(valor)
```

---

## Nota importante:

Veo que escribiste **dos veces** la misma función. Borrá la primera (la que tiene `pass`) y dejá solo una con el código correcto.

```python
# ❌ Borrá esta:
def convertir_a_float(valor: str) -> float:
    pass

# ✅ Dejá solo esta:
def convertir_a_float(valor: str) -> float:
    return float(valor)
```

---

**¿Tenés más funciones en ese archivo?** Mostrame el archivo completo y te ayudo con todas. 🚀





### 2 - condicionales.py

**Herramienta**: 

Herramienta: Deepseek
funcion:clasificar_numero

Prompt usado:

def clasificar_numero(n: int) -> str:
    """
    Retorna "positivo", "negativo" o "cero" según corresponda.
    """
    # TU CÓDIGO AQUÍ
    pass

Quiero entender qué significan n: int y -> str , es como decir int n?, que es el "-->" el pass del final es acaso como un "return null" de java?.

Resultado obtenido:
La IA me explicó que:

n: int y -> str son type hints (sugerencias de tipo, no obligatorias).

Python es dinámicamente tipado, a diferencia de Java por ende estos operadores funcionan como una ""recomendacion"".

pass es una instrucción vacía que no hace nada (no es un return null).


¿Lo usaste tal cual o lo modificaste?

Lo escribí yo mismo después de entender la lógica.


Funcion: mayor_de_tres
**Prompt usado**:
Tengo que hcer esto, es facil pero como es la sintaxis en pyton para un operador "y"?
**Resultado obtenido**:
¡Perfecto! Directo al grano:

## Operador "Y" en Python:

```python
and
```

## Ejemplo:

```python
if condicion1 and condicion2:
    # se ejecuta si ambas son True
```

¿Necesitás algún ejemplo más específico o con eso andamos? 🚀

## Resumen rápido:

- `and` = ambas condiciones deben ser verdaderas
- `or` = al menos una condición debe ser verdadera
- `not` = invierte el valor (True → False, False → True)

*¿Eso era lo que necesitabas o era para otra función?** 🤔



**¿Lo usaste tal cual o lo modificaste?**
No, solamente lo utilize para aprender la sintaxis, es algoritmo empleado es el mio
---

### 3 - listas.py

**Herramienta**:Deepseek

Funcion: suma_lista



**Prompt usado**:
def suma_lista(numeros: list) -> int | float:
    """
    Retorna la suma de todos los elementos de la lista.
    """
    # TU CÓDIGO AQUÍ
    def suma_lista(numeros: list) -> int | float:
    float sumatoria = 0;
    for(num : numeros):
        sumatoria+=num;
    return sumatoria;
asi se usan los for en pyton no?

**Resultado obtenido**:
¡Casi! Pero hay varios errores de sintaxis. Te explico:

## Lo que escribiste (con errores):
```python
def suma_lista(numeros: list) -> int | float:
    float sumatoria = 0;      # ❌ Error: Python no declara tipos así
    for(num : numeros):       # ❌ Error: no se usa ":" dentro del for
        sumatoria+=num;       # ✅ Esto está bien (aunque el ; sobra)
    return sumatoria;
```

## Versión correcta en Python:
```python
def suma_lista(numeros: list) -> int | float:
    sumatoria = 0              # ✅ Sin "float", sin ";"
    for num in numeros:        # ✅ "for variable in lista"
        sumatoria += num       # ✅ Sin ";" (opcional pero no se usa)
    return sumatoria           # ✅ Sin ";"
```

---

## Diferencias clave con otros lenguajes:

| Lo que pensaste (Java/C#) | Python correcto |
|---------------------------|-----------------|
| `float sumatoria = 0;` | `sumatoria = 0` |
| `for(num : numeros)` | `for num in numeros` |
| `punto y coma ;` | No se usa (opcional pero mal visto) |

---

## Versión aún más corta (usando `sum()`):
```python
def suma_lista(numeros: list) -> int | float:
    return sum(numeros)
```

Pero si el ejercicio pide que implementes el loop vos mismo, usá la primera versión.

---

## Resumen del for en Python:

```python
# ✅ Así se escribe:
for elemento in lista:
    # hacé algo

# ❌ Así NO:
for(elemento : lista)   # Eso es Java/C#
```



**¿Lo usaste tal cual o lo modificaste?**

Normalmente empleo la ia como buscador inteligente, me gusta pensar el algoritmo, en este caso tambien lo realize yo, solo emplee la ia para identificar sintaxis caracteristica de pyton



Funcion: filtrar_pares



**Prompt usado**:
hasme un analisis cognitivo del ejersicio def filtrar_pares(numeros: list) -> list:
   pares=list();   """en pyton solo existe las listas, pero se puede declarar semejante a un arreglo Ej: x=[] o bien x=list() """
   for num in numeros:
    if num%2==0:
        pares.append(num);
            
   return pares;

**Resultado obtenido**:
## Análisis cognitivo completo de `filtrar_pares` 🧠

---

### 📊 Evaluación general: **APROBADO** ✅

| Criterio | Estado | Puntaje |
|----------|--------|---------|
| Corrección lógica | ✅ Perfecto | 10/10 |
| Sintaxis Python | ✅ Correcta | 9/10 |
| Casos borde | ✅ Bien manejados | 10/10 |
| Estilo/Pythonic | ⚠️ Mejorable | 7/10 |
| Documentación | ✅ Aceptable | 8/10 |

---

### ✅ Lo que está EXCELENTE:

1. **Lógica correcta**: `num % 2 == 0` captura TODOS los pares (incluyendo 0, negativos)
2. **Caso borde del 0**: ✅ BIEN (ahora sí lo incluís)
3. **Lista vacía**: `[]` → retorna `[]` ✅
4. **Estructura clara**: loop → condición → append → return

---

### ⚠️ Lo que es MEJORABLE (pero NO incorrecto):

| Problema | Tu código | Mejor versión |
|----------|-----------|---------------|
| Punto y coma | `pares = list();` | `pares = []` |
| Posición del docstring | Dentro de la función | Encima (justo abajo del `def`) |
| Comentario largo | Dentro del código | Mejor en el docstring |

---

### 🔍 Análisis línea por línea:

```python
def filtrar_pares(numeros: list) -> list:
```
✅ Tipo de parámetro y retorno bien especificados

```python
    pares = list();
```
✅ Crea lista vacía correctamente  
⚠️ El `;` sobra (pero no rompe nada)

```python
    """en pyton solo existe las listas..."""
```
⚠️ El docstring debería describir QUÉ hace la función, no dar lecciones de Python

```python
    for num in numeros:
```
✅ Iteración correcta

```python
        if num % 2 == 0:
```
✅ Condición perfecta (0, negativos, positivos)

```python
            pares.append(num);
```
✅ Agrega elemento correctamente  
⚠️ `;` sobra

```python
    return pares;
```
✅ Retorna la lista correcta  
⚠️ `;` sobra

---

### 🧪 Casos borde probados:

| Entrada | Salida | ¿Correcto? |
|---------|--------|------------|
| `[0, 1, 2, 3, 4]` | `[0, 2, 4]` | ✅ |
| `[]` | `[]` | ✅ |
| `[-4, -3, -2, -1]` | `[-4, -2]` | ✅ |
| `[1, 3, 5]` | `[]` | ✅ |
| `[0, 0, 0]` | `[0, 0, 0]` | ✅ |

---

### 🚀 Versión mejorada (más "Pythonica"):

```python
def filtrar_pares(numeros: list) -> list:
    """
    Filtra y retorna solo los números pares de la lista recibida.
    Incluye el 0 y números negativos pares.
    """
    return [num for num in numeros if num % 2 == 0]
```

---

### 📈 Resumen cognitivo:

| Aspecto | Evaluación |
|---------|------------|
| **Comprensión del problema** | ✅ Completa |
| **Manejo de casos borde** | ✅ Excelente (0 incluido) |
| **Sintaxis básica** | ✅ Correcta |
| **Estilo Python** | ⚠️ Aceptable (mejorable) |
| **Legibilidad** | ✅ Buena |

---

### 🎯 Nota final: **8.5/10**

**Puntos a mejorar para llegar a 10:**
1. Sacar los `;` (son de Java/C, no de Python)
2. Mover el comentario a docstring
3. Usar `[]` en lugar de `list()` (más rápido y legible)

---

**¿Querés que te ayude a refactorizarlo a la versión "Python puro" o así lo dejamos?** 😊

**¿Lo usaste tal cual o lo modificaste?**

No aplica, solo pedi un diagnostico cognitivo del algoritmo


Funcion:invertir_lista


**Prompt usado**:
def invertir_lista(lista: list) -> list:
    """
    Retorna la lista invertida SIN modificar la original.
    """
    # TU CÓDIGO AQUÍ
    pass no quiero que me lo resuelvas solo quiero saber si las listas tienen un getSize() u los for alguna manera de hacer un recorido lineal inverso


**Resultado obtenido**:

¡Excelente pregunta! Te explico sin resolverlo:

## En Python NO existe `getSize()` → se usa `len(lista)`

| Java / C# | Python |
|-----------|--------|
| `lista.size()` | `len(lista)` |
| `lista.length` | `len(lista)` |

---

## Para recorrer una lista de forma inversa (3 formas):

### 1. **Usando `reversed()`** (la más común)
```python
for elemento in reversed(lista):
    # recorre desde el último hasta el primero
```

### 2. **Usando índice negativo**
```python
for i in range(len(lista) - 1, -1, -1):
    elemento = lista[i]
    # i empieza en el último índice, baja hasta 0
```

### 3. **Usando slicing invertido**
```python
for elemento in lista[::-1]:
    # recorre la lista invertida
```

---

## Índices negativos en Python (importante):

| Lista | `[10, 20, 30, 40]` |
|-------|---------------------|
| Índice positivo | 0→10, 1→20, 2→30, 3→40 |
| Índice negativo | -4→10, -3→20, -2→30, -1→40 |

```python
mi_lista = [10, 20, 30, 40]
print(mi_lista[-1])  # 40 (último)
print(mi_lista[-2])  # 30
```

---

## Para tu ejercicio `invertir_lista`:

Necesitás **crear una NUEVA lista** (sin modificar la original). Algunas ideas:
- Recorrer la original desde el final hasta el principio e ir agregando
- Usar slicing: `lista[::-1]` crea una copia invertida

---

## Resumen:

| Necesitas | En Python |
|-----------|-----------|
| Tamaño de lista | `len(lista)` |
| Recorrer inverso | `reversed(lista)` |
| Último elemento | `lista[-1]` |
| Crear copia invertida | `lista[::-1]` |

¿Con estas herramientas podés resolverlo o necesitás alguna aclaración más?** 😊

**¿Lo usaste tal cual o lo modificaste?**

Use lo que me enseño, el algoritmo prefiero procesarlo yo mismo para conetar mas con pyton


funcion: invertir_lista

**Prompt usado**:
> def invertir_lista(lista: list) -> list:
    """
En este caso podria hacer un algoritmo mas tradicional solicictando la longitud de la lista y a aprtir de ahi recorrerla de forma opuesta pero pyton posee una funcion elegante que voy a emplear:    """
    return list(reversed(lista));

 diagnostico

**Resultado obtenido**:
## ¡Me encanta! ❤️

Es **excelente** tu enfoque por dos razones:

---

### 1. ✅ **Reconocés la herramienta adecuada**
No forzás un algoritmo "tradicional" (con índices y `len()`) cuando Python ya tiene algo más elegante.

### 2. ✅ **Documentás tu decisión**
Explicás POR QUÉ elegiste esa forma. Eso es valioso.

---

## Puntaje imaginario:

| Aspecto | Puntaje |
|---------|---------|
| Corrección | 10/10 |
| Elegancia | 10/10 |
| Documentación | 10/10 |
| Estilo Python | 9/10 (solo por el `;`) |

---

## Mini mejora (sacá el `;`):

```python
def invertir_lista(lista: list) -> list:
    """
    En este caso podría hacer un algoritmo más tradicional solicitando la 
    longitud de la lista y a partir de ahí recorrerla de forma opuesta, 
    pero Python posee una función elegante que voy a emplear.
    """
    return list(reversed(lista))
```

---

## Lo que VALORO de tu código:

> *"No todo lo que se puede hacer con un loop tradicional debe hacerse con un loop tradicional. Python te da herramientas de alto nivel para pensar más claro."*

---

## ¿Se puede aún más elegante?

```python
def invertir_lista(lista: list) -> list:
    """Retorna la lista invertida usando slicing."""
    return lista[::-1]
```

Pero **ambas son perfectamente válidas**. La tuya es más explícita (muestra la intención de "reversar" claramente).

---

¿Dejamos esa versión o querés probar la de slicing?** Cualquiera de las dos está perfecta. 😊👍

**¿Lo usaste tal cual o lo modificaste?**

no aplica, solo pedi un diagnositoco del area cognitiva del algoritmo.Aun asi descubri que puedo crear una lista directamente usando el iterador que retorna reversed(), sin el uso explicitp de un for

**Nota**:Tuve una larga discusion sobre el funcionamiento del for en pyton ya que entendia que recorria de forma directa cada elemento a la derecha del In, pero la Ia me enseño que el operador for de pyton funciona de forma diferente, abstrayendo procesos al usuario, basicamente :
for X in Y:
si Y es objeto lista=> for pide un iterador al(un indice) y recorre segun el iterador, si le doy el iterador directamente=> for directamente lo recorre segun el iterador, el REVERSED ES UN METODO QUE RETORNA UN ITERADOR CON LOGICA INVERSA A LA LISTA QUE TIENE DE PARAMETRO.Cambio mi vision de los for en pyton y ahora los pienso como un operador que hace multiples invocaciones segun una especie de indice determinada Iterador,


Funcion: eliminar_duplicados


**Prompt usado**:
def eliminar_duplicados(lista: list) -> list:
    sinDuplicados=list(lista);
    for elemento in sinDuplicados:
       copy=sinDuplicados.count(elemento);
       while(not copy==0):
        for buscado in reversed(sinDuplicados):
            if(buscado==elemento):
                sinDuplicados.remove(elemento);
                copy=sinDuplicados.count(elemento);
                break;

             quiero que corrigas mi idea para que en ves de usar el reversed acceda al mismo indice del iterador y busque hacia adelante, porque aunque mi logica que comparar con los elmentos atras del elemento es en bano ya que ya se comparo, es corresta, sinembargo en caso de recivir comoparametro una lista ordenada perderia la oprtunidad de hacerlo mas efciciente al ser los elementos estan ubicados como vecinos, pero no alteres la logica prinsipal del algoritmo que te envio dado que la idea es que fucniones si no esta ordenado, y que funcione aun mejor si esta ordenado, es decir no compara sol con su vecino sino con todos los de adelante, pero se replante con el metodo count si sigue aviendo para asi tener chance de ahorrarse una busqueda lineal inecesaria, es decir siempre cada que elimina un elmento , decrece el contador pero busca asia adelante del indice del elemetno NUNCA ASUME QUE EL SIGUIENTE ES IGUAL O QUE ESTA ORDENADA
> 

**Resultado obtenido**:
¡Excelente! Entiendo perfectamente tu idea. Querés **mantener tu lógica original** pero optimizarla para que:

1. ✅ Funcione siempre (lista ordenada o no)
2. ✅ Sea más eficiente cuando está ordenada
3. ✅ Busque **hacia adelante** desde el elemento actual (no use `reversed`)
4. ✅ Use `count()` para saber si aún quedan duplicados

---

## Tu idea corregida y optimizada:

```python
def eliminar_duplicados(lista: list) -> list:
    sinDuplicados = list(lista)
    i = 0  # Índice manual en lugar de for elemento
    
    while i < len(sinDuplicados):
        elemento = sinDuplicados[i]
        cantidad = sinDuplicados.count(elemento)
        
        if cantidad > 1:
            # Buscar hacia ADELANTE (desde i+1 hasta el final)
            for j in range(i + 1, len(sinDuplicados)):
                if sinDuplicados[j] == elemento:
                    sinDuplicados.pop(j)  # Eliminar por índice
                    cantidad -= 1
                    break  # Salgo del for, vuelvo al while
        else:
            i += 1  # Solo avanzo si no eliminé nada
    
    return sinDuplicados
```

---

## ¿Qué cambié?

| Tu versión | Mi corrección |
|------------|---------------|
| `for elemento in sinDuplicados` | `while i < len()` (control manual) |
| `reversed(sinDuplicados)` | `for j in range(i+1, len())` (hacia adelante) |
| `remove(elemento)` | `pop(j)` (eliminar por índice exacto) |
| `break` dentro del `for` | `break` + `cantidad -= 1` |

---

## ¿Por qué funciona mejor?

### Ejemplo con lista ordenada `[1, 1, 1, 2]`:

```python
i=0, elemento=1, cantidad=3 (>1)
  Busca desde i+1 (posición 1): encuentra 1 en j=1
  Elimina posición 1 → lista = [1, 1, 2]
  cantidad=2, break, vuelve al while (i sigue siendo 0)

i=0, elemento=1, cantidad=2 (>1)
  Busca desde i+1 (posición 1): encuentra 1 en j=1
  Elimina posición 1 → lista = [1, 2]
  cantidad=1, break

i=0, elemento=1, cantidad=1 (no >1)
  i++ → i=1

i=1, elemento=2, cantidad=1 (no >1)
  i++ → i=2 (termina)

Resultado: [1, 2] ✅
```

### Ejemplo con lista desordenada `[2, 1, 2, 1]`:

```python
i=0, elemento=2, cantidad=2
  Busca desde i+1: j=2 (posición 2 hay un 2)
  Elimina j=2 → lista = [2, 1, 1]
  cantidad=1

i=0, elemento=2, cantidad=1 → i=1

i=1, elemento=1, cantidad=2
  Busca desde i+1: j=2 (posición 2 hay un 1)
  Elimina j=2 → lista = [2, 1]

Resultado: [2, 1] ✅ (preserva orden de primera aparición)
```

---

## Complejidad algorítmica:

| Situación | Tu idea original | Esta versión |
|-----------|------------------|--------------|
| Peor caso (desordenado) | O(n²) | O(n²) |
| Mejor caso (ordenado) | O(n²) | **O(n)** ✅ |

---

## Versión aún más eficiente (si permitís cambiar la lógica):

```python
def eliminar_duplicados(lista: list) -> list:
    visto = set()
    resultado = []
    for elemento in lista:
        if elemento not in visto:
            visto.add(elemento)
            resultado.append(elemento)
    return resultado
```
Esto es **O(n)** siempre, pero no usa tu lógica original.

---

## Conclusión:

Tu idea de **buscar hacia adelante en lugar de usar `reversed`** es **correcta y más eficiente** cuando la lista está ordenada.

La versión que te propongo **respeta tu lógica original** pero corrige:
- El problema de modificar la lista mientras se recorre
- La búsqueda ineficiente hacia atrás
- El uso de `remove()` por `pop(j)`

**¿Te gusta esta corrección o querés que ajuste algo más?** 😊
**¿Lo usaste tal cual o lo modificaste?**
Lo modifique tenia algunas fallas como que asumia que solo existe una copia debido al operador if cantidad > 1:
 en lugar de un while

---

### 4 - diccionarios.py

**Herramienta**: DeepSeek

**Prompt usado**:
def contar_palabras(texto: str) -> dict:
    """
    Retorna un diccionario con la frecuencia de cada palabra.
    Ejemplo: contar_palabras("hola mundo hola") -> {"hola": 2, "mundo": 1}
    Las palabras deben ser comparadas en minúsculas.
    """
    # TU CÓDIGO AQUÍ
    pass   reseta: 1)lee cadapalabra y comparala con todas las que siguen,2)Al aver contado anotala de la manera corresta en la lista cuentaPalabras, y enlista la palabra repetida en una lista palabras repertidas para y avansar indice y repetir si solo si la palabra no esta en la lista de palabras repetidas

**Resultado obtenido**:
La ia me explico me dio un  codigo funcional y me enseño que no hacia flata llevar un registro de que palabras ya se consideraron para que no ocurran casos de repeticion(siguiendo el ejemplo del comentario Ej:Hola:2, Hola:2), ya que pyton tiene una dato llamado diccionario en en palabras simples relaciona un valor a una clave, por tanto al haver una clave hola todas sus repeticiones e almacenarar en la misma ""casilla""

**¿Lo usaste tal cual o lo modificaste?**
Luego de entender el funcionamiento de los diccionarios lo deje tal cual ya que era funcional

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final
## Reflexión final

- Aprendí que para formular buenos prompts hay que ser **claro y específico**. No basta con decir "resolvé esto", sino que hay que explicar el contexto, qué parte no se entiende y qué tipo de respuesta se espera. También aprendí que hacer preguntas concretas sobre sintaxis o conceptos específicos da mejores resultados que pedir soluciones completas.

- La IA fue muy útil para explicar conceptos como type hints, la diferencia entre listas y diccionarios, o cómo funciona el operador `and`. También me ayudó a entender errores de lógica. En cambio, no fue tan útil cuando intenté resolver ejercicios más complejos con mi propia lógica (como eliminar duplicados), porque la IA a veces proponía soluciones muy alejadas de mi razonamiento o que no terminaban de funcionar como esperaba.

- La próxima vez consideraria mas algunos patrones que s eme hisieron comodos como el analisis cognitivo ya que me da un buen diagnostico, y resetea ya que es como escrivir mi algoritmo de forma mas abstarcta pero que sostiene la idea de que razar y no que la ia lo haga.Ademas usaria mas la Ia con un enfoque de acelerar ya que al inicio me centre en entender muy bien pyton y su sintaxis y no llegaba con el timepo de entrega lo que me orillo a usar la ia para resolver y a aprtir de ahi preguntar en lugar de hacerlo yo mismo y hacer diagnosticos y consultas despues