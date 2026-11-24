# Aseguramiento de la calidad de 8=1

Repositorio del Equipo Alfa para la materia Aseguramiento de la Calidad del Software (40019, UABC, ciclo 2026-2). Guarda el plan de aseguramiento de la plataforma 8=1, con código SQAP-8IGUAL1, y los productos que lo sustentan. Es privado porque contiene información del cliente.

## Estructura del repositorio

Cada carpeta corresponde a una sección del SQAP y lleva su mismo número. Solo existen las carpetas de las secciones que tienen productos propios. Las secciones 2, 4, 7 y 10 se redactan dentro del SQAP o todavía no tienen producto.

- `00_SQAP` guarda el plan de aseguramiento.
- `01_Proposito_y_alcance` guarda la ficha del proyecto y del cliente.
- `03_Organizacion_y_roles` guarda el Lab 2.4.1 con costos, roles y análisis estático.
- `05_Riesgos` guarda la matriz de riesgos y el reporte de la Clase 4.
- `06_Revisiones_evaluacion_y_auditorias` guarda el modelo de calidad, el plan y el informe de evaluación, la revisión técnica RT-01 y la auditoría AU-01.
- `08_Configuracion_y_versiones` guarda el registro del estado de la configuración (REG-01) y el manifiesto SHA-256 de cada línea base.
- `09_Problemas_acciones_y_mejora` guarda el análisis de causa raíz con la matriz defecto-fuente.
- `99_Fuera_de_alcance` guarda productos de otros proyectos que se conservan como referencia del método.

Cada carpeta guarda sus versiones superadas en la subcarpeta `obsoletas`. La convención de nombres y la relación de cada archivo con su componente están en [INVENTARIO.md](INVENTARIO.md).

## Elementos de configuración y líneas base

La sección 8 del SQAP define qué artefactos son elementos de configuración, con código `CFG-<tipo>-<número>`, y cuáles son registros. La hoja Elementos de REG-01 tiene la versión vigente de cada elemento.

Las líneas base de aseguramiento son etiquetas anotadas de Git con el nombre `LB-ASEG-<nn>`. Una etiqueta no se mueve ni se borra. Si una línea base resulta incorrecta, se crea la siguiente y REG-01 explica por qué.

Ningún elemento que esté en una línea base cambia sin una solicitud `SC-<nn>` registrada en la hoja Solicitudes de REG-01. La solicitud pasa por solicitud, análisis de impacto, decisión, implementación, verificación y cierre.

## Cómo comprobar una línea base

Estos comandos reconstruyen una línea base y comprueban que cada archivo registrado está en la versión anotada. En Windows se ejecutan en Git Bash.

```bash
git fetch --tags
git checkout LB-ASEG-02
sha256sum -c 08_Configuracion_y_versiones/LB-ASEG-02.sha256
git checkout main
```

Cada línea debe terminar en `OK`. Después se compara la lista de archivos de la etiqueta con REG-01 e INVENTARIO.md para confirmar que no haya elementos sin registrar.

## Lo que no entra al repositorio

Los documentos del cliente y los artefactos de 8=1 se registran por identificador, versión y ubicación, sin copiar su contenido. Tampoco entran contraseñas, llaves de acceso, archivos de variables de entorno con valores reales ni datos personales de alumnos. El archivo `.gitignore` bloquea los casos más comunes.
