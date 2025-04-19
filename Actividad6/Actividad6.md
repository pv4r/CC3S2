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

1. **Ejercicio para git checkout --ours y git checkout --theirs**

	**Contexto**: En un sprint ágil, dos equipos están trabajando en diferentes ramas. Se produce un conflicto de fusión en un archivo de configuración crucial. El equipo A quiere mantener sus cambios mientras el equipo B solo quiere conservar los suyos. El proceso de entrega continua está detenido debido a este conflicto.

	**Pregunta**:  
	¿Cómo utilizarías los comandos `git checkout --ours` y `git checkout --theirs` para resolver este conflicto de manera rápida y eficiente? Explica cuándo preferirías usar cada uno de estos comandos y cómo impacta en la pipeline de CI/CD. ¿Cómo te asegurarías de que la resolución elegida no comprometa la calidad del código?

	- Si primero hice merge a al rama del equipo A y el conflicto ocurre cuando quiero hacer merge a la rama del equipo B, entonces ejecutaría `git checkout --ours configfile`  ya que B se quiere quedar con sus cambios. 
	- Uso `--ours` cuando mis cambios han sido validados y sé que son compatibles con la CI. Uso `--theirs` cuando los cambios del otro equipo son más recientes, corrigen un error o son necesarios para la CI.
	- Para asegurarme de no comprometer la calidad del código tengo que ejecutar las pruebas localmente y consultar con el otro equipo si es necesario.
2. **Ejercicio para git diff**

	**Contexto**: Durante una revisión de código en un entorno ágil, se observa que un pull request tiene una gran cantidad de cambios, muchos de los cuales no están relacionados con la funcionalidad principal. Estos cambios podrían generar conflictos con otras ramas en la pipeline de CI/CD.

	**Pregunta**:  
	Utilizando el comando `git diff`, ¿cómo compararías los cambios entre ramas para identificar diferencias específicas en archivos críticos? Explica cómo podrías utilizar `git diff feature-branch..main` para detectar posibles conflictos antes de realizar una fusión y cómo esto contribuye a mantener la estabilidad en un entorno ágil con CI/CD.

	- `git diff rama1..rama2 -- archivo-critico`
	- Usar `git diff` permite ver qué lineas cambian en archivos compartidos, de esta forma no tenemos que esperar a realizar un merge para resolver conflictos
	- Ya que los problemas se pueden solucionar antes del merge entonces no se rompen los builds
3. **Ejercicio para git merge --no-commit --no-ff**

	**Contexto**: En un proyecto ágil con CI/CD, tu equipo quiere simular una fusión entre una rama de desarrollo y la rama principal para ver cómo se comporta el código sin comprometerlo inmediatamente en el repositorio. Esto es útil para identificar posibles problemas antes de completar la fusión.

	**Pregunta**:  
	Describe cómo usarías el comando `git merge --no-commit --no-ff` para simular una fusión en tu rama local. ¿Qué ventajas tiene esta práctica en un flujo de trabajo ágil con CI/CD, y cómo ayuda a minimizar errores antes de hacer commits definitivos? ¿Cómo automatizarías este paso dentro de una pipeline CI/CD?

	-  `git checkout main` y `git merge --no-commit --no-ff feature-branch` simula la fusión de `feature-branch` en `main` pero no crea ningún commit, lo cual nos sirve para revisar los cambios antes de comprometer todo.
	- Previenes errores ya que usando `git diff --cached` puedes ver que cambios se aplicarán, y los cambios no rompen la CI/CD ya que no se ha actualizado el historial de commits.
	- Con un hook se puede automatizar, juntando los comandos :
		```yaml
			-name: Simulacion de merge
			  run: |
			    git fetch origin
			    git checkout main
			    git merge --no-commit --no-ff origin/feature-branch
		```
	
4. **Ejercicio para git mergetool**

	**Contexto**: Tu equipo de desarrollo utiliza herramientas gráficas para resolver conflictos de manera colaborativa. Algunos desarrolladores prefieren herramientas como vimdiff o Visual Studio Code. En medio de un sprint, varios archivos están en conflicto y los desarrolladores prefieren trabajar en un entorno visual para resolverlos.

	**Pregunta**:  
	Explica cómo configurarías y utilizarías `git mergetool` en tu equipo para integrar herramientas gráficas que faciliten la resolución de conflictos. ¿Qué impacto tiene el uso de `git mergetool` en un entorno de trabajo ágil con CI/CD, y cómo aseguras que todos los miembros del equipo mantengan consistencia en las resoluciones?

	- Usaría `git config --global nvimdiff`
	- Habrían menos errores en merge complejos, como hay menos conflictos entonces hay menos errores que puedan rompera la pipeline de CI o de tests
	- Para mantener la consistencia se necesita un archivo de configuración compartido `.gitconfig`

