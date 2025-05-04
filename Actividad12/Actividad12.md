# Actividad: Revisión de fixtures en pruebas

## **Paso 1: Inicializar la base de datos**

En este paso, se configurará un fixture de prueba para conectar y desconectar de la base de datos.

- Primero creamos nuestro entorno virtual e instalamos los paquetes necesarios

	![](Attachments/Pasted%20image%2020250504101347.png)

- Creamos el archivo `models/__init__.py`

	```python
	"""
	Modelo de datos
	"""
	from flask import Flask
	from flask_sqlalchemy import SQLAlchemy
	
	app = Flask(__name__)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
	db = SQLAlchemy(app)
	```

- Se crea un fixture que ejecute las acciones a nivel módulo

	```python
	import pytest
	import sys
	import os
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
	from models import db, app

	@pytest.fixture(scope="module", autouse=True)
	def setup_database():
	    """Configura la base de datos antes y después de todas las pruebas"""
	    with app.app_context():
	        # Se ejecuta antes de todas las pruebas
	        db.create_all()
	        yield
	        # Se ejecuta después de todas las pruebas
	        db.session.close()
	```

- Salida de pytest

	![](Attachments/Pasted%20image%2020250504113547.png)
## **Paso 2: Cargar datos de prueba**

- Datos de prueba en `tests/fixtures/account_data.json`:

	```json
	[
	    {
	        "name": "Roberta Schaefer",
	        "email": "scotttodd@example.org",
	        "phone_number": "001-630-302-1546x3624",
	        "disabled": false
	    },
	    {
	        "name": "Amber Torres",
	        "email": "reedjoann@example.org",
	        "phone_number": "121.566.9078",
	        "disabled": true
	    },
	    {
	        "name": "Becky Franco",
	        "email": "joan88@example.com",
	        "phone_number": "908-592-2015x1764",
	        "disabled": false
	    },
	    {
	        "name": "Mary Barker",
	        "email": "mreyes@example.org",
	        "phone_number": "872.976.1464x40750",
	        "disabled": true
	    },
	    {
	        "name": "Jennifer Smith",
	        "email": "stevensjennifer@example.org",
	        "phone_number": "351.317.1639x79470",
	        "disabled": true
	    }
	]
	```

- Dentro de la clase `TestAccountModel` utilizamos el método `setup_class` para cargar los datos de prueba antes de que se ejecuten las pruebas

	```python
	class TestAccountModel:
    """Modelo de Pruebas de Cuenta"""

    @classmethod
    def setup_class(cls):
        """Conectar y cargar los datos necesarios para las pruebas"""
        global ACCOUNT_DATA
        with open('tests/fixtures/account_data.json') as json_data:
            ACCOUNT_DATA = json.load(json_data)
        print(f"ACCOUNT_DATA cargado: {ACCOUNT_DATA}")

    @classmethod
    def teardown_class(cls):
        """Desconectar de la base de datos"""
        pass  # Agrega cualquier acción de limpieza si es necesario
	```

## **Paso 3: Escribir un caso de prueba para crear una cuenta**

- Dentro de la clase `TestAccountModel`, se agrega el siguiente método de prueba:

	```python
	def test_create_an_account(self):
	    """Probar la creación de una sola cuenta"""
	    data = ACCOUNT_DATA[0]  # obtener la primera cuenta
	    account = Account(**data)
	    account.create()
	    assert len(Account.all()) == 1
	```

- Ejecutamos `pytest` para ver que funcione correctamente

	![](Attachments/Pasted%20image%2020250504120422.png)

## **Paso 4: Escribir un caso de prueba para crear todas las cuentas**

Ahora se escribirá una prueba que cree todas las cuentas del diccionario `ACCOUNT_DATA`

- Dentro de la clase `TestAccountModel`, agregamos esta prueba:

	```python
	def test_create_all_accounts(self):
	    """Probar la creación de múltiples cuentas"""
	    for data in ACCOUNT_DATA:
	        account = Account(**data)
	        account.create()
	    assert len(Account.all()) == len(ACCOUNT_DATA)
	```

- Ejecutamos `pytest` y deberíamos ver que pasaron 2 tests

	![](Attachments/Pasted%20image%2020250504122302.png)

## **Paso 5: Limpiar las tablas antes y después de cada prueba**

Se utilizarán los métodos `setup_method` y `teardown_method` dentro de la clase de pruebas para limpiar la base de datos antes y después de cada prueba.

- Dentro de la clase `TestAccountModel` agregamos lo siguiente:

	```python
	def setup_method(self):
	    """Truncar las tablas antes de cada prueba"""
	    db.session.query(Account).delete()
	    db.session.commit()

	def teardown_method(self):
	    """Eliminar la sesión después de cada prueba"""
	    db.session.remove()
	```

- De esta manera la base de datos queda limpia antes y después de ejecutar las pruebas
- Comprobamos que las pruebas pasan con `pytest`:

	![](Attachments/Pasted%20image%2020250504122914.png)

## Conclusiones

- `setup_class` se ejecuta **ANTES** de las pruebas, sirve para preparar el entorno de pruebas
- `teardown_class` se ejecuta **DESPUÉS** de todas las pruebas de la clase
- `setup_method` se ejecuta **ANTES** de cada método de prueba
- `teardown_method` se ejecuta **DESPUÉS** de cada método de prueba