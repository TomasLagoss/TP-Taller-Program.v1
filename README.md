# GameSec Monitor

Trabajo práctico de Taller de Programación

## Integrantes

Lencina, Jose
Lagos, Tomas
Blanco, Uriel

## Descripción

Programa de consola que analiza sesiones de videojuegos.
Calcula estadísticas generales y por servidor, clasifica
incidentes de seguridad y genera un reporte de texto.

## Requisitos

- Python 3.10 o superior.
- No requiere instalar librerías externas.

## Archivos

- carga.py: lectura y validación del CSV.
- procesamiento.py: estadísticas y clasificación de incidentes.
- main.py: menú y exportación del reporte.
- gamesec_logs.csv: datos proporcionados por la cátedra.
- reporte_gamesec.txt: reporte generado por el programa.

## Ejecución

1. Colocar los archivos del proyecto en una misma carpeta.
2. Abrir una terminal en esa carpeta.
3. Ejecutar: python main.py
4. Elegir la opción 1 para cargar los datos.
5. Usar las opciones 2, 3 y 4 para consultar los análisis.
6. Elegir la opción 5 para generar el reporte.
7. Elegir la opción 6 para salir.

Al exportar, el programa solicita la fecha y tres conclusiones
redactadas por el grupo. Si ya existe un reporte, lo reemplaza.