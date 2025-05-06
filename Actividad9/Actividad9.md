# Actividad: Red-Green-Refactor

Empezamos con la siguiente estructura:

![](Attachments/Pasted%20image%2020250505210227.png)

## **Primera iteración (RGR 1): Agregar artículos al carrito**

### **1. Escribir una prueba que falle (Red)**

Escribimos una prueba para **agregar un artículo a un carrito**, pero como aún no tenemos implementada la clase `ShoppingCart`, entonces al ejecutar `pytest` obtendremos un error

```python
# test_shopping_cart.py
import pytest
from shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"apple": {"quantity": 2, "unit_price": 0.5}}
```

Resultado: No encuentra la clase `ShoppingCart`

![](Attachments/Pasted%20image%2020250505211449.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos la clase `ShoppingCart` con el método `add_item`

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
```

Resultado:

![](Attachments/Pasted%20image%2020250505215258.png)

### **3. Refactorizar el código si es necesario (Refactor)**

No es necesario refactorizar porque el código se pequeño

## **Segunda iteración (RGR 2): Eliminar artículos del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos `test_remove_item` para eliminar un artículo del carrito

```python
# test_shopping_cart.py
def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.remove_item("apple")
    assert cart.items == {}
```

Resultado: Falla porque `ShoppingCart` aún no tiene el método `remove_item`

![](Attachments/Pasted%20image%2020250505220616.png)

### **2. Implementar el código para pasar la prueba (Green)**

Agregamos el método `remove_item` a la clase `ShoppingCart`

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado:

![](Attachments/Pasted%20image%2020250505221034.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Mejoramos el método `add_item` para que aumente la cantidad de items si vuelvo a agregar el mismo artículo.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado:

![](Attachments/Pasted%20image%2020250505221034.png)

## **Tercera iteración (RGR 3): Calcular el total del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para calcular el total del carrito.

```python
# test_shopping_cart.py
def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    total = cart.calculate_total()
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25
```

Resultado: El test falla porque no existe el método `calculate_total`

![](Attachments/Pasted%20image%2020250505222109.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos el método `calculate_total`.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["quantity"] * item["unit_price"]
        return total
```

Resultado:

![](Attachments/Pasted%20image%2020250505222351.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Refactorizamos el método `calcular_total` para utilizar  comprensión de listas.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        return sum(item["quantity"] * item["unit_price"] for item in self.items.values())
```

Resultado:

![](Attachments/Pasted%20image%2020250505222659.png)
## Código final acumulativo

`shopping_cart.py`

![](Attachments/Pasted%20image%2020250505231259.png)

`test_shopping_cart.py`

![](Attachments/Pasted%20image%2020250505231337.png)
## **Ejecutar las pruebas**

`ShoppingCart` funciona correctamente después de las tres iteraciones del proceso RGR.

![](Attachments/Pasted%20image%2020250505223113.png)

## Más iteraciones

Las funcionalidades a implementar serán:

1. **Agregar artículos al carrito**
2. **Eliminar artículos del carrito**
3. **Calcular el total del carrito**
4. **Aplicar descuentos al total**
## **Cuarta iteración (RGR 4): Agregar artículos al carrito**

### **1. Escribir una prueba que falle (Red)**

Escribimos una prueba para agregar un artículo al carrito.

```python
# test_shopping_cart.py
import pytest
from shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"apple": {"quantity": 2, "unit_price": 0.5}}
```

Resultado:

![](Attachments/Pasted%20image%2020250505231719.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos la clase `ShoppingCart` con el método `add_item`

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
```

Resultado:

![](Attachments/Pasted%20image%2020250505231840.png)

### **3. Refactorizar el código si es necesario (Refactor)**

El código no requiere factorización porque es sencillo

## **Quinta iteración (RGR 5): eliminar artículos del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para eliminar un artículo del carrito.

```python
# test_shopping_cart.py
def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.remove_item("apple")
    assert cart.items == {}
```

Resultado: Falla porque no existe el método `remover_item`

![](Attachments/Pasted%20image%2020250505232213.png)

### **2. Implementar el código para pasar la prueba (Green)**

Añadimos el método `remove_item` a la clase `ShoppingCart`.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado:

![](Attachments/Pasted%20image%2020250505232337.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Podemos mejorar el método `add_item` para manejar la adición de múltiples cantidades del mismo artículo.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado:

![](Attachments/Pasted%20image%2020250505232806.png)

## **Sexta iteración (RGR 6): calcular el total del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para calcular el total del carrito.

```python
# test_shopping_cart.py
def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    total = cart.calculate_total()
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25
```

Resultado: No existe `calculate_total`

![](Attachments/Pasted%20image%2020250505232951.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos el método `calculate_total`.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["quantity"] * item["unit_price"]
        return total
```

Resultado:

![](Attachments/Pasted%20image%2020250505233152.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Podemos optimizar el método `calculate_total` utilizando comprensión de listas

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        return sum(item["quantity"] * item["unit_price"] for item in self.items.values())
```

Resultado:

![](Attachments/Pasted%20image%2020250505233332.png)

## **Séptima iteración (RGR 7): aplicar descuentos al total**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para aplicar un descuento al total del carrito.

```python
# test_shopping_cart.py
def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)  # Descuento del 10%
    total = cart.calculate_total()
    expected_total = (2*0.5 + 3*0.75) * 0.9  # Aplicando 10% de descuento
    expected_total = rounded(expected_total, 2) # Redondear a 2 decimales
    assert total == expected_total
```

Resultado: No existe `apply_discount`

![](Attachments/Pasted%20image%2020250505233544.png)

### **2. Implementar el código para pasar la prueba (Green)**

Añadimos el método `apply_discount` y ajustamos `calculate_total` para considerar el descuento.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento, por ejemplo, 10 para 10%
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return total
    
    def apply_discount(self, discount_percentage):
        self.discount = discount_percentage
```

Resultado: 

![](Attachments/Pasted%20image%2020250505233800.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Por simplicidad, mantendremos un único descuento y añadiremos validación para que el descuento esté entre 0 y 100.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total, 2)  # Redondear a 2 decimales
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
```

Resultado:

![](Attachments/Pasted%20image%2020250505234400.png)

## Código final acumulativo

`shopping_cart.py`

![](Attachments/Pasted%20image%2020250505234534.png)

`test_shopping_cart.py`

![](Attachments/Pasted%20image%2020250505234613.png)

## Ejecutar las pruebas

`ShoppingCart` funciona correctamente luego de las 4 iteraciones

![](Attachments/Pasted%20image%2020250505234747.png)

## RGR, mocks, stubs e inyección de dependencias

Continuaremos mejorando la funcionalidad de la clase `ShoppingCart`, añadiendo una nueva característica en cada iteración. Las funcionalidades a implementar serán:

1. **Agregar artículos al carrito**
2. **Eliminar artículos del carrito**
3. **Calcular el total del carrito**
4. **Aplicar descuentos al total**
5. **Procesar pagos a través de un servicio externo**

## **Octava iteración (RGR 8): agregar artículos al carrito**

### **1. Escribir una prueba que falle (Red)**

Escribimos una prueba para agregar un artículo al carrito.

```python
# test_shopping_cart.py
import pytest
from shopping_cart import ShoppingCart

def test_add_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)  # nombre, cantidad, precio unitario
    assert cart.items == {"apple": {"quantity": 2, "unit_price": 0.5}}
```

Resultado: No existe la clase `Shoppingcart`

![](Attachments/Pasted%20image%2020250505235634.png)

### 2. Implementar el código para pasar la prueba (Green)

Implementamos la clase `ShoppingCart` con el método `add_item`

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
```

Resultado:

![](Attachments/Pasted%20image%2020250505235752.png)

### **3. Refactorizar el código si es necesario (Refactor)**

El código es sencillo y no requiere refactorización inmediata.

## **Novena iteración (RGR 9): eliminar artículos del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para eliminar un artículo del carrito.

```python
# test_shopping_cart.py
def test_remove_item():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.remove_item("apple")
    assert cart.items == {}
```

Resultado: La clase `ShoppingCart` aún no tiene el método `remove_item`

![](Attachments/Pasted%20image%2020250505235954.png)

### **2. Implementar el código para pasar la prueba (Green)**

Añadimos el método `remove_item` a la clase `ShoppingCart`.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado:

![](Attachments/Pasted%20image%2020250506000117.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Mejoramos el método `add_item` para manejar la adición de múltiples cantidades del mismo artículo.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
```

Resultado: 

![](Attachments/Pasted%20image%2020250506000318.png)

## **Décima iteración (RGR 10): calcular el total del carrito**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para calcular el total del carrito.

```python
# test_shopping_cart.py
def test_calculate_total():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    total = cart.calculate_total()
    assert total == 2*0.5 + 3*0.75  # 2*0.5 + 3*0.75 = 1 + 2.25 = 3.25
```

Resultado: No existe `calculate_total`

![](Attachments/Pasted%20image%2020250506000437.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos el método `calculate_total`.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = 0
        for item in self.items.values():
            total += item["quantity"] * item["unit_price"]
        return total
```

Resultado: 

![](Attachments/Pasted%20image%2020250506000606.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Optimizar el método `calculate_total` utilizando comprensión de listas.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        return sum(item["quantity"] * item["unit_price"] for item in self.items.values())
```

Resultado:

![](Attachments/Pasted%20image%2020250506000716.png)

## **Onceava iteración (RGR 11): aplicar descuentos al total**

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para aplicar un descuento al total del carrito.

```python
# test_shopping_cart.py
def test_apply_discount():
    cart = ShoppingCart()
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)  # Descuento del 10%
    total = cart.calculate_total()
    expected_total = (2*0.5 + 3*0.75) * 0.9  # Aplicando 10% de descuento
    assert total == round(expected_total, 2)  # Redondear a 2 decimales
```

Resultado: La clase `ShoppingCart` no tiene el método `apply_discount`

![](Attachments/Pasted%20image%2020250506095233.png)

### **2. Implementar el código para pasar la prueba (Green)**

Añadimos el método `apply_discount` y ajustamos `calculate_total` para considerar el descuento.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total, 2)  # Redondear a 2 decimales
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
```

Resutado:

![](Attachments/Pasted%20image%2020250506095417.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Podemos mantener la implementación actual.

## **Doceava iteración (RGR 5): Procesar Pagos a través de un Servicio Externo**

Implementaremos **inyección de dependencias** para facilitar el uso de **mocks** y **stubs** en las pruebas.

### **1. Escribir una prueba que falle (Red)**

Añadimos una prueba para procesar el pago.

```python
# test_shopping_cart.py
from unittest.mock import Mock

def test_process_payment():
    payment_gateway = Mock()
    payment_gateway.process_payment.return_value = True
    
    cart = ShoppingCart(payment_gateway=payment_gateway)
    cart.add_item("apple", 2, 0.5)
    cart.add_item("banana", 3, 0.75)
    cart.apply_discount(10)
    
    total = cart.calculate_total()
    result = cart.process_payment(total)
    
    payment_gateway.process_payment.assert_called_once_with(total)
    assert result == True
```

Resultado: 

![](Attachments/Pasted%20image%2020250506135044.png)

### **2. Implementar el código para pasar la prueba (Green)**

Implementamos el método `process_payment` en la clase `ShoppingCart`, utilizando inyección de dependencias para el gateway de pago.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self, payment_gateway=None):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento
        self.payment_gateway = payment_gateway  # Inyección de dependencia
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total, 2)  # Redondear a 2 decimales
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    
    def process_payment(self, amount):
        if not self.payment_gateway:
            raise ValueError("No payment gateway provided.")
        return self.payment_gateway.process_payment(amount)
```

Resultado:

![](Attachments/Pasted%20image%2020250506142555.png)

### **3. Refactorizar el código si es necesario (Refactor)**

Podemos mejorar la gestión del `payment_gateway` asegurándonos de que es inyectado y manejando posibles excepciones.

```python
# shopping_cart.py
class ShoppingCart:
    def __init__(self, payment_gateway=None):
        self.items = {}
        self.discount = 0  # Porcentaje de descuento
        self.payment_gateway = payment_gateway  # Inyección de dependencia
    
    def add_item(self, name, quantity, unit_price):
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"quantity": quantity, "unit_price": unit_price}
    
    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
    
    def calculate_total(self):
        total = sum(item["quantity"] * item["unit_price"] for item in self.items.values())
        if self.discount > 0:
            total *= (1 - self.discount / 100)
        return round(total, 2)  # Redondear a 2 decimales
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.discount = discount_percentage
        else:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    
    def process_payment(self, amount):
        if not self.payment_gateway:
            raise ValueError("No payment gateway provided.")
        try:
            success = self.payment_gateway.process_payment(amount)
            return success
        except Exception as e:
            # Manejar excepciones según sea necesario
            raise e
```

Resultado:

![](Attachments/Pasted%20image%2020250506142821.png)

## **Código final acumulativo**

`shopping_cart.py`

![](Attachments/Pasted%20image%2020250506142907.png)
`test_shopping_cart.py`

![](Attachments/Pasted%20image%2020250506143009.png)

## **Ejecutar las pruebas**

Todas las pruebas pasan

![](Attachments/Pasted%20image%2020250506143106.png)

## Ejercicio

Desarrollaremos las 6 iteraciones de Desarrollo Guiado por Pruebas (TDD) (Red-Green-Refactor) aplicadas a la clase `UserManager`, incluyendo casos de mocks, stubs, fakes, spies e inyección de dependencias.

## **Iteración 1: Agregar usuario (Básico)**

### **Paso 1 (Red): Escribimos la primera prueba**

Creamos la prueba que verifica que podemos agregar un usuario con éxito.

```python
import pytest
from user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
```

Resultado: No encuentra las clases `UserManager` y `UserAlreadyExistsError`

![](Attachments/Pasted%20image%2020250506144549.png)

### **Paso 2 (Green): Implementamos lo mínimo para que pase la prueba**

```python
class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users
```

Resultado:

![](Attachments/Pasted%20image%2020250506144926.png)

### **Paso 3 (Refactor)**

Por ahora, el diseño es simple y cumple su función.

## **Iteración 2: Autenticación de usuario (Introducción de una dependencia para Hashing)**

### **Paso 1 (Red): Escribimos la prueba**

Queremos verificar que `UserManager` autentica correctamente a un usuario con la contraseña adecuada. Asumiremos que la contraseña se almacena en hash.

```python
import pytest
from user_manager import UserManager, UserNotFoundError, UserAlreadyExistsError

class FakeHashService:
    """
    Servicio de hashing 'falso' (Fake) que simplemente simula el hashing
    devolviendo la cadena con un prefijo "fakehash:" para fines de prueba.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."
```

Resultado:

![](Attachments/Pasted%20image%2020250506152345.png)

### Paso 2 (Green): Implementamos la funcionalidad y la DI

Modificamos `user_manager.py` para inyectarle un servicio de hashing:

```python
class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None):
        """
        Si no se provee un servicio de hashing, se asume un hash trivial por defecto
        (simplemente para no romper el código).
        """
        self.users = {}
        self.hash_service = hash_service
        if not self.hash_service:
            # Si no pasamos un hash_service, usamos uno fake por defecto.
            # En producción, podríamos usar bcrypt o hashlib.
            class DefaultHashService:
                def hash(self, plain_text: str) -> str:
                    return plain_text  # Pésimo, pero sirve de ejemplo.

                def verify(self, plain_text: str, hashed_text: str) -> bool:
                    return plain_text == hashed_text

            self.hash_service = DefaultHashService()

    def add_user(self, username, password):
        if self.user_exists(username):
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self, username):
        return username in self.users

    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        stored_hash = self.users[username]
        return self.hash_service.verify(password, stored_hash)
```

Resultado:

![](Attachments/Pasted%20image%2020250506152449.png)

### Paso 3 (Refactor)

Por ahora la estructura cumple el propósito.

## Iteración 3: Uso de un Mock para verificar llamadas (Spy / Mock)

Ahora queremos asegurarnos de que, cada vez que llamamos a `add_user`, se invoque el método `hash` de nuestro servicio de hashing. Para ello, usaremos un **mock** que “espía” si se llamó el método y con qué parámetros. Esto sería un caso de **Spy o Mock**.

### Paso 1 (Red): Escribimos la prueba de "espionaje"

Instalaremos e importaremos `unittest.mock` (incluido con Python 3) para crear un mock:

```python
from unittest.mock import MagicMock

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)
```

Esta prueba verificará que, después de llamar a `add_user`, efectivamente el método `hash` se llamó **exactamente una vez** con `password` como argumento.

Resultado:

![](Attachments/Pasted%20image%2020250506153620.png)

### Paso 2 (Green): Probar que todo pasa

Si ejecutamos `pytest`, la prueba debería pasar de inmediato, pues la implementación actual ya cumple la expectativa.

### Paso 3 (Refactor)

No hay cambios adicionales.

## Iteración 4: Excepción al agregar usuario existente (Stubs/más pruebas negativas)

### Paso 1 (Red): Prueba

Aquí forzamos con una subclase `StubUserManager` que devuelva `True` en `user_exists`, simulando que el usuario “ya existe”. Así aislamos el comportamiento sin importar lo que pase dentro.

```python
def test_no_se_puede_agregar_usuario_existente_stub():
    # Este stub forzará que user_exists devuelva True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)
```

Resultado:

![](Attachments/Pasted%20image%2020250506154828.png)

### Paso 2 (Green)

La prueba debería pasar sin modificar el código.

### Paso 3 (Refactor)

Nada adicional por el momento.

## Iteración 5: Agregar un "Fake" repositorio de datos (Inyección de Dependencias)

Hasta ahora, `UserManager` guarda los usuarios en un diccionario interno (`self.users`). Supongamos que queremos que en producción se use una base de datos, pero en pruebas se use un repositorio en memoria. Esto es un uso típico de **Fake** o **InMemory** repos.

### Paso 1 (Red): Nueva prueba

Creamos una prueba que verifique que podemos inyectar un repositorio y que `UserManager` lo use.

```python
class InMemoryUserRepository:
    """Fake de un repositorio de usuarios en memoria."""
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_password):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_password

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)  # inyectamos repo
    username = "fakeUser"
    password = "fakePass"

    manager.add_user(username, password)
    assert manager.user_exists(username)
```

Resultado:

![](Attachments/Pasted%20image%2020250506155552.png)

### Paso 2 (Green): Implementación

Modificamos `UserManager` para recibir un `repo`:

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo
        if not self.repo:
            # Si no se inyecta repositorio, usamos uno interno por defecto
            self.repo = self._default_repo()
    
    def _default_hash_service(self):
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text
            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text
        return DefaultHashService()

    def _default_repo(self):
        # Un repositorio en memoria muy básico
        class InternalRepo:
            def __init__(self):
                self.data = {}
            def save_user(self, username, hashed_password):
                if username in self.data:
                    raise UserAlreadyExistsError(f"'{username}' ya existe.")
                self.data[username] = hashed_password
            def get_user(self, username):
                return self.data.get(username)
            def exists(self, username):
                return username in self.data
        return InternalRepo()

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)

    def user_exists(self, username):
        return self.repo.exists(username)

    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.hash_service.verify(password, stored_hash)
```

Resultado:
![](Attachments/Pasted%20image%2020250506164536.png)

### Paso 3 (Refactor)

El código quedó un poco más ordenado; `UserManager` no depende directamente de la estructura interna de almacenamiento.

## Iteración 6: Introducir un “Spy” de notificaciones (Envío de correo)

Finalmente, agregaremos una funcionalidad que, cada vez que se agrega un usuario, se envíe un correo de bienvenida. Para probar este envío de correo sin mandar correos reales, usaremos un **Spy** o **Mock** que verifique que se llamó al método `send_welcome_email` con los parámetros correctos.

### Paso 1 (Red): Prueba

```python
from unittest.mock import MagicMock

def test_envio_correo_bienvenida_al_agregar_usuario():
    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)
```

Resultado: `UserManager` tiene que aceptar como parámetro un `email_service`o

![](Attachments/Pasted%20image%2020250506164920.png)

### Paso 2 (Green): Implementamos la llamada al servicio de correo

Modificamos `UserManager`

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None, email_service=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service  # <--- nuevo

    # ... resto de métodos ...

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)
        if self.email_service:
            self.email_service.send_welcome_email(username)
```

Resultado:

![](Attachments/Pasted%20image%2020250506165122.png)

### Paso 3 (Refactor)

No se hace nada especial.

## Ejercicio integral

Estructura inicial

![](Attachments/Pasted%20image%2020250506170136.png)

## Iteración 1: Agregar usuario (Básico

### Paso 1 (Red): Primera prueba

```python
import pytest
from user_manager import UserManager, UserAlreadyExistsError

def test_agregar_usuario_exitoso():
    # Arrange
    manager = UserManager()
    username = "kapu"
    password = "securepassword"

    # Act
    manager.add_user(username, password)

    # Assert
    assert manager.user_exists(username), "El usuario debería existir después de ser agregado."
```

Resultado:

![](Attachments/Pasted%20image%2020250506170203.png)
### Paso 2 (Green): Implementamos lo mínimo

```python
class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self):
        self.users = {}  # Diccionario simple para guardar usuarios en memoria

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        self.users[username] = password

    def user_exists(self, username):
        return username in self.users
```

Resultado:

![](Attachments/Pasted%20image%2020250506170243.png)

### Paso 3 (Refactor)

Por ahora está bien.

## Iteración 2: Autenticación con inyección de un servicio de Hashing (Fake)

Queremos que la contraseña se almacene con un hash seguro.

### Paso 1 (Red): Nueva prueba

```python
class FakeHashService:
    """
    Servicio 'fake' que devuelve un hash simplificado con un prefijo, y lo verifica.
    """
    def hash(self, plain_text: str) -> str:
        return f"fakehash:{plain_text}"

    def verify(self, plain_text: str, hashed_text: str) -> bool:
        return hashed_text == f"fakehash:{plain_text}"

def test_autenticar_usuario_exitoso_con_hash():
    # Arrange
    hash_service = FakeHashService()
    manager = UserManager(hash_service=hash_service)

    username = "usuario1"
    password = "mypassword123"
    manager.add_user(username, password)

    # Act
    autenticado = manager.authenticate_user(username, password)

    # Assert
    assert autenticado, "El usuario debería autenticarse correctamente con la contraseña correcta."
```

Resultado: `UserManager` no acepta como argumento `hash_service`

![](Attachments/Pasted%20image%2020250506170536.png)

### Paso 2 (Green): Implementación con inyección de hash_service

```python
class UserNotFoundError(Exception):
    pass

class UserAlreadyExistsError(Exception):
    pass

class UserManager:
    def __init__(self, hash_service=None):
        """
        Inyectamos un servicio de hashing para no depender de una implementación fija.
        """
        self.users = {}
        self.hash_service = hash_service or self._default_hash_service()

    def _default_hash_service(self):
        # Hash por defecto si no se provee nada (inseguro, solo para no romper).
        class DefaultHashService:
            def hash(self, plain_text: str) -> str:
                return plain_text
            def verify(self, plain_text: str, hashed_text: str) -> bool:
                return plain_text == hashed_text
        return DefaultHashService()

    def add_user(self, username, password):
        if username in self.users:
            raise UserAlreadyExistsError(f"El usuario '{username}' ya existe.")
        hashed_pw = self.hash_service.hash(password)
        self.users[username] = hashed_pw

    def user_exists(self, username):
        return username in self.users

    def authenticate_user(self, username, password):
        if not self.user_exists(username):
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        stored_hash = self.users[username]
        return self.hash_service.verify(password, stored_hash)
```

Resultado:

![](Attachments/Pasted%20image%2020250506170729.png)

### Paso 3 (Refactor)

El código se ve razonable para esta etapa.

## Iteración 3: Uso de un Mock/Spy para verificar llamadas internas

Usaremos `MagicMock` de `unittest.mock` para espiar la llamada.

### Paso 1 (Red) Prueba con Spy

```python
from unittest.mock import MagicMock

def test_hash_service_es_llamado_al_agregar_usuario():
    # Arrange
    mock_hash_service = MagicMock()
    manager = UserManager(hash_service=mock_hash_service)
    username = "spyUser"
    password = "spyPass"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_hash_service.hash.assert_called_once_with(password)
```

Resultado:

![](Attachments/Pasted%20image%2020250506172431.png)

### Paso 2 (Green)

Nuestra implementación ya invoca `hash(...)`, así que al correr `pytest` pasa sin cambios.

### Paso 3 (Refactor)

Nada adicional.

## Iteración 4: Uso de Stubs para forzar comportamientos

Como ejemplo, usaremos un **stub** que fuerza que `user_exists` devuelva `True`, de modo que `UserAlreadyExistsError` se lance inmediatamente.

### Paso 1 (Red): Prueba

```python
def test_no_se_puede_agregar_usuario_existente_stub():
    # Creamos una subclase que "stubbea" user_exists para devolver True
    class StubUserManager(UserManager):
        def user_exists(self, username):
            return True

    stub_manager = StubUserManager()
    with pytest.raises(UserAlreadyExistsError) as exc:
        stub_manager.add_user("cualquier", "1234")

    assert "ya existe" in str(exc.value)
```

Resultado:

![](Attachments/Pasted%20image%2020250506172807.png)

### Paso 2 (Green)

Ya tenemos en `add_user` la lógica que lanza la excepción si existe el usuario. Nuestra subclase “stub” fuerza esa condición. La prueba debe pasar de inmediato.

### Paso 3 (Refactor)

Sin cambios.

## Iteración 5: Inyección de un repositorio (Fake)

Queremos que `UserManager` no dependa de un diccionario interno para almacenar usuarios, sino que podamos inyectar (en producción) un repositorio real (BD, etc.) y en las pruebas, un repositorio en memoria. Esto es otro ejemplo de **Fake**.

### Paso 1 (Red): Prueba con un repositorio fake

```python
class InMemoryUserRepository:
    """Fake de repositorio en memoria."""
    def __init__(self):
        self.data = {}

    def save_user(self, username, hashed_pw):
        if username in self.data:
            raise UserAlreadyExistsError(f"'{username}' ya existe.")
        self.data[username] = hashed_pw

    def get_user(self, username):
        return self.data.get(username)

    def exists(self, username):
        return username in self.data

def test_inyectar_repositorio_inmemory():
    repo = InMemoryUserRepository()
    manager = UserManager(repo=repo)  # inyectamos el repo
    username = "fakeUser"
    password = "fakePass"

    manager.add_user(username, password)
    assert manager.user_exists(username)
```

Resultado: Falla porque `UserManager` no recibe `repo` como parámetro

![](Attachments/Pasted%20image%2020250506173144.png)

### Paso 2 (Green): Implementación

En `user_manager.py`, modificamos el constructor y métodos:

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()

    def _default_hash_service(self):
        # ... igual que antes ...
    
    def _default_repo(self):
        # Repo interno por defecto
        class InternalRepo:
            def __init__(self):
                self.data = {}
            def save_user(self, username, hashed_pw):
                if username in self.data:
                    raise UserAlreadyExistsError(f"'{username}' ya existe.")
                self.data[username] = hashed_pw
            def get_user(self, username):
                return self.data.get(username)
            def exists(self, username):
                return username in self.data
        return InternalRepo()

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)

    def user_exists(self, username):
        return self.repo.exists(username)

    def authenticate_user(self, username, password):
        stored_hash = self.repo.get_user(username)
        if stored_hash is None:
            raise UserNotFoundError(f"El usuario '{username}' no existe.")
        return self.hash_service.verify(password, stored_hash)
