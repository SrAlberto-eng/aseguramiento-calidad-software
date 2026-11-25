---
tags: [aseguramiento, 8igual1, defectos, registro]
actualizado: 2026-11-24
responsable: Jorge Alberto Méndez Oseguera
origen: "Meta 3.4.1, análisis de causa raíz del 5 de noviembre de 2026"
---

# Matriz defecto-fuente de 8=1

Esta matriz es el registro de problemas del plan de aseguramiento. Liga cada defecto de 8=1 con la actividad que lo detectó, el artefacto donde nació, su severidad y su causa raíz. Empezó como la Tabla 1 del reporte de la Meta 3.4.1. Se pasó a este archivo para que cada cambio de estado quede en el historial de Git con su fecha, su autor y el issue que lo pidió.

Es un registro, no un elemento de configuración. No entra a ninguna línea base. Se actualiza en cada revisión semanal, siempre por una solicitud de integración.

## Cómo leerla

La severidad usa los criterios del análisis de causa raíz. Un defecto crítico puede dar un crédito de más o de menos. Uno mayor impide una tarea principal, hace repetir una acción que registra datos o expone información del sistema. Los demás son menores.

La columna de seguimiento dice en qué estado está cada defecto y qué falta para cerrarlo. Un defecto se cierra solo cuando se verifica su corrección.

En el glosario de la ERS, sesión y actividad son sinónimos. Por eso el defecto 1 habla de alumno y sesión, y la solicitud SC-03 de alumno y actividad. Las dos frases piden la misma restricción.

## Defectos del producto

| Núm. | Defecto | Detectado con | Origen y tipo | Severidad | Causa raíz | Seguimiento |
|---|---|---|---|---|---|---|
| 1 | La tabla de asistencias no tiene una restricción única sobre el alumno y la sesión. Una asistencia se puede registrar dos veces. | Revisión por escenarios | Diseño, omisión | Crítica | Reglas sin especificación verificable | Abierta. Los hallazgos 1 y 5 de la revisión técnica confirman que la ERS tampoco lo impide. |
| 2 | El requisito de topes no dice el valor, el periodo ni qué pasa con lo que lo rebasa. | Revisión de cobertura | Requisitos, incompleto | Crítica | Reglas sin especificación verificable | Abierta |
| 3 | El recordatorio de un evento próximo no tiene entidad ni pantalla. | Revisión de cobertura | Diseño, omisión | Menor | Requisitos sin versión ni prioridad | Abierta |
| 4 | La exportación del historial de créditos no tiene pantalla ni función. | Revisión de cobertura | Diseño, omisión | Menor | Requisitos sin versión ni prioridad | Abierta |
| 5 | El botón para registrar asistencia es un ícono QR sin texto. | Prueba con alumnos | Diseño, interacción | Mayor | Prototipo sin prueba con alumnos | Abierta |
| 6 | La confirmación de asistencia desaparece en un segundo. | Prueba con alumnos | Diseño, interacción | Mayor | Prototipo sin prueba con alumnos | Abierta |
| 7 | La lista de eventos no tiene filtro por facultad. | Prueba con alumnos | Diseño, interacción | Mayor | Prototipo sin prueba con alumnos | Abierta |
| 8 | La pantalla de inicio no tiene acceso directo a los eventos. | Prueba con alumnos | Diseño, interacción | Menor | Prototipo sin prueba con alumnos | Abierta |
| 9 | Progreso y Créditos son dos secciones con información parecida. | Prueba con alumnos | Diseño, interacción | Menor | Prototipo sin prueba con alumnos | Abierta |
| 10 | Un mensaje de validación siempre dice que falta la carrera, sin importar el campo que falte. | Análisis estático | Código, lógica | Menor | Backend sin revisión automática | Abierta |
| 11 | El servidor revela en una cabecera el framework que usa. | Análisis estático | Código, configuración | Mayor | Backend sin revisión automática | Abierta |
| 12 | Hay constantes sin uso y un comentario pendiente. | Análisis estático | Código, mantenibilidad | Menor | Backend sin revisión automática | Abierta |

Los defectos 1 a 9 salen de la evaluación de la calidad de la Clase 10. Los defectos 10 a 12 salen del análisis estático del Lab 2.4.1.

## Hallazgos de la revisión técnica de la ERS

La revisión técnica del 24 de noviembre de 2026 encontró 12 hallazgos en los requisitos del registro de asistencia, del RF-34 al RF-43. La auditoría de esa revisión pidió registrarlos aquí como acción correctiva. Se usan los mismos números del reporte de la revisión, donde está el texto completo de cada uno.

| Núm. | Requisitos | Hallazgo | Severidad | Defecto relacionado | Seguimiento |
|---|---|---|---|---|---|
| 1 | RF-34, RF-37, RF-39 | Un mismo alumno puede registrar dos códigos distintos de la misma actividad y sumar dos asistencias. | Crítica | Defecto 1 | Abierto. Falta entregarlo al equipo de desarrollo. |
| 2 | RF-36, RF-37 | En una actividad virtual se envía un solo código a toda la lista, así que deja de ser individual. | Crítica | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 3 | RF-41, RF-41.1 | Los dos requisitos tienen el mismo disparador, la carga de una lista en CSV, y respuestas opuestas. | Crítica | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 4 | RF-41, RF-41.2 | Las asistencias cargadas por CSV no pasan por el plazo, el traslape ni el alumno inhabilitado. | Crítica | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 5 | RF-42 | Un alumno que registró su código y además aparece en la lista CSV tendría dos asistencias. | Crítica | Defecto 1 | Abierto. Falta entregarlo al equipo de desarrollo. |
| 6 | RF-40 | No queda definido si un traslape bloquea el registro o solo se señala. | Mayor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 7 | RF-34, RF-36 | Ningún requisito dice cómo registra su código quien asiste a una actividad híbrida. | Mayor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 8 | RF-38 | El plazo de 15 días no considera el cierre del periodo. | Mayor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 9 | RF-43 | No se define qué pasa al llegar a ocho asistencias ni cómo se cuenta un segundo crédito. | Mayor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 10 | RF-41 | No se define qué es una matrícula válida ni cómo se identifica la actividad en cada renglón del CSV. | Mayor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 11 | RF-35 | El requisito dice «asistente» donde los demás dicen «alumno». | Menor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |
| 12 | RF-34 | No dice que el código pasa a estado «registrado». | Menor | Ninguno | Abierto. Falta entregarlo al equipo de desarrollo. |

La entrega al equipo de desarrollo es la otra mitad de la acción correctiva y se hace en la revisión semanal del 27 de noviembre de 2026.
