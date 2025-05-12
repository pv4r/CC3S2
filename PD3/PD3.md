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

- `$1`: Captura el primer argumento
- `re`: Guarda la expresión regular
- `$email =~ $re`: Evalua si el email cumple con el regex
- `{BASH_REMATCH[n]}`: Retorna el n-esimo grupo capturado. Para `n=0` captura todo.

```bash
#!/usr/bin/env bash

email="$1"
re='^([[:alnum:]_.+-]+)@([[:alnum:]-]+\.[[:alnum:].-]+)$'
if [[ $email =~ $re ]]; then
  echo "Email válido"
  echo "Email: ${BASH_REMATCH[0]}"  # todo el email
  echo "Usuario: ${BASH_REMATCH[1]}"  # primer grupo
  echo "Dominio: ${BASH_REMATCH[2]}"  # segundo grupo
else
  echo "Email inválido"
fi

```

### Paso 13 – Expresiones regulares en Python

**Validar email**

`extract_emails.py`

- Se usa `[A-Za-z0-9]` como reemplazo de `[:alnum:]`, este último reconoce caracteres no ingleses.

```bash
#!/usr/bin/env python3

import re, sys
texto=sys.stdin.read()
pat=re.compile(r'([A-Za-z0-9_.+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9-.]+)')
for email in set(pat.findall(texto)):
    print(f"Email extraido: {email}")
```

Uso: 

Redirige el `stdout` de `cat` hacia el `stdin` de `extract_emails.py`

```bash
cat logs.txt | python3 extract_emails.py
```

**Validar nombre de rama**

- `git rev-parse --abbrev-ref HEAD`: Obtiene el nombre de la rama actual.

Regex:
1. `^` - Inicio de la cadena
2. `(feature|hotfix)` - Debe comenzar con "feature" o "hotfix"
3. `\/` - Seguido de una barra diagonal (/)
4. `[A-Z]{2,5}` - De 2 a 5 letras mayúsculas (ej: "ABC", "XYZ")
5. `-` - Un guión
6. `[0-9]+` - Uno o más dígitos (número de ticket/issue)
7. `-` - Otro guión
8. `[a-z0-9]+` - Uno o más caracteres en minúscula o números (descripción)
9. `(-[a-z0-9]+)*` - Opcional: más guiones con texto (para descripciones múltiples)
10. `$` - Fin de la cadena

```bash
#!/usr/bin/env bash
branch=$(git rev-parse --abbrev-ref HEAD)
# solo: feature/XYZ-123-descripcion o hotfix/XYZ-123
re='^(feature|hotfix)\/[A-Z]{2,5}-[0-9]+-[a-z0-9]+(-[a-z0-9]+)*$'
if [[ ! $branch =~ $re ]]; then
  echo "Nombre de rama inválido: $branch"
  echo "Formato correcto: feature/ABC-123-descripcion"
  exit 1
fi
```

**Validar mensaje de commit**

Regex:
1. `^` - Inicio de la cadena
2. `(feat|fix|docs|style|refactor|perf|test|chore)` - **Tipo** de commit:

    - `feat`: Nueva característica
    - `fix`: Corrección de bug
    - `docs`: Cambios en documentación
    - `style`: Cambios de formato (espacios, comas, etc.)
    - `refactor`: Cambios que no corrigen bugs ni añaden features
    - `perf`: Mejoras de rendimiento
    - `test`: Añadir o corregir tests
    - `chore`: Tareas de mantenimiento
3. `(\([a-z0-9_-]+\))?` - **Ámbito/scope** (opcional):

    - `\(` y `\)`: Paréntesis literales
    - `[a-z0-9_-]+`: 1+ caracteres en minúscula, números, guiones o guiones bajos
    - `?`: Hace que todo este grupo sea opcional
4. `(!)?` - **Breaking change** (opcional):

    - `!`: Indica cambios que rompen compatibilidad con versiones anteriores
5. `:` - Dos puntos seguidos de espacio (separador obligatorio)
6. `.{10,}` - **Descripción**:

    - `.`: Cualquier caracter (excepto salto de línea)
    - `{10,}`: Mínimo 10 caracteres
7. `$` - Fin de la cadena

