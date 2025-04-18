# Actividad: Rebase, Cherry-Pick y CI/CD en un entorno ágil

## Parte 1: git rebase para mantener un historial lineal

2. Escenario de ejemplo

	![](Attachments/Pasted%20image%2020250416004336.png)
	
	Luego del rebase se crea un nuevo commit, no se mantiene el hash
	
	![](Attachments/Pasted%20image%2020250416005023.png)
	
3. Revisión

	![](Attachments/Pasted%20image%2020250416013424.png)
	
4. Momento de fusionar y completar el proceso de rebase

	![](Attachments/Pasted%20image%2020250416013456.png)
	
## Parte 2: git cherry-pick para la integración selectiva de commit

2. Escenario de ejemplo:

	![](Attachments/Pasted%20image%2020250416022122.png)
	
	**Pregunta:** Muestra un diagrama de como se ven las ramas en este paso.
	
	![](Attachments/Pasted%20image%2020250416023907.png)
	
3. **Tarea**: Haz cherry-pick de un commit de add-base-documents a main:

	![](Attachments/Pasted%20image%2020250416024308.png)
	
4. Revisión:

	![](Attachments/Pasted%20image%2020250416024443.png)
	
### Preguntas de discusión

1. ¿Por qué se considera que rebase es más útil para mantener un historial de proyecto lineal en comparación con merge?  

	Porque si estando en `rama1` se realiza la operación `git merge rama2` se realizó con No Fast Forward, entonces se crea un commit en `rama1` y se forma una conexión entre la `rama2` y este nuevo commit. Cuando existen muchas ramas y muchas conexiones en un flujo de trabajo es complicado poder leer los logs.
	
2. ¿Qué problemas potenciales podrían surgir si haces rebase en una rama compartida con otros miembros del equipo?  

	Si estoy en `rama2` y hago `git rebase` , se crean nuevos commits con los cambios que existian en `rama2` pero por delante en la `rama1` . Esto significa que si alguien estaba trabajando con los commits de `rama2` antes del rebase, terminarán fuera de las ramas establecidas.
	
3. ¿En qué se diferencia cherry-pick de merge, y en qué situaciones preferirías uno sobre el otro?  

	`cherry-pick` sólo trae los cambios de los commits individualmente, mientras que `merge` trae los cambios de toda la rama, `cherry-pick` es más conveniente cuando no quiero traer muchos cambios y prefiero probar sólo algunas funcionalidades.
	
4. ¿Por qué es importante evitar hacer rebase en ramas públicas?

	Porque se modifica el historial de las ramas.

## **Ejercicios teóricos**

1. **Diferencias entre git merge y git rebase**  
   **Pregunta**: Explica la diferencia entre git merge y git rebase y describe en qué escenarios sería más adecuado utilizar cada uno en un equipo de desarrollo ágil que sigue las prácticas de Scrum.
   
	- Diferencias: Lo que los diferencia es que `git merge` trae todos los cambios de una rama y muy probablemente (No Fast Forward) creará otro commit junto con los cambios mezclados, mientras que `git rebase` cambia la base de la rama, creando nuevos commits por delante de la otra rama. 
	- En un equipo de desarrollo ágil:
		- Usaría `git merge` dentro de una rama colaborativa
		- Usaría `git rebase` cuando ambas ramas sólo las use yo
2. **Relación entre git rebase y DevOps**  
   **Pregunta**: ¿Cómo crees que el uso de git rebase ayuda a mejorar las prácticas de DevOps, especialmente en la implementación continua (CI/CD)? Discute los beneficios de mantener un historial lineal en el contexto de una entrega continua de código y la automatización de pipelines.
   
   Si se hace `git rebase` a una rama como `main`, una herramienta de CI puede revisar todos esos cambios uno por uno en vez de sólo revisar commits de merge que son más confusos.

3. **Impacto del git cherry-pick en un equipo Scrum**  
   **Pregunta**: Un equipo Scrum ha finalizado un sprint, pero durante la integración final a la rama principal (main) descubren que solo algunos commits específicos de la rama de una funcionalidad deben aplicarse a producción. ¿Cómo podría ayudar git cherry-pick en este caso? Explica los beneficios y posibles complicaciones.
   
   Se utiliza cherry-pick a esos commits y así se tiene un nuevo commit en la rama `main` con esas funcionalidades, una complicación puede ser que ahora debe tenerse un seguimiento de los otros commits faltantes, para futuros merge.
## Ejercicios prácticos

1. **Simulación de un flujo de trabajo Scrum con git rebase y git merge**

	![](Attachments/Pasted%20image%2020250416053225.png)

	Se realiza un `git rebase main` , para luego hacer una fusión fast-forward con main.

	![](Attachments/Pasted%20image%2020250416061216.png)

	**Preguntas**

	- ¿Qué sucede con el historial de commits después del rebase?

		El historial se altera, en vez de `49a2f2b` vemos `c7afcdb`

		![](Attachments/Pasted%20image%2020250416061301.png)

	- ¿En qué situación aplicarías una fusión fast-forward en un proyecto ágil?

		Si estoy trabajando en una feature yo solo y reviso el historial de commits de main pero nadie ha realizado commits desde que me puse a trabajar, en ese caso puedo hacer realizar un `git rebase` y en main `git merge ` fast forward.

