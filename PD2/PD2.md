# Actividad: Exploración y administración avanzada de Git mediante un script interactivo

El repositorio de prueba que se utilizó para esta actividad es este [Repositorio PD2](https://github.com/pv4r/PD2-CC3S2).

## 1. Inicio del script

![](Attachments/Pasted%20image%2020250422232031.png)

## 2. Agregar un submódulo

![](Attachments/Pasted%20image%2020250422233515.png)

## 3. Opción: Gestión de ramas (Opción 4)

![](Attachments/Pasted%20image%2020250422234858.png)

![](Attachments/Pasted%20image%2020250422235541.png)

## 5. Opción: Gestión de hooks (Opción 10)

![](Attachments/Pasted%20image%2020250423000031.png)

![](Attachments/Pasted%20image%2020250423000050.png)

## Preguntas

- ¿Qué diferencias observas en el historial del repositorio después de restaurar un commit mediante reflog?

	El comando `git reflog` me muestra un registro de todos los cambios de posición de `HEAD`, entonces, si yo borrara un commit (usando `reset` por ejemplo) aún podría acceder a él gracias a `git reflog`. Aunque puedo recuperar los cambios del commit, **no vuelve automáticamente a formar parte de la rama actual**, sólo se ha realizado un movimiento de `HEAD`.

- ¿Cuáles son las ventajas y desventajas de utilizar submódulos en comparación con subtrees?

	Cada uno se usa dependiendo del subproyecto que se está realizando, la diferencia más clara entre estos dós es el espacio, un subtree ocupa mucho más espacio que un submódulo ya que todo su historial se añade al repo inicial.

	| Situación                | Submódulo |      Subtree         |
	|----------------------------------------------------------|-----------|-----------|
	| El subproyecto tiene un desarrollo independiente        | Sí    |  No |
	| Simplicidad para usuarios/colaboradores        | No     |  Sí             |
	| Facil manejo de CI/CD                                           |  No |  Sí    |
	| Historial comprensible y modular          | Sí         | No              |
	| Para proyectos pequeños           | No        |  Sí         |

- ¿Cómo impacta la creación y gestión de hooks en el flujo de trabajo y la calidad del código?

	 - Para el flujo de trabajo:
		 - Automatización de tareas repetitivas
		 - Consistencia: Todos siguen las mismas reglas y validaciones, por ejemplo si usan `pre-commit` o `pre-push` o `commit-msg`
	- Para la calidad del código:
		- Mismo estilo de código
		- Prevención de bugs gracias a los tests de `pre-commit`

- ¿De qué manera el uso de git bisect puede acelerar la localización de un error introducido recientemente?

	Implementa una **búsqueda binaria** en mi historial de commits para encontrar **cual fue el commit que produjo el bug**. Utiliza un marcado de commits buenos y malos para realizar la busqueda.

- ¿Qué desafíos podrías enfrentar al administrar ramas y stashes en un proyecto con múltiples colaboradores?

	- No se establecen convenciones para nombrar las ramas
	- Conflictos al realizar merge
	- Ramas viejas que ya cumplieron su función y no se borraron 
	- Si necesito urgentemente cambiar de rama entonces el uso de `git stash` es útil para guardar mi progreso sin hacer commit
	- Es necesario agregar un mensaje al stash para reconocerlo luego

## Ejercicios

### 1. Extiende el menú de gestión de ramas para incluir la funcionalidad de renombrar ramas.

#### Modificacion

![](Attachments/Pasted%20image%2020250423012056.png)

#### Salida

![](Attachments/Pasted%20image%2020250423012225.png)

### 2. Amplia la sección de "Gestión de git diff" para permitir ver las diferencias de un archivo específico entre dos commits o ramas.

![](Attachments/Pasted%20image%2020250423020425.png)

![](Attachments/Pasted%20image%2020250423020842.png)

![](Attachments/Pasted%20image%2020250423020901.png)

### 3. Crea una función que permita instalar automáticamente un hook que, por ejemplo, verifique si se han agregado comentarios de documentación en cada commit.

#### Creacion del script

![](Attachments/Pasted%20image%2020250423021514.png)

#### Integración de la función en el submenú de Gestión de Hooks

![](Attachments/Pasted%20image%2020250423025044.png)

#### Salida

![](Attachments/Pasted%20image%2020250423025932.png)

![](Attachments/Pasted%20image%2020250423030049.png)

### 4. Implementa una opción en el script que realice un merge automatizado de una rama determinada en la rama actual, incluyendo la resolución automática de conflictos (siempre que sea posible).

#### Integracion de la funcion

![](Attachments/Pasted%20image%2020250423032406.png)

![](Attachments/Pasted%20image%2020250423032426.png)
#### Salida

![](Attachments/Pasted%20image%2020250423032112.png)

### 5. Implementa una opción en el script que genere un reporte con información relevante del repositorio (estado, ramas, últimos commits, stashes, etc.) y lo guarde en un archivo.

#### Integración de la función

![](Attachments/Pasted%20image%2020250423033602.png)

#### Salida

![](Attachments/Pasted%20image%2020250423033404.png)

![](Attachments/Pasted%20image%2020250423033433.png)

![](Attachments/Pasted%20image%2020250423033510.png)