```bash
#!/usr/bin/env bash
msg_file=$1
# tipo(scope)!?: descripción de al menos 10 caracteres
re='^(feat|fix|docs|style|refactor|perf|test|chore)(\([a-z0-9_-]+\))?(!)?: .{10,}$'
if ! grep -Eq "$re" "$msg_file"; then
  echo "Mensaje de commit no cumple conventional commits"
  echo "Ej: fix(parser): manejar comillas dobles correctamente"
  exit 1
fi
```

**Validar formato de tag semántico (SemVer)** 

Regex: 

1. **Versión Básica (Obligatoria)**:

    - `^` - Inicio de la cadena
    - `v?` - 'v' opcional al inicio (ej: v1.0.0 o 1.0.0)
    - `[0-9]+` - Número mayor (Major) - 1+ dígitos
    - `\.` - Punto literal
    - `[0-9]+` - Número menor (Minor) - 1+ dígitos
    - `\.` - Punto literal
    - `[0-9]+` - Número de parche (Patch) - 1+ dígitos
2. **Pre-release (Opcional)**:

    - `(-[0-9A-Za-z.-]+)?` - Grupo opcional que:
        - Comienza con guión `-`
        - Contiene 1+ caracteres alfanuméricos, guiones o puntos
        - Ejemplos: -alpha, -beta.1, -rc.2
3. **Metadata (Opcional)**:

    - `(\+[0-9A-Za-z.-]+)?` - Grupo opcional que:
        - Comienza con signo más `+`
        - Contiene 1+ caracteres alfanuméricos, guiones o puntos
        - Ejemplos: +exp, +20130313144700, +sha.5114f85
4. `$` - Fin de la cadena

```bash
#!/usr/bin/env bash
tag="$1"
# vX.Y.Z o X.Y.Z-prerelease+metadata
re='^v?[0-9]+\.[0-9]+\.[0-9]+(-[0-9A-Za-z.-]+)?(\+[0-9A-Za-z.-]+)?$'
if [[ ! $tag =~ $re ]]; then
  echo "Tag inválido: $tag"
  echo "Formato semver: 1.2.3, v1.2.3-beta+exp"
  exit 1
fi
```

**Extraer issue IDs de mensajes (`git log`)**

Regex:
1. **`git log --oneline`**:

    - Muestra el historial de commits en formato compacto (una línea por commit)
    - Ejemplo de salida:
        ```
        1234567 [PROJ-123] Fix issue with login
        89abcde [TASK-456] Update README
        2345678 [BUG-789] Fix typo in code
        ```
2. **`grep -Po '(?<=\[)[A-Z]{2,5}-[0-9]+(?=\])'`**:

    - `-P`: Usa expresiones regulares Perl (más potentes)
    - `-o`: Muestra solo la parte que coincide (no toda la línea)
    - La expresión regular tiene 3 partes:
        a. **`(?<=\[)`** - Lookbehind positivo:
        - Busca un corchete de apertura `[` pero no lo incluye en el resultado
        - Asegura que el ID viene después de `[`
        b. **`[A-Z]{2,5}-[0-9]+`** - Patrón del ticket:
        - `[A-Z]{2,5}`: 2 a 5 letras mayúsculas (ej: PROJ, TASK, BUG)
        - `-`: Un guión separador
        - `[0-9]+`: 1 o más dígitos (número del ticket)
        c. **`(?=\])`** - Lookahead positivo:
        - Busca un corchete de cierre `]` pero no lo incluye en el resultado
        - Asegura que el ID termina antes de `]`
		
3. **`sort -u`**:

    - Ordena los resultados alfabéticamente
    - `-u`: Muestra solo valores únicos (elimina duplicados)

```bash
git log --oneline | \
  grep -Po '(?<=\[)[A-Z]{2,5}-[0-9]+(?=\])' | sort -u
# Explicación:
# (?<=\[)  ─ lookbehind para "["
# [A-Z]{2,5}-[0-9]+  ─ proyecto-1234
# (?=\])   ─ lookahead para "]"
```

**Detectar merges automáticos y extraer la rama objetivo**

