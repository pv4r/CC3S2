# Herramientas del shell

Lee la ayuda de `man ls` y escribe un comando `ls` que liste archivos de la siguiente manera:

- Incluye todos los archivos, incluidos los ocultos

	```bash
	       -a, --all
              do not ignore entries starting with .
	```
	
- Los tamaños aparecen en formato legible por humanos (p. ej. 454M en lugar de 454279954)

	```bash
	       -h, --human-readable
              with -l and -s, print sizes like 1K 234M 2G etc.
	```
	
- Los archivos se ordenan por fecha de modificación (del más reciente al más antiguo)

	```bash
	       -c     with -lt: sort by, and show, ctime (time of last change  of  file status information); with -l: show ctime and sort by name; other‐wise: sort by ctime, newest first
	```
	
- La salida está coloreada

	```bash
	       --color[=WHEN]
              color the output WHEN; more info below
	```

Resultado:

![](Attachments/Pasted%20image%2020250507193740.png)

## Bash

### Paso 1 – Abrir la terminal y verificar Bash

![](Attachments/Pasted%20image%2020250507201211.png)

### Paso 2 – "Hello, World!": tu primer script

Uso de un Shebang

![](Attachments/Pasted%20image%2020250507201414.png)

Le damos permisos de ejecución al archivo antes de ejecutarlo

![](Attachments/Pasted%20image%2020250507201618.png)

### Paso 3 - Asignación de variables

- La palabra clave `readonly` hace que esa variable no pueda ser modificada más adelante en el script.

- La palabra clave `export` hace que esa variable esté disponible para cualquier **subproceso** que este script ejecute (por ejemplo, si se llama a otro script o programa desde aquí).

![](Attachments/Pasted%20image%2020250507202220.png)

![](Attachments/Pasted%20image%2020250507202806.png)

>[!caution]
>1. Usar siempre comillas al expandir variables: `"$VAR"`: Esto evita errores con espacios o caracteres especiales.
>
>	Ejemplo:
>	
>	```bash
>	NOMBRE="Juan Pérez"
>    echo "$NOMBRE"  # ✅ Correcto
>    echo $NOMBRE    # ⚠️ Incorrecto: se divide en dos palabras
>	```
>2. Usar `set -u`: Esto hace que el script **termine con error si usas una variable no definida**, en lugar de asumir que su valor es vacío.

### Paso 4 – Parámetros posicionales

- `$0` Muestra el nombre del script 
- `$n (con n entero positivo)` se utiliza para mostrar el valor del n-ésimo parámetro que ingresaste
- `$@` muestra todos los valores de los parámetros ingresados
- `$#` muestra la cantidad de parámetros ingresados
- `shift` equivale por defecto a `shift 1`, desplaza los parámetros 1 posición a la izquierda, es decir
	- `$2` pasa a ser `$1`
	- `$3` pasa a ser `$2`
	- Y así sucesivamente

![](Attachments/Pasted%20image%2020250507204355.png)

![](Attachments/Pasted%20image%2020250507205504.png)

### Paso 5 – Arrays en Bash

![](Attachments/Pasted%20image%2020250507205556.png)

- `FRUTAS[@]`: Accede a todos los elementos del array
- Se usa `declare -A` para crear un array asociativo (diccionario)

![](Attachments/Pasted%20image%2020250507212918.png)

### Paso 6 – Expansiones

#### Aritmética

- `((...))`: Evaluación aritmética/condicional

![](Attachments/Pasted%20image%2020250507213529.png)

#### Substitución de comandos

![](Attachments/Pasted%20image%2020250507215120.png)

#### Otras

![](Attachments/Pasted%20image%2020250507215434.png)

### Paso 7 – Pipes y redirección

#### Redirección de `stdout`

![](Attachments/Pasted%20image%2020250507220546.png)

#### Redirección de `stderr`

![](Attachments/Pasted%20image%2020250507221453.png)

#### Redirección de ambos

![](Attachments/Pasted%20image%2020250507221639.png)

#### Pipe

![](Attachments/Pasted%20image%2020250507221851.png)

- `|` conecta la salida de un comando con la entrada de otro
- `ps aux` lista todos los procesos
- `grep sshd` filtra sólo los que tienen sshd
- `awk '{print $2}'` impreime el segundo campo, i.e., el PID

#### Process substitution

- `<(command)` ejecuta un comando **y lo convierte en un archivo temporal "virtual"**.
- **Resultado:** Compara `file1` y `file2` **ordenados**, sin modificar los originales.

### Paso 8 – Condicionales

`if`

![](Attachments/Pasted%20image%2020250507235202.png)

`case`

![](Attachments/Pasted%20image%2020250507235538.png)

### Paso 9 - Bucles

![](Attachments/Pasted%20image%2020250507235904.png)

### Paso 10 – Funciones

![](Attachments/Pasted%20image%2020250508000020.png)

![](Attachments/Pasted%20image%2020250508000127.png)

### Paso 11 - Depuración

![](Attachments/Pasted%20image%2020250508000554.png)

## Ejercicios










