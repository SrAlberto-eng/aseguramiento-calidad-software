---
tags: [aseguramiento, sqap, configuracion, 8igual1]
actualizado: 2026-11-24
responsable: Jorge Alberto Méndez Oseguera
---

# Control del repositorio de aseguramiento de 8=1

Este repositorio guarda los documentos de aseguramiento de la calidad que el Equipo Alfa hizo sobre el proyecto 8=1 en la materia Aseguramiento de la Calidad del Software 40019. No es el repositorio del código de 8=1. La especificación de requisitos, el esquema, la aplicación y el backend viven con el equipo de desarrollo de 8=1 y aquí solo se registran por nombre, versión y ubicación.

El plan de administración de la configuración está en el componente 8 del SQAP. Este archivo resume cómo está ordenado el repositorio para que cualquiera lo pueda recorrer.

## Estructura

Cada carpeta lleva el número del componente del SQAP al que da sustento.

| Carpeta | Qué guarda |
|---|---|
| `00_SQAP` | El plan de aseguramiento vigente |
| `01_Proposito_y_alcance` | La ficha del proyecto y del cliente |
| `03_Organizacion_y_roles` | El Lab 2.4.1, con los roles y el costo de la mala calidad |
| `05_Riesgos` | La matriz de riesgos y el reporte de la Clase 4 |
| `06_Revisiones_evaluacion_y_auditorias` | El modelo de calidad, el plan y el informe de evaluación, la revisión técnica de la especificación y su auditoría |
| `07_Pruebas` | El plan de pruebas, con sus casos y su ejecución |
| `08_Configuracion` | El registro del estado de la configuración y los manifiestos de las líneas base |
| `09_Problemas_acciones_y_mejora` | El análisis de causa raíz, con la matriz defecto-fuente |

Dentro de cada carpeta, `obsoletas` guarda las versiones superadas de los elementos de configuración.

## Nombres de archivo

Los archivos se nombran con la forma `<actividad>_<Titulo>_v<X.Y>_<AAAA-MM-DD>.<ext>`. La actividad es el número de la práctica del curso, así que los archivos quedan en el orden del semestre. El título va sin acentos ni espacios. La versión solo aparece en los documentos que tienen versión propia. La fecha es la de «Lugar y fecha» del documento.

## Elementos de configuración y registros

Un elemento de configuración es un documento que se entrega, cambia, usan varias personas y cuyo error es costoso. En este repositorio son cinco:

- `EC-07` el plan de pruebas.
- `EC-08` el SQAP.
- `EC-09` la ficha del proyecto y del cliente.
- `EC-10` la matriz de riesgos.
- `EC-11` el plan de evaluación de la calidad del producto.

Un elemento solo cambia con una solicitud de cambio registrada en el registro del estado. Su versión anterior pasa a `obsoletas`.

Los demás documentos son registros. Cuentan lo que pasó en una fecha y no se versionan. Si se corrigen, se reemplazan y el historial de Git conserva lo anterior.

## Líneas base

Cada línea base es una etiqueta de Git con la forma `LB-SQAP-NN`. Una etiqueta publicada nunca se mueve ni se borra. Si una línea base resulta incorrecta, se crea la siguiente y se explica por qué.

Para comprobar que una línea base está completa:

```bash
git checkout LB-SQAP-01
sha256sum -c 08_Configuracion/LB-SQAP-01.sha256
```

La auditoría física completa, que además revisa el registro del estado, los archivos sin registrar, los commits directos en `main` y los marcadores de conflicto, se hace desde un clon nuevo con `python3 08_Configuracion/verificar_linea_base.py LB-SQAP-04`, cambiando la etiqueta.

## Control de versiones

El repositorio sigue GitHub Flow. La rama `main` siempre tiene la versión vigente de los documentos y nadie escribe directo en ella. Cada cambio se hace en una rama corta, entra por una solicitud de integración y se fusiona después de revisarse. El plan completo está en las secciones 8.8 a 8.11 del SQAP.

Cada cambio empieza con un issue que dice su origen, que puede ser una solicitud de cambio, una acción preventiva o una no conformidad. Después se siguen estas convenciones:

- La rama se llama `<tipo>/<issue>-<descripcion-corta>`, como `docs/2-matriz-defecto-fuente`. El tipo es `docs` para documentos, `fix` para corregir algo ya integrado y `chore` para mantenimiento del repositorio.
- El mensaje de commit tiene la forma `<tipo>(<documento>): <qué cambia> (#<issue>)`, en presente y en minúsculas, como `docs(matriz): registra los 12 hallazgos de la revisión técnica (#3)`. El cuerpo dice por qué cambia. Un commit hace un solo cambio lógico.
- La solicitud de integración se titula con lo que hace y lleva en su descripción `Closes #<issue>`. GitHub solo reconoce las palabras de cierre en inglés.
- Cada solicitud recibe al menos un comentario de revisión técnica antes de fusionarse, y desde la Clase 15 la aprobación de una cuenta distinta a la del autor.
- Se fusiona con merge commit, titulado `Integra #<solicitud>: <resumen> (cierra #<issue>)`. No se usa squash ni rebase, porque las etiquetas de línea base apuntan a commits que deben seguir en la historia de `main`.

Si al integrar aparece un conflicto, se trae `main` a la rama con `git merge`, sin rebase. Quien lo resuelve lee los dos issues, decide el resultado, quita los marcadores, verifica el archivo y explica la decisión en la solicitud. Los archivos `.docx` y `.xlsx` no se pueden combinar línea por línea, así que solo una rama abierta a la vez puede cambiar cada uno.

Para comprobar que nadie escribió directo en `main` desde que empezó el plan, este comando no debe mostrar nada:

```bash
git log --first-parent --no-merges e3ab430..main
```

## Lo que no se sube

En el repositorio no hay contraseñas, claves de acceso ni datos personales de alumnos. Los documentos de 8=1 que no son del equipo, como la especificación de requisitos o el código, no se suben. Se registran por nombre, versión y ubicación en el registro del estado.