Regex:
1. **`git log --grep='^Merge branch' --pretty=format:'%s'`**:

    - `--grep='^Merge branch'`: Filtra commits cuyo mensaje comienza con "Merge branch"
    - `--pretty=format:'%s'`: Muestra solo el asunto (subject) del commit
    - Ejemplo de salida:
        ```
        Merge branch 'feature/ABC-123'
        Merge branch 'hotfix/XYZ-456'
        Merge branch 'bugfix/DEF-789'
        ```
        
2. **`grep -Po "(?<=Merge branch ')[^']+"`**:

    - `-P`: Usa expresiones regulares Perl (para soportar lookbehinds)
    - `-o`: Muestra solo la parte que coincide
    - La expresión regular tiene:
        - `(?<=Merge branch ')`: Lookbehind para el texto "Merge branch '"
        - `[^']+`: Captura uno o más caracteres que no sean comilla simple (el nombre de la rama)

```bash
git log --grep='^Merge branch' --pretty=format:'%s' | \
  grep -Po '(?<=Merge branch ')[^']+' 
# Captura el nombre de la rama tras "merge branch '<rama>'"
```

**Paso con grupo nombrado y alternancia**

Detalles de la función:

1. **Decorador `@given`**:
    
    - Define un paso tipo "Given" (dado/precondición)
    - Recibe una expresión regular que debe coincidir con el paso en el archivo .feature
        
2. **Expresión Regular**:
    
    - `r'^...$'`: Cadena raw (sin escapar) que debe coincidir completamente
    - `(?P<user>[A-Za-z0-9_]+)`: Grupo nombrado "user" que captura:
        - Letras mayúsculas/minúsculas, números y guiones bajos
        - `+` indica 1 o más caracteres
    - `tiene`: Texto literal " tiene "
    - `(?P<count>[0-9]+)`: Grupo nombrado "count" que captura:
        - Solo dígitos (0-9)
    - `(artículos|productos)`: Grupo no nombrado que acepta:
        - "artículos" o "productos"
            
3. **Función step_user_items**:
    
    - Recibe el contexto de Behave (`context`)
    - Recibe los parámetros capturados (`user` y `count`)
    - Almacena los valores en el contexto para usarlos en pasos posteriores
    - Convierte `count` a entero con `int(count)`

```python
from behave import given

@given(r'^(?P<user>[A-Za-z0-9_]+) tiene (?P<count>[0-9]+) (artículos|productos)$')
def step_user_items(context, user, count):
    # user: nombre de usuario
    # count: número de artículos o productos
    context.user = user
    context.count = int(count)
```

**Paso con partes opcionales y lookahead**

Detalles de la función:

1. **Expresión Regular Compleja**:
    
    - `^el usuario intenta`: Texto inicial obligatorio
    - `(?:...)`: Grupo no capturado (no crea parámetro en la función)
    - `iniciar sesión`: Texto opcional (por estar dentro de (?:...)?)
    - `(?: con contraseña "(?P<pw>[^"]+)")?`: Subgrupo opcional dentro del grupo opcional
        - `?P<pw>`: Grupo nombrado que captura la contraseña
        - `[^"]+`: Cualquier carácter excepto comillas (1 o más)
    - Los `?` al final hacen que cada grupo sea opcional
        
2. **Variaciones que Coinciden**:
    
    - `el usuario intenta` (solo texto base)
    - `el usuario intenta iniciar sesión` (sin contraseña)
    - `el usuario intenta iniciar sesión con contraseña "miClave123"` (con contraseña)
        
3. **Función step_login_optional_pw**:
    
    - `pw=None`: Parámetro opcional con valor por defecto
    - Almacena la contraseña en `context.pw` (será None si no se proporciona)

```python
from behave import when

@when(r'^el usuario intenta(?: iniciar sesión(?: con contraseña "(?P<pw>[^"]+)")?)?$')
def step_login_optional_pw(context, pw=None):
    # El paso coincide con:
    #   "el usuario intenta"
    #   "el usuario intenta iniciar sesión"
    #   'el usuario intenta iniciar sesión con contraseña "abc"'
    context.pw = pw
```

**Validar formatos de fecha dentro de un paso**

Detalles de la función:

