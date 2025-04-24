# Actividad: Explorando diferentes formas de fusionar en Git

## Ejemplos

### 1. Fusión Fast-forward (git merge --ff)

Creación del repositorio `prueba-fast-forward-merge`, así como de las ramas `main` y `add-description`, cada una con solo un commit.

![](Attachments/Pasted%20image%2020250423211727.png)

**Pregunta:** Muestra la estructura de commits resultante

Al hacer `git merge` se intenta por defecto realizar un `merge --ff`, como no teníamos commits luego de la creación de `add-description` entonces `git` pudo mover el puntero de `main` hacia adelante, como se había esperado.

![](Attachments/Pasted%20image%2020250423212150.png)

### 2. Fusión No-fast-forward (git merge --no-ff)

Creación del repositorio `prueba-no-fast-forward-merge`, así como de las ramas `main` y `add-feature`, cada una con solo un commit.

![](Attachments/Pasted%20image%2020250423213519.png)

**Pregunta:** Muestra el log de commits resultante.

En este caso le decimos a `git` explícitamente que **NO** haga una fusión `fast-forward`. Aunque en este caso los commits de ambas ramas no divergen, de todas maneras se crea un nuevo commit en la rama `main`.

![](Attachments/Pasted%20image%2020250423213839.png)

### 3. Fusión squash (git merge --squash)

Creación el repositorio `prueba-squash-merge`, así como de las ramas `main` y `add-basic-files`, la primera con un commit y la segundo con 2 commits.

![](Attachments/Pasted%20image%2020250423215434.png)

Antes del merge:

![](Attachments/Pasted%20image%2020250423220120.png)

Después del merge:

![](Attachments/Pasted%20image%2020250423220612.png)

Notamos que realiza un `fast-forward` ya que las ramas no divergen, además ambos cambios de los commits ahora están en el `staging area` esperando a realizar el commit.

![](Attachments/Pasted%20image%2020250423220858.png)

Finalmente, se crea un nuevo commit utilizando los cambios de los 2 commits en la rama `add-basic-files`, esta rama no se elimina a menos que lo hagamos explícitamente.

### Ejercicios

1. Clonar un repositorio de git con múltiples ramas

	Notamos que las ramas no divergen, por lo tanto, se pueden mezclar usando `git merge --ff`

	![](Attachments/Pasted%20image%2020250423231959.png)

	Luego del `merge` el historial queda de esta manera

	![](Attachments/Pasted%20image%2020250423232128.png)

	**Pregunta:** ¿En qué situaciones recomendarías evitar el uso de `git merge --ff`? Reflexiona sobre las desventajas de este método.

	No es conveniente usarlo cuando se trabaja en un proyecto colaborativo con muchos desarrolladores, ya que si bien mantiene limpio el historial también oculta las razones por las que se realizó el merge.

2. **Simula un flujo de trabajo de equipo.**

	Historial antes de realizar los merges

	![](Attachments/Pasted%20image%2020250423235335.png)

	Cambiamos a la rama `main` y realizamos un `git merge --no-ff` a la rama `feature2` , observamos que se crea un nuevo commit en la rama `main`

	![](Attachments/Pasted%20image%2020250423235606.png)

	Aunque por el gráfico parezca que los commits de `feature2` se hicieron después que los de `feature3` esto es un tema del propio `git` y como dibuja las conexiones en la terminal, el correcto gráfico del historial sería este

	![](Attachments/Pasted%20image%2020250423235821.png)

	Después realizamos la misma operación de merge pero con la rama `feature3`

	![](Attachments/Pasted%20image%2020250423235941.png)

	Aquí el historial está mucho más dificil de leer que el anterior (al menos en la terminal), en el cliente `GitKraken` podemos visualizar de esta manera los dos commits de merge.

	![](Attachments/Pasted%20image%2020250424000154.png)

	**Pregunta:** ¿Cuáles son las principales ventajas de utilizar `git merge --no-ff` en un proyecto en equipo? ¿Qué problemas podrían surgir al depender excesivamente de commits de fusión?

	Se consigue un mejor entendimiento de como se desarrolló la funcionalidad y por qué se hizo el merge, quizás para realizar el merge de `feature3` iba a necesitar algo de `feature2`.

