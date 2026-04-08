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




---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

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

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
