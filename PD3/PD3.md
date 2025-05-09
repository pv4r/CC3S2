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

1. Escribe funciones de Bash `marco` y `polo` que hagan lo siguiente: cada vez que ejecutes `marco`, debe guardarse de alguna manera el directorio de trabajo actual, luego, cuando ejecutes `polo`, sin importar en qué directorio te encuentres, `polo` te debe devolver (con `cd`) al directorio en el que ejecutaste `marco`. Para facilitar la depuración, puedes poner el código en un archivo `marco.sh` y recargarlo con `source marco.sh`.

	**Solución:**

	Se tiene que hacer `source marco.sh` luego de crearlo para cargar la información del script, es diferente a hacer  `./marco.sh` ya que este último comando ejecuta el script, es decir, las funciones y la variable existen hasta que el script acabe.

	`marco.sh`

	```bash
	#!/bin/bash

	# Guarda el directorio actual
	marco() {
	    export MARCO_DIR="$PWD"
	}

	# Vuelve al directorio guardado
	polo() {
	    if [ -n "$MARCO_DIR" ]; then
	        cd "$MARCO_DIR" || echo "Error: no se pudo acceder a $MARCO_DIR"
	    else
	        echo "MARCO_DIR no está definido. Ejecuta 'marco' primero."
	    fi
	}
	```

	Funcionamiento

	![](Attachments/Pasted%20image%2020250509135849.png)

2. Tienes un comando que falla muy raramente. Para depurarlo necesitas capturar su salida, pero puede llevar tiempo que falle. Escribe un script de Bash que ejecute el siguiente fragmento **hasta que falle**, capture sus flujos de salida estándar y de error en archivos, y finalmente imprima todo:

	**Solución:**

	- `>&2` : Redirecciona algo al canal de error (stderr)
	- `2>`: Redirecciona la salida de error

	`script_falla.sh`

	```bash
	#!/usr/bin/env bash

	n=$(( RANDOM % 100 ))
	
	if [[ n -eq 42 ]]; then
	   echo "Algo esta pasando!"
	   >&2 echo "El error fue por usar numero magicos"
	   exit 1
	fi

	echo "Todo salio de acuerdo al plan"

	```

	`capture.sh`

	```bash
	#!/usr/bin/env bash

	# Archivos temporales para guardar la salida
	out_file="logs.txt"
	err_file="error_logs.txt"
	
	# Bucle infinito hasta que el comando falle
	while true; do
	    # Ejecuta el comando y redirige stdout y stderr a archivos
	    ./script_falla.sh >"$out_file" 2>"$err_file"

	    # Verifica si falló
	    if [ $? -ne 0 ]; then
	        echo "¡El comando falló!"
	        echo "=== Salida estándar ==="
	        cat "$out_file"
	        echo "=== Salida de error ==="
	        cat "$err_file"
	        break
	    fi
	done
	```

	- `$?`: La variable `?` contiene el código de salida del último comando ejecutado, si sale 0 significa que no hubo error y si es distinto de 0 es porque ocurrió un fallo.

	Funcionamiento:

	![](Attachments/Pasted%20image%2020250509143801.png)

3. El `-exec` de `find` puede ser muy poderoso para realizar operaciones sobre los archivos que encuentra. Sin embargo, ¿qué pasa si queremos hacer algo con **todos** los archivos, como crear un archivo ZIP? Algunos comandos leen de **STDIN**, pero otros (como `tar`) necesitan recibir la lista de archivos como argumentos. Para unir ambos mundos tenemos `xargs`, que ejecuta un comando tomando su **STDIN** como lista de argumentos. Por ejemplo:

	```bash
	ls | xargs rm
	```

	Eliminará los archivos que `ls` lista.

	**Solución:**

	```bash
	find /path/ -type f -name "*.html" -print0 | xargs -0 zip archivos_html.zip
	```

	Donde:

	- `find /path/ -type f -name "*.html"`: Busca recursivamente todos los archivos con extensión `html` dentro de la carpeta.
	- `-print0`: Imprime los resultados separados por **null (`\0`)**, para evitar problemas con nombres que contienen espacios o saltos de línea.
	- `xargs -0`: Lee la entrada null-separated del `find` y la pasa como **argumentos individuales seguros** al siguiente comando.
	- `zip archivos_html.zip`: Crea un archivo llamado `archivos_html.zip`y mete dentro todos los archivos `html` que encontró

	`comprimir_html.sh`

	```bash
	#!/usr/bin/env bash

	# Verifica si se ingreso una ruta
	if [ -z "$1" ]; then
	    echo "Uso: $0 <ruta-de-la-carpeta>"
	    exit 1
	fi

	# Guarda la ruta proporcionada como variable
	CARPETA="$1"

	# Verifica si la ruta es válida
	if [ ! -d "$CARPETA" ]; then
	    echo "Error: '$CARPETA' no es un directorio válido"
	    exit 1
	fi

	# Ejecuta el comando de compresión
	find "$CARPETA" -type f -name "*.html" -print0 | xargs -0 zip archivos_html.zip

	echo "Archivo ZIP creado exitosamente: archivos_html.zip"
	```

	Funcionamiento:

	![](Attachments/Pasted%20image%2020250509151815.png)

4. Escribe un comando o script que, de forma recursiva, encuentre el archivo **más recientemente modificado** en un directorio. Y, más en general, ¿puedes listar todos los archivos por orden de recencia?

	**Solución:**

	Encontrar el archivo más reciente modificado

	```bash
	find /path/ -type f -printf "%T@ %p\n" | sort -n | tail -1 | cut -d' ' -f2-
	```

	Listar todos los archivos por tiempo de modificación

	```bash
	find /path/ -type f -printf "%T@ %p\n" | sort -nr | cut -d' ' -f2-
	```

	`archivos_recientes.sh`

	```bash
	#!/usr/bin/env bash

	# Verifica que se haya dado al menos un argumento (la ruta)
	if [ -z "$1" ]; then
	    echo "Uso: $0 <ruta> [--solo-uno]"
	    exit 1
	fi

	# Guarda la ruta del directorio
	CARPETA="$1"

	# Verifica que sea un directorio válido
	if [ ! -d "$CARPETA" ]; then
	    echo "Error: '$CARPETA' no es un directorio válido"
	    exit 1
	fi

	# Opción --solo-uno: mostrar solo el archivo más reciente
	if [ "$2" == "--solo-uno" ]; then
	    find "$CARPETA" -type f -printf "%T@ %p\n" | sort -n | tail -1 | cut -d' ' -f2-
	else
	    # Mostrar todos los archivos ordenados por fecha (más recientes primero)
	    find "$CARPETA" -type f -printf "%T@ %p\n" | sort -nr | cut -d' ' -f2-
	fi
	```


	Funcionamiento:

	![](Attachments/Pasted%20image%2020250509153807.png)

### Paso 12 - Expresiones regulares en bash


	