```

Resultado: 

![](Attachments/Pasted%20image%2020250506173732.png)

### Paso 3 (Refactor)

Se ve razonable el código actual.

## Iteración 6: Spy de Servicio de Correo

Por último, simularemos que cada vez que se registra un nuevo usuario, se envía un correo de bienvenida. Queremos verificar esa llamada con un **Spy** o un **Mock**.

### Paso 1 (Red): Prueba

```python
def test_envio_correo_bienvenida_al_agregar_usuario():
    from unittest.mock import MagicMock

    # Arrange
    mock_email_service = MagicMock()
    manager = UserManager(email_service=mock_email_service)
    username = "nuevoUsuario"
    password = "NuevaPass123!"

    # Act
    manager.add_user(username, password)

    # Assert
    mock_email_service.send_welcome_email.assert_called_once_with(username)
```

Resultado: La clase `UserManager` no acepta `email_service`

![](Attachments/Pasted%20image%2020250506174113.png)

### Paso 2 (Green): Implementamos en `UserManager`

```python
class UserManager:
    def __init__(self, hash_service=None, repo=None, email_service=None):
        self.hash_service = hash_service or self._default_hash_service()
        self.repo = repo or self._default_repo()
        self.email_service = email_service

    # ... resto de métodos ...

    def add_user(self, username, password):
        hashed = self.hash_service.hash(password)
        self.repo.save_user(username, hashed)
        # Enviamos correo si se inyectó un email_service
        if self.email_service:
            self.email_service.send_welcome_email(username)
```

Resultado:

![](Attachments/Pasted%20image%2020250506174525.png)

### Paso 3 (Refactor)

Código listo.





