5. **Ejercicio para git reset**

	**Contexto**: En un proyecto ágil, un desarrollador ha hecho un commit que rompe la pipeline de CI/CD. Se debe revertir el commit, pero se necesita hacerlo de manera que se mantenga el código en el directorio de trabajo sin deshacer los cambios.

	**Pregunta**:  
	Explica las diferencias entre `git reset --soft`, `git reset --mixed` y `git reset --hard`. ¿En qué escenarios dentro de un flujo de trabajo ágil con CI/CD utilizarías cada uno? Describe un caso en el que usarías `git reset --mixed` para corregir un commit sin perder los cambios no commiteados y cómo afecta esto a la pipeline.

	- Diferencias entre tipos de `git reset`:
		- `--soft`: Mueve HEAD hasta un commit antes al especificado, y mantiene los cambios tanto en el `staging area` como en el `working directory`
		- `--mixed`: Mueve HEAD hasta un commit antes al especificado, borra lo que estaba en el `staging area` pero mantiene los cambios en el `working directory`
		- `--hard`: Mueve HEAD hasta un commit antes al especificado, borra lo que estaba en el `staging area` y en el `working directory`
	- Usos en un flujo ágil CI/CD:
		- `--soft`: Si escribí mal el mensaje del commit o si es necesario separar este commit en varios 
		- `--mixed`:Si un commit rompe el pipeline y quiero revertir ese commit para corregirlo
		- `--hard`: Si en mi rama hay varios commits innecesarios y quiero hacer como que nunca los hice

6. **Ejercicio para git revert**

	**Contexto**: En un entorno de CI/CD, tu equipo ha desplegado una característica a producción, pero se ha detectado un bug crítico. La rama principal debe revertirse para restaurar la estabilidad, pero no puedes modificar el historial de commits debido a las políticas del equipo.

	**Pregunta**:  
	Explica cómo utilizarías `git revert` para deshacer los cambios sin modificar el historial de commits. ¿Cómo te aseguras de que esta acción no afecte la pipeline de CI/CD y permita una rápida recuperación del sistema? Proporciona un ejemplo detallado de cómo revertirías varios commits consecutivos.

	- Uso `git revert --no-commit` para probar que los cambios solucionan el problema y no interfieren con el pipeline
	- Si quiero revertir varios commits consecutivos:
		- a1b2c3d (HEAD -> main) Commit actual
		- 8f9e7d1 Buggy commit (feature)
		- 3c4d5e6 Good commit
		- 7a8b9c0 Another commit

		Si quiero revertir de `7a8b9c0` a `8f9e7d1` hago: `git revert 7a8b9c0..8f9e7d1`

7. **Ejercicio para git stash**

	**Contexto**: En un entorno ágil, tu equipo está trabajando en una corrección de errores urgente mientras tienes cambios no guardados en tu directorio de trabajo que aún no están listos para ser committeados. Sin embargo, necesitas cambiar rápidamente a una rama de hotfix para trabajar en la corrección.

	**Pregunta**:  
	Explica cómo utilizarías `git stash` para guardar temporalmente tus cambios y volver a ellos después de haber terminado el hotfix. ¿Qué impacto tiene el uso de `git stash` en un flujo de trabajo ágil con CI/CD cuando trabajas en múltiples tareas? ¿Cómo podrías automatizar el proceso de _stashing_ dentro de una pipeline CI/CD?

	- Si estoy trabajando en una rama `feature` y no he guardado mis cambios, entonces no podré cambiar a otra hasta que haga commit o use `git stash` para guardar los cambios en una pila. De esta manera me permite cambiar a otra rama a trabajar en otra funcionalidad y luego volver como si no hubiera pasado nada.
	- Se podría automatizar usando un hook:
		```bash
		#!/bin/bash
		git stash push -m "Auto-stash before hotfix"
		git checkout hotfix/urgent-bug
		```

8. **Ejercicio para .gitignore**

	**Contexto**: Tu equipo de desarrollo ágil está trabajando en varios entornos locales con configuraciones diferentes (archivos de logs, configuraciones personales). Estos archivos no deberían ser parte del control de versiones para evitar confusiones en la pipeline de CI/CD.

	**Pregunta**:  
	Diseña un archivo `.gitignore` que excluya archivos innecesarios en un entorno ágil de desarrollo. Explica por qué es importante mantener este archivo actualizado en un equipo colaborativo que utiliza CI/CD y cómo afecta la calidad y limpieza del código compartido en el repositorio.
	
	```bash
	node_modules/
	venv/
	.env

	*.env
	*.local
	*.dev
	*.test

	*.log
	*.out
	*.err
	logs/
	debug.log
	npm-debug.log*

	dist/
	build/
	.tmp/
	.cache/
	coverage/
	*.pyc
	__pycache__/

	junit.xml
	coverage.xml
	.nyc_output/
	test-output/

	.vscode/
	.idea/
	*.sublime-workspace
	*.swp

	.DS_Store
	Thumbs.db

	*.bak
	*.old
	*.orig
	*.rej
	*.log.*
	*.pid

	secret.json
	credentials.json

	```

