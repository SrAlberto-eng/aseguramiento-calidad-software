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
| `08_Configuracion` | El registro del estado de la configuración y los manifiestos de las líneas base |
| `09_Problemas_acciones_y_mejora` | El análisis de causa raíz, con la matriz defecto-fuente |

La carpeta `07_Pruebas` se crea en la Clase 15 con el plan de pruebas. Dentro de cada carpeta, `obsoletas` guarda las versiones superadas de los elementos de configuración.

## Nombres de archivo

Los archivos se nombran con la forma `<actividad>_<Titulo>_v<X.Y>_<AAAA-MM-DD>.<ext>`. La actividad es el número de la práctica del curso, así que los archivos quedan en el orden del semestre. El título va sin acentos ni espacios. La versión solo aparece en los documentos que tienen versión propia. La fecha es la de «Lugar y fecha» del documento.

## Elementos de configuración y registros

Un elemento de configuración es un documento que se entrega, cambia, usan varias personas y cuyo error es costoso. En este repositorio son cuatro:

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

## Lo que no se sube

En el repositorio no hay contraseñas, claves de acceso ni datos personales de alumnos. Los documentos de 8=1 que no son del equipo, como la especificación de requisitos o el código, no se suben. Se registran por nombre, versión y ubicación en el registro del estado.
