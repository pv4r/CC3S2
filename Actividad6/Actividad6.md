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

