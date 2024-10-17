# RETO MODULO 2 
```markdown
# ETL de Harry Potter utilizando HP-API
Se desarrolló la implementación de un proceso ETL (Extracción, Transformación y Carga) que realizó una extracción combinada de datos desde una API y un archivo CSV. Como fuente principal, se utilizó la HP-API, una API que proporciona información sobre los personajes de la saga de Harry Potter. Los datos del código, apodo (nickname) y ascendencia (ancestry) se extrajeron de un archivo llamado characters.csv. Esta información se utilizó como complemento a los datos obtenidos de la API, que incluían el nombre, casa, patronus y varita (wand) de los personajes.

Para la orquestación de los flujos y tareas del proceso ETL, se utilizó Prefect, lo Sque permitió una gestión eficiente del proceso. Finalmente, los datos consolidados fueron almacenados en una base de datos para ser visualizados tanto en la terminal, junto con los logs, como a través de MySQL Workbench.

Nota: Cabe destacar que los campos vacíos en la tabla se deben a que cierta información en la API aparecía sin datos.
```