2. **Cherry-pick para integración selectiva en un pipeline CI/CD**

	![](Attachments/Pasted%20image%2020250417053040.png)

	**Preguntas**

	- ¿Cómo utilizarías cherry-pick en un pipeline de CI/CD para mover solo ciertos cambios listos a producción?

		Cuando quiera llevar cambios específicos a producción sin tener que hacer un deploy completo de la rama de desarrollo

	- ¿Qué ventajas ofrece cherry-pick en un flujo de trabajo de DevOps?

		Facilta que los despliegues puedan ser **controlados** y **rapidos**, que es justo la idea de DevOps

## **Git, Scrum y Sprints**

### **Fase 1: Planificación del sprint (sprint planning)**

#### **Ejercicio 1: Crear ramas de funcionalidades (feature branches)**

![](Attachments/Pasted%20image%2020250417063504.png)

#### **Pregunta:** ¿Por qué es importante trabajar en ramas de funcionalidades separadas durante un sprint?

Porque permite que cada desarrollador trabaje por separado en una funcionalidad, sin interrumpir el trabajo de otro.

### **Fase 2: Desarrollo del sprint (sprint execution)**

#### **Ejercicio 2: Integración continua con git rebase**

![](Attachments/Pasted%20image%2020250417080529.png)

#### **Pregunta:** ¿Qué ventajas proporciona el rebase durante el desarrollo de un sprint en términos de integración continua?

Se reducen conflictos ya que la rama se mantiene sincronizada con el proyecto base, se entiendo mejor la evolución del código y permite debugear con `git bisect`

### **Fase 3: Revisión del sprint (sprint review)**

#### **Ejercicio 3: Integración selectiva con git cherry-pick**

![](Attachments/Pasted%20image%2020250417082502.png)

#### **Pregunta:** ¿Cómo ayuda `git cherry-pick` a mostrar avances de forma selectiva en un sprint review?

No es necesario realizar un merge, entonces pueden verse poco a poco los commits realizados en la rama de la feature para mostrar el avance.

### **Fase 4: Retrospectiva del sprint (sprint retrospective)**

#### **Ejercicio 4: Revisión de conflictos y resolución**

![](Attachments/Pasted%20image%2020250417083349.png)

Escogemos cual cambio aceptar

![](Attachments/Pasted%20image%2020250417083429.png)

![](Attachments/Pasted%20image%2020250417083504.png)
![](Attachments/Pasted%20image%2020250417083823.png)

#### **Pregunta**: ¿Cómo manejas los conflictos de fusión al final de un sprint? ¿Cómo puede el equipo mejorar la comunicación para evitar conflictos grandes?

Los rebases frecuentes pueden ayudar a que aparezcan tantos conflictos, además de la distribución de responsabilidades para que el desarrollo de una feature sea independiente de los otros.

### **Fase 5: Fase de desarrollo, automatización de integración continua (CI) con git rebase**

#### **Ejercicio 5: Automatización de rebase con hooks de Git**

![](Attachments/Pasted%20image%2020250417132003.png)

![](Attachments/Pasted%20image%2020250417131941.png)

#### **Pregunta**: ¿Qué ventajas y desventajas observas al automatizar el rebase en un entorno de CI/CD?

- Ventajas: Permite ejecutar las pruebas en un entorno lo más actualizado posible.
- Desventajas: Manejar la solución automática de conflictos

## Navegando conflictos y versionando en un entorno DevOps

### Ejemplo:

1. **Inicialización del proyecto y creación de ramas**

	![](Attachments/Pasted%20image%2020250418113622.png)

2. **Fusión y resolución de conflictos**

	![](Attachments/Pasted%20image%2020250418115149.png)

3. Simulación de fusiones y uso de git diff

	![](Attachments/Pasted%20image%2020250418121217.png)

4. **Uso de git mergetool**

	![](Attachments/Pasted%20image%2020250418123719.png)
	
	![](Attachments/Pasted%20image%2020250418122442.png)

	![](Attachments/Pasted%20image%2020250418123826.png)

	![](Attachments/Pasted%20image%2020250418123936.png)

	![](Attachments/Pasted%20image%2020250418124054.png)

5. **Uso de git revert y git reset**

	![](Attachments/Pasted%20image%2020250418133905.png)

6. **Versionado semántico y etiquetado**

	![](Attachments/Pasted%20image%2020250418134515.png)

7. **Aplicación de git bisect para depuración**

	![](Attachments/Pasted%20image%2020250418135528.png)

	![](Attachments/Pasted%20image%2020250418140306.png)

8. **Documentación y reflexión**

	- `git checkout --theirs` y `git checkout --ours` sirven cuando conocemos los cambios de nuestros compañeros y no necesitamos utilizar un mergetool para solucionarlos.
	- `git merge --no-commit --no-ff feature-branch` sirve para simular un merge y revisar los cambios facilmente con `git diff --cached`, en caso de que decidamos que no haremos el merge usamos `git merge --abort`.
	- `git mergetool` nos permite usar una herramienta específica para manejar los conflictos de merge.
	- `git revert` permite deshacer cambios realizados en un commit, creando un nuevo commit que niega al commit señalado.
	- `git tag` sirve para marcar hitos en nuestro código.
	- `git bisect` sirve para encontrar donde ocurrió un error concreto.

## Preguntas