3. **Crea múltiples commits en una rama.**

	Hacemos varios commits en la rama `feature4`

	![](Attachments/Pasted%20image%2020250424000640.png)

	Nos cambiamos a rama `main` y hacemos `git merge --squash feature4`, esto agrupa los cambios que aparecieron en la rama `feature4` y los deja en el `staging area`. Hacemos commit de los cambios y tenemos una nueva gráfica

	![](Attachments/Pasted%20image%2020250424002429.png)

	**Pregunta:** ¿Cuándo es recomendable utilizar una fusión squash? ¿Qué ventajas ofrece para proyectos grandes en comparación con fusiones estándar?

	Es recomendable cuando se prioriza un historial simple. En proyectos grandes se suele utilizar squash si están utilizando metodologías ágiles, CI/CD, de esta manera con squash pueden resumir pequeños cambios en uno solo.

##  Resolver conflictos con una fusión fast-forward

- Inicializamos el repositorio, creamos un archivo `index.html` y realizamos un commit en la rama main

	![](Attachments/Pasted%20image%2020250424014408.png)

- Creamos y cambiamos a una rama `feature-update`, luego realizamos cambios en el mismo archivo y hacemos commit en esta rama

	![](Attachments/Pasted%20image%2020250424014547.png)

- Volvemos a la rama `main`, realizamos cambios en el mismo archivo y hacemos commit

	![](Attachments/Pasted%20image%2020250424014827.png)

- Luego de las dos ediciones en distintas ramas tenemos este gráfico

	![](Attachments/Pasted%20image%2020250424015017.png)

- Cuando intentamos hacer un merge desde la rama `main` obtenemos un conflicto

	![](Attachments/Pasted%20image%2020250424015124.png)

- Si entramos al archivo problemático veremos 3 líneas que indican los cambios de mi rama actual y los cambios de la rama a mezclar, editamos el archivo con tal de mantener ambos cambios de las ramas

	![](Attachments/Pasted%20image%2020250424015222.png)

	![](Attachments/Pasted%20image%2020250424020045.png)
	
-  Hacemos commit de los cambios y se completa la fusión

	![](Attachments/Pasted%20image%2020250424020248.png)

	**Preguntas:**
	
	- ¿Qué pasos adicionales tuviste que tomar para resolver el conflicto?

		- Al momento de borrar las líneas que indican conflicto, tuve que reordenar las líneas de código para que tengan sentido.
		- Luego de guardar el archivo este se queda en el `working tree`, así que debemos añadirlo al `staging area` y luego recién hacer el commit.
	
	- ¿Qué estrategias podrías emplear para evitar conflictos en futuros desarrollos colaborativos?

		No editar los mismos archivos en diferentes ramas o al menos no las mismas líneas.

## Ejercicio: Comparar los historiales con git log después de diferentes fusiones

### 1. Crea un nuevo repositorio y realiza varios commits en dos ramas:

![](Attachments/Pasted%20image%2020250424021707.png)

![](Attachments/Pasted%20image%2020250424021724.png)

Antes de realizar cualquier merge, este es el grafico del historial

![](Attachments/Pasted%20image%2020250424021925.png)

### 2. Fusiona feature-1 usando fast-forward:

Cambiamos a la rama main y ejecutamos `git merge feature-1 --ff` y lo que sucede es que el puntero `main` avanza hasta donde está el puntero `feature-1`, ya que estas ramas no divergen entonces ocurre el merge fast-forward

![](Attachments/Pasted%20image%2020250424022034.png)

### 3. Fusiona feature-2 usando non-fast-forward:

Cuando intentamos hacer el merge con `feature-2` nos aparece un `merge conflict`

![](Attachments/Pasted%20image%2020250424022300.png)

![](Attachments/Pasted%20image%2020250424022456.png)

Solucionamos el conflicto

![](Attachments/Pasted%20image%2020250424022512.png)

Finalmente, el commit de merge se vería así

![](Attachments/Pasted%20image%2020250424022721.png)

