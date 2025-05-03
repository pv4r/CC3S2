# Actividad: Ejecutar pruebas con pytest 

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

![](Attachments/Pasted%20image%2020250503120633.png)

## **Paso 2: Escribiendo y ejecutando pruebas con pytest**

Utilizando el comando `pytest -v` corremos las pruebas en modo detallado, como todas las pruebas aparecen de color verde, significa que todas pasaron.

![](Attachments/Pasted%20image%2020250503121221.png)

## **Paso 3: Añadiendo cobertura de pruebas con pytest-cov**

Para ejecutar las pruebas con un informa de cobertura se utiliza el complemento `pytest-cov`

```bash
pytest --cov=nombre_de_tu_paquete
```

En nuestro caso sólo mostramos un paquete que sería todo el proyecto.

![](Attachments/Pasted%20image%2020250503140248.png)

Si se desea generar un informa de cobertura en HTML, se agrega la opción `--cov-report=html`

![](Attachments/Pasted%20image%2020250503140849.png)

Si se desea un informa más detallado, que incluya las líneas no cubiertas, se agrega la opción `--cov-report=term-missing`

![](Attachments/Pasted%20image%2020250503142753.png)

Entonces, si quiero un informe HTML con la misma cantidad de detalles haría

```bash
pytest --cov=pruebas_con_pytest.triangle --cov-report=term-missing --cov-report=html
```

![](Attachments/Pasted%20image%2020250503143250.png)

![](Attachments/Pasted%20image%2020250503143329.png)

![](Attachments/Pasted%20image%2020250503143347.png)

## **Paso 4: Añadiendo colores automáticamente**

- Si se necesita forzar la aparición de colores se usa `--color=yes`

## **Paso 5: Automatizando la configuración de pytest**

### setup.cfg

- Utilizado cuando quieres centralizar la configuración del proyecto en un solo archivo

	![](Attachments/Pasted%20image%2020250503145514.png)

- Como resultado se aplica lo mencionado en el archivo

	![](Attachments/Pasted%20image%2020250503145611.png)

### pytest.ini

- Es un archivo de configuración específico para pytest. Solo contiene configuraciones que pytest usa directamente.

	![](Attachments/Pasted%20image%2020250503145927.png)

- **Importancia**

	- setup.cfg es para múltiples herramientas en el proyecto, mientras que pytest.ini es solo para configurar pytest.
	- En setup.cfg, las configuraciones de pytest deben ir bajo [tool:pytest].
	- En pytest.ini, las configuraciones se agrupan bajo el encabezado [pytest], ya que el archivo solo es para esa herramienta.

## **Paso 6: Ejecutando pruebas con la configuración automatizada** Una vez que hayas creado el archivo o setup.cfg pytest.ini, simplemente ejecuta pytest sin ningún parámetro adicional:

Ejecutamos `pytest` utilizando sólo el archivo `pytest.ini`,

![](Attachments/Pasted%20image%2020250503150208.png)
