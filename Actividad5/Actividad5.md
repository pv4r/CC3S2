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