### 4. Realiza una nueva rama feature-3 con múltiples commits y fusiónala con squash:

Escribimos múltiples commits en la nueva rama `feature-3`

![](Attachments/Pasted%20image%2020250424023136.png)

Cambiamos a `main` y hacemos un merge squash con `feature-3`, esto nos deja un único cambio en main con los 2 pasos para la característica, hacemos commit de ese cambio y terminamos el merge squash

![](Attachments/Pasted%20image%2020250424023226.png)

Finalmente, el gráfico del historial se ve así

![](Attachments/Pasted%20image%2020250424023504.png)

**Preguntas:**

- ¿Cómo se ve el historial en cada tipo de fusión?

	- Usando `git log --merges`, puedes ver los commits de **merge explícito**
	- Para ver los commits de un `merge --ff` no existe una forma exacta, ya que en realidada ahí no se crean nuevos commits, sólo se mueve el puntero `head`
	- Igualmente para los commits de `merge --squash`, no hay una forma concreta ya que el commit que resulta es un commit normal, no uno de tipo merge

	En el último caso podría ayudar si se usan mensajes de commit descriptivo, como "Squash ...". De esa manera haciendo `git log --grep="Squash"` se pueden encontrar.
	
- ¿Qué método prefieres en diferentes escenarios y por qué?

	- `--ff`:  Cuando no he realizado cambios en mi rama principal desde que empecé a trabajar en mi rama actual
	- `--no-ff`: Cuando es obvia la bifurcación del historial
	- `--squashed`: Cuando la funcionalidad en sí es más importante que los commits que se hicieron para desarrollarla

## Ejercicio: Usando fusiones automáticas y revertir fusiones

### 1. Inicializa un nuevo repositorio y realiza dos commits en main:

![](Attachments/Pasted%20image%2020250424035811.png)

### 2. Crea una nueva rama auto-merge y realiza otro commit en file.txt:

![](Attachments/Pasted%20image%2020250424035949.png)

### 3. Vuelve a main y realiza cambios no conflictivos en otra parte del archivo:

![](Attachments/Pasted%20image%2020250424041051.png)

### 4. Fusiona la rama automerge con main

![](Attachments/Pasted%20image%2020250424041212.png)

Así se ve el gráfico luego del merge

![](Attachments/Pasted%20image%2020250424041253.png)

### 5. Revertir la fusión: Si decides que la fusión fue un error, puedes revertirla:

![](Attachments/Pasted%20image%2020250424041843.png)

![](Attachments/Pasted%20image%2020250424041858.png)

`Revert` crea otro commit adelante, `-m 1` significa que me quedo con los cambios del primer padre del commit (`main`) y `HEAD` indica el commit que será revertido, como HEAD apunta al último commit entonces el revert se aplica a `e51968c`.

### 6. Verificar el historial

![](Attachments/Pasted%20image%2020250424041957.png)

**Preguntas:**

- ¿Cuándo usarías un comando como git revert para deshacer una fusión?

	- Si según las políticas de la empresa no se puede usar `git reset` para eliminar commits, entonces usaría `git revert` y así revertiría cambios pero sin perder el historial de commits
	- Si el commit que hice es demasiado grande, haría un `git revert` y luego `git add -p` para hacer varios commits
	- Si me doy cuenta que hay un bug que se introdujo en cierto commit, usaría `git revert` para recuperar los cambios anteriores
	
- ¿Qué tan útil es la función de fusión automática en Git?

	Bastante útil ya que si estoy seguro que en dos ramas no se han editado las mismas líneas, no hay por qué complicar las cosas pensando en la estrategia de mergeo, `git` ya se ocupa de eso usando `ort(Ostensibly Recursive's Twin`

## Ejercicio: Fusión remota en un repositorio colaborativo

### 1. Clona un repositorio desde github o crea uno nuevo

![](Attachments/Pasted%20image%2020250424044017.png)

### 2. Crea una nueva rama colaboracion y haz algunos cambios:

![](Attachments/Pasted%20image%2020250424044252.png)

### 3. Empuja los cambios a la rama remota:

