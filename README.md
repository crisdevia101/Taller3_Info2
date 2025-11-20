TALLER 3 - INTRODUCCION A LA INFORMATICA MEDICA
- Cristian Camilo Devia Bohorquez

1. Breve descripcion del proyecto.

Este proyecto desarrolla una aplicacion en Python capaz de cargar archivos DICOM, extraer sus metadatos principales, analizarlos y organizarlos en un DataFrame,
ademas se exporta a un csv para observar mejor los metadatos.
Ademas, calcula la intensidad promedio de cada imagen y permite exportar los resultados. Su proposito es simular una parte del flujo de un sistema PACS, aplicando
estandares de informatica medica y herramienta como pydicom, numpy y pandas.


2. Explica brevemente por que DICOM y HL7 son cruciales para la interoperabilidad en salud
y en que se diferencian conceptualmente.

DICOM es el estandar usado para almacenar, transmitir y visualizar imagenes medicas junto con sus metadatos; permite que equipos y sistemas de diferentes fabricantes
sean compatible. HL7 es el estandar usado para el intercambio de informacion clnica y administrativa entre sistemas hospitalarios. DICOM se enfoca en imagenes medicas,
mientras que HL7 se enfoca en datos clinicos textuales. Ambos son esenciales porque permiten que los sistemas de salud puedan comunicarse correctamente y compartir
informacion sin importar la plataforma o fabricante.


3. Pregunte teorica: ¿Que relevancia clinica o de pre-procesamiento podria tener el analisis
de de la distribucion de intensidades en una imagen medica?

El analisis de la distribucion de intensidades en una imagen medica es relevante porque permite identificar variaciones en los tejidos, detectar posibles lesiones,
evaluar la calidad de la iamgen y servir como base para procesos de pre-procesamiento como normalizacion, segmentacion y filtrado. Tambien es util en diagnostico asistido
y en modelos de IA que requieren informacion cuantitativa sobre las imagenes.


4. Mencionar dificultades encontradas y la importancia de las herramientas de Python para el
analisis de datos medicos.

Dificultades:
- Algunos archivos DICOM estan anonimizados
- No todas las modalidades contienen pixel_array
- Diferentes versiones de DICOM pueden manejar nombres/tags diferentes
- Pueden haber errores al leer archivos no compatibles o corruptos

Python facilita el procesamiento clinico gracias a pydicom que hace la lectura de imagenes medicas, numpy que hace un analisis numerico eficiente y pandas que ayuda a
la estructuracion de datos. Esto permite proesar grandes cantidades de informacion de manera eficiente y reproducible.