1. **Expresión Regular**:
    
    - `^la fecha de entrega es` : Texto literal inicial
    - `(?P<date>\d{4}-\d{2}-\d{2})`: Grupo nombrado "date" que captura:
        - `\d{4}`: 4 dígitos (año)
        - `-`: guión separador
        - `\d{2}`: 2 dígitos (mes)
        - `-`: guión separador
        - `\d{2}`: 2 dígitos (día)
    - `$`: Fin de la cadena
        
2. **Validación de Fecha**:
    
    - `datetime.strptime(date, '%Y-%m-%d')` convierte el string a objeto datetime:
        - `%Y`: Año con 4 dígitos
        - `%m`: Mes con 2 dígitos (01-12)
        - `%d`: Día con 2 dígitos (01-31)
    - Si la fecha es inválida (ej: "2025-13-01"), lanzará ValueError
        
3. **Ejemplos Válidos**:
    
    - "la fecha de entrega es 2025-04-16"
    - "la fecha de entrega es 2023-12-31"
        
4. **Ejemplos Inválidos**:
    
    - "la fecha de entrega es 25-04-16" (año corto)
    - "la fecha de entrega es 2025/04/16" (separadores incorrectos)
    - "la fecha de entrega es 2025-13-01" (mes inválido)
    - "la fecha de entrega es 2025-04-31" (abril solo tiene 30 días)

```python
from behave import then

@then(r'^la fecha de entrega es (?P<date>\d{4}-\d{2}-\d{2})$')
def step_check_date(context, date):
    # date: "2025-04-16"
    import datetime
    datetime.datetime.strptime(date, '%Y-%m-%d')
```

**Step definition para comandos Git**

Detalles de la función:

1. **Obtener rama actual**:
    
    - `subprocess.check_output()`: Ejecuta un comando en el sistema
    - `['git','rev-parse','--abbrev-ref','HEAD']`: Comando Git para obtener el nombre de la rama actual
        - `rev-parse`: Comando interno de Git para interpretar referencias
        - `--abbrev-ref`: Devuelve el nombre abreviado de la rama
        - `HEAD`: Referencia a la confirmación actual
    - `.decode().strip()`: Convierte la salida binaria a string y elimina espacios/retornos
        
2. **Verificación**:
    
    - `assert current == branch`: Compara la rama actual con la especificada
    - Si no coinciden, la prueba fallirá con un AssertionError

Ejemplos de uso:

```gherkin
Dado que estoy en la rama "feature/login"
Cuando hago cambios en el código
Entonces puedo confirmarlos en esta rama
```

Casos que Acepta:

- `estoy en la rama "main"`
- `estoy en la rama "feature/user-authentication"`
- `estoy en la rama "hotfix/v1.2.3"`

```python
from behave import given

@given(r'^estoy en la rama "(?P<branch>[a-z0-9/_-]+)"$')
def step_on_branch(context, branch):
    import subprocess
    current = subprocess.check_output(['git','rev-parse','--abbrev-ref','HEAD']).decode().strip()
    assert current == branch
```

**Capturar tablas Gherkin con regex dinámico**

```python
from behave import then
import re

@then(r'^los siguientes usuarios:$')
def step_table_users(context):
    # context.table tendrá filas:
    # | user   | age |
    # | alice  | 30  |
    # Validación adicional:
    for row in context.table:
        assert re.match(r'^[a-z]+$', row['user'])
        assert re.match(r'^[0-9]{1,3}$', row['age'])
```

**Scenario outline con ejemplos que usan regex**

```gherkin
Scenario Outline: Validación de correos
  Given el email "<email>"
  When valido el formato
  Then debe ser <valid>

Examples:
  | email                 | valid  |
  | user@example.com      | True   |
  | invalid-email@        | False  |
  | otra.cosa@dominio.org | True   |
```

```python
from behave import given, then
import re

EMAIL_RE = re.compile(r'^[[:alnum:]_.+-]+@[[:alnum:]-]+\.[[:alnum:].-]+$')

@given(r'el email "(?P<email>[^"]+)"')
def step_set_email(context, email):
    context.email = email

@then(r'debe ser (?P<valid>True|False)')
def step_check_email(context, valid):
    match = bool(EMAIL_RE.match(context.email))
    assert match == (valid == 'True')
```



























