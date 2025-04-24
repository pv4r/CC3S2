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