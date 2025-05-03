# Actividad: Escribir aserciones en pruebas con pytest

## **Paso 1: Instalando pytest y pytest-cov**

- Creamos un entorno virtual y lo activamos

	```bash
	python -m venv venv
	source venv/bin/activate
    ```

- Instalamos las herramientas necesarias

	```bash
	pip install pytest pytest-cov
	```

![](Attachments/Pasted%20image%2020250503155130.png)

## **Paso 2: Archivos de prueba**

Se usarán los archivos `stack.py` y `test_stack.py`.

- `stack.py`: Contiene la implementación de una pila (stack) que queremos probar.
- `test_stack.py`: Contiene el esqueleto de las pruebas para los métodos `push()`, `pop()`, `peek()`, y `is_empty()`.

### Métodos de la clase Stack

```python
class Stack:
    def push(self, data: Any) -> None:
        ...
    def pop(self) -> Any:
        ...
    def peek(self) -> Any:
        ...
    def is_empty(self) -> bool:
        ...
```

Descripción de funciones:

- `push()`: Añade un elemento a la parte superior de la pila.
- `pop()`: Elimina y devuelve el elemento en la parte superior de la pila.
- `peek()`: Devuelve el valor del elemento en la parte superior de la pila sin eliminarlo.
- `is_empty()`: Devuelve True si la pila está vacía y False si no lo está.

Actualmente el archivo `test_stack.py` se ve así, por lo que el resultado mostrará **FAILED**

```python
from unittest import TestCase
from stack import Stack


class TestStack(TestCase):
    """Casos de prueba para la Pila"""

    def test_push(self) -> None:
        """Prueba de insertar un elemento en la pila."""
        self.assertTrue(False, "Prueba de inserción no implementada")

    def test_pop(self) -> None:
        """Prueba de eliminar un elemento de la pila."""
        self.assertTrue(False, "Prueba de eliminación no implementada")

    def test_peek(self) -> None:
        """Prueba de observar el elemento superior de la pila."""
        self.assertTrue(False, "Prueba de observación no implementada")

    def test_is_empty(self) -> None:
        """Prueba de si la pila está vacía."""
        self.assertTrue(False, "Prueba de vacío no implementada")
```

Verificamos con `pytest -vx` para un resultado detallado y que pare al aparecer el primer **FAILED**

![](Attachments/Pasted%20image%2020250503162740.png)

**Observación**

pytest no ejecuta las pruebas en un orden pseudoaleatorio por defecto. En pytest, el orden de ejecución de las pruebas sigue la secuencia en la que se encuentran en los archivos de prueba. Es decir, las pruebas se ejecutan en el mismo orden en que están definidas dentro de cada archivo de prueba.

Sin embargo, si se desea ejecutar las pruebas en un orden aleatorio, pytest ofrece un plugin llamado pytest-randomly, que permite que las pruebas se ejecuten en un orden aleatorio o pseudoaleatorio, garantizando que los casos de prueba no dependan del orden de ejecución.

```bash
pytest --randomly-seed=RANDOMLY_SEED
```

En esta ejecución el primer test que evalua es el de la función `pop()`

![](Attachments/Pasted%20image%2020250503163809.png)

## **Paso 3: Escribiendo aserciones para el método `is_empty()`**

Se modifica función `test_is_empty()`:

```python
def test_is_empty():
    stack = Stack()
    assert stack.is_empty() == True  # La pila recién creada debe estar vacía
    stack.push(5)
    assert stack.is_empty() == False  # Después de agregar un elemento, la pila no debe estar vacía
```

## **Paso 4: Ejecuta pytest para verificar `is_empty()`**

![](Attachments/Pasted%20image%2020250503170641.png)

## **Paso 5: Escribiendo aserciones para el método `peek()`**

Modificamos la función `test_peek()`:

```python
def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2  # El valor superior debe ser el último agregado (2)
    assert stack.peek() == 2  # La pila no debe cambiar después de peek()
```

```python
def test_peek(self):
    self.stack.push(3)
    self.stack.push(5)
    self.assertEqual(self.stack.peek(), 5)
```

Ahora obtenemos el mensaje **PASSED** en `test_peek()` : 

![](Attachments/Pasted%20image%2020250503172714.png)

## **Paso 6: Escribiendo aserciones para el `método pop()`**

Modificamos la función `test_pop()` : 

```python
def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2  # El valor superior (2) debe eliminarse y devolverse
    assert stack.peek() == 1  # Después de pop(), el valor superior debe ser 1
```

Y también `test_pop(self)`:

```python
def test_pop(self):
    self.stack.push(3)
    self.stack.push(5)
    self.assertEqual(self.stack.pop(), 5)
    self.assertEqual(self.stack.peek(), 3)
    self.stack.pop()
    self.assertTrue(self.stack.is_empty())
```

Mostrando que ahora pasan 3 de los tests:

![](Attachments/Pasted%20image%2020250503173106.png)

## **Paso 7: Escribiendo aserciones para el `método push()`**

Modificamos la función `test_push()`:

```python
def test_push():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1  # El valor recién agregado debe estar en la parte superior
    stack.push(2)
    assert stack.peek() == 2  # Después de otro push, el valor superior debe ser el último agregado
```

También comprobamos con este código:

```python
 def test_push(self):
    self.stack.push(3)
    self.assertEqual(self.stack.peek(), 3)
    self.stack.push(5)
    self.assertEqual(self.stack.peek(), 5)
```

## **Paso 8: Ejecuta pytest para verificar todas las pruebas**

Ejecutamos por última vez `pytest` para mostrar que pasan todas las pruebas

![](Attachments/Pasted%20image%2020250503173619.png)

## **Paso 9: Agregando cobertura de pruebas con pytest-cov**

Nos muestra un 100% de cobertura

![](Attachments/Pasted%20image%2020250503180205.png)