![](Attachments/Pasted%20image%2020250424044331.png)

### 4. Simula una fusión desde la rama colaboracion en la rama main de otro colaborador. (Puedes usar la interfaz de GitHub para crear un Pull Request y realizar la fusión).

Me aparece un mensaje de que la rama `colaboracion` tiene commits que no tiene mi rama `main`, le doy click a `Compare & pull request`

![](Attachments/Pasted%20image%2020250424044435.png)

Se muestran los cambios que se hicieron en la nueva rama y quien lo hizo

![](Attachments/Pasted%20image%2020250424044618.png)

Abrimos un pull request y escribimos una breve descripción del cambio (o funcionalidad)

![](Attachments/Pasted%20image%2020250424045109.png)

Evalua si hoy conflictos y como no los hay dice que puede realizar un **merge automático**

![](Attachments/Pasted%20image%2020250424045329.png)

Actuo como si fuera el revisor y escribo un comentario sobre el código si fuera necesario

![](Attachments/Pasted%20image%2020250424045426.png)

**Preguntas:**

- ¿Cómo cambia la estrategia de fusión cuando colaboras con otras personas en un repositorio remoto?

	Normalmente la rama `main` está protegida así que si quiero integrar la funcionalidad en la que he estado trabajando debo hacer un `pull request`, esperar que mis compañeros revisen mi código y le den el visto bueno para que mi rama aparezca en el remoto.
	
- ¿Qué problemas comunes pueden surgir al integrar ramas remotas?

	- Que se editen las mismas líneas de código en distintas ramas
	- Que alguien haga una operación forzada como `git push --force` porque quiere utilizar `git amend`

## Ejercicio final: flujo de trabajo completo

### 1. Crea un proyecto con tres ramas: main, feature1, y feature2.

![](Attachments/Pasted%20image%2020250424050403.png)

### 2. Realiza varios cambios en feature1 y feature2 y simula colaboraciones paralelas.

![](Attachments/Pasted%20image%2020250424050912.png)

### 3. Realiza fusiones utilizando diferentes métodos:

- Fusiona feature1 con main utilizando `git merge --ff`.

	![](Attachments/Pasted%20image%2020250424051051.png)

- Fusiona feature2 con main utilizando `git merge --no-ff`.

	![](Attachments/Pasted%20image%2020250424051143.png)

- Haz una rama adicional llamada feature3 y aplasta sus commits usando `git merge --squash`

	Se agregan 3 commits en la rama `feature3`
	
	![](Attachments/Pasted%20image%2020250424055834.png)

	Realizamos `git merge --squash feature3`
	
	![](Attachments/Pasted%20image%2020250424060022.png)

	Como `--squash` no crea realmente un commit de merge, entonces tenemos que hacer el commit nosotros
	
	![](Attachments/Pasted%20image%2020250424060048.png)

	Analiza el historial de commits:

	- Revisa el historial para entender cómo los diferentes métodos de fusión afectan el árbol de commits.

		- `--ff`: Mantiene la linealidad
		- `--no-ff`: Genera una conexión entre dos ramas, lo que crea algo de ruido en el gráfico
		- `--squash`: Minimiza la cantidad de commits en una rama, pero no elimina automáticamente la rama a la que se hizo squash, por lo que deja una rama sin conectar

	- Compara los resultados y discute con tus compañeros de equipo cuál sería la mejor estrategia de fusión para proyectos más grandes.

		No existe una mejor estrategia, hay un caso de uso para cada estrategia de fusión:
		- `--ff`: Puede utilizarse luego de un `git rebase` siempre y cuando se esté seguro de que no se han hecho commits en la rama `main`
		- `--no-ff`: Se debería usar para realizar los merge de funcionalidades luego de un `pull request` de esta manera se puede revisar los cambios para dicha funcionalidad, cuando y cómo empezó la rama
		- `--squash`: Este depende del flujo de trabajo del equipo y si es importante identificar a los autores de commits (ya que el autor del commit de squash puede ser cualquiera que tenga acceso a escribir en `main`), de no ser así, es muy útil al momento de integrar DevOps.


