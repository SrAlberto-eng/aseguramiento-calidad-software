---
tags: [aseguramiento, sqap, inventario, 8igual1, configuracion]
actualizado: 2026-11-23
linea_base: LB-ASEG-02
---

# Inventario de documentos del SQAP 8=1

Este repositorio, `aseguramiento-calidad-software`, guarda los productos de la materia Aseguramiento de la Calidad del Software (40019) que sustentan el plan de aseguramiento de 8=1 (SQAP-8IGUAL1). Cada producto vive en la carpeta del componente del plan al que da sustento. Las carpetas siguen la numeración de las secciones del SQAP, así que la Tabla 19 del plan y este inventario se pueden leer lado a lado.

La regla del equipo es que todo lo que sustenta el plan debe ser del proyecto 8=1, el de la ficha. Lo que se hizo sobre otro proyecto se guarda en `99_Fuera_de_alcance` como referencia del método.

Desde la Clase 13 el repositorio sigue el plan de administración de la configuración de la sección 8 del SQAP. Los elementos de configuración tienen código `CFG-<tipo>-<número>` y su versión vigente está en la hoja Elementos de `08_Configuracion_y_versiones/REG-01_Registro_del_estado_de_la_configuracion.xlsx`. Las líneas base son etiquetas de Git `LB-ASEG-<nn>`. Lo demás son registros, que se conservan sin versión.

## Convención de nombres

Los nombres siguen la forma `<código>_<Título>_<AAAA-MM-DD>[_<ETIQUETA>].<ext>`. El código es el número de la actividad del curso (2.1.1 a 4.1.1), lo que ordena los archivos en el orden del semestre. El título va sin acentos ni espacios, y si el documento tiene versión propia, la versión va en el título. La fecha es la de «Lugar y fecha» del documento.

La etiqueta solo aparece cuando el archivo es una excepción. Hay cinco.

- `POR-EJECUTAR` marca un documento preparado cuya actividad todavía no ocurre. Cuando ocurre, se cambia la fecha por la de la sesión y se quita la etiqueta.
- `SIMULADA` marca una actividad que se documentó como ejercicio simulado de escritorio, con autorización del docente. El documento lo declara en su primer punto.
- `RECIBIDO` marca un documento hecho por otro equipo.
- `OBSOLETA` marca una versión superada, que se guarda en la subcarpeta `obsoletas` de su componente.
- `OTRO-PROYECTO` marca un documento que no es de 8=1 y que vive en `99_Fuera_de_alcance`.

Cuando un elemento de configuración cambia, el cambio pasa por una solicitud `SC-<nn>` en REG-01. Al cerrarla, la versión anterior pasa a `obsoletas`, se actualizan este inventario y la Tabla 19 del SQAP y se crea la nueva línea base.

## Documentos por componente

| Carpeta | Archivo | Producto | Clase | Tipo | Estado |
|---|---|---|---|---|---|
| 00_SQAP | `4.1.1_SQAP_v1.1_2026-11-23.docx` y `.pdf` | Plan de aseguramiento, versión 1.1, con el componente 8 | 13 | CFG-ASG-01 | Vigente en LB-ASEG-02. Aprobación del cliente pendiente |
| 01_Proposito_y_alcance | `2.1.1_Ficha_del_proyecto_y_del_cliente_v1.2_2026-11-23.docx` y `.pdf` | Ficha del proyecto y del cliente, versión 1.2 | 1, 4 y 13 | CFG-ASG-02 | Vigente en LB-ASEG-02 |
| 03_Organizacion_y_roles | `2.4.1_Costos_roles_y_analisis_estatico_v1.1_2026-11-11.docx` y `.pdf` | Costos de la mala calidad, roles y análisis estático | 7 | Registro | Vigente. El costeo usa los 11 hallazgos de RT-01 |
| 05_Riesgos | `2.1.1_Matriz_de_riesgos_v1.1_2026-11-23.xlsx` | Matriz de riesgos de calidad, versión 1.1, con R7 | 4 y 13 | CFG-ASG-03 | Vigente en LB-ASEG-02 |
| 05_Riesgos | `2.1.1_Reporte_Clase4_riesgos_e_indicadores_2026-09-18.docx` y `.pdf` | Reporte de la Clase 4: matriz, estimación de 67 horas, indicadores I1 a I3 y trazabilidad | 4 | Registro | Vigente |
| 06_Revisiones_evaluacion_y_auditorias | `2.2.1_Revision_tecnica_RT-01_8igual1_2026-11-11_SIMULADA.docx` y `.pdf` | Revisión técnica RT-01 sobre 8=1, ejercicio simulado. Sus Tablas 1 a 3 son el plan de revisión técnica | 5 | Registro y CFG-ASG-05 | 11 hallazgos, 4 críticos, dictamen «No aceptado» |
| 06_Revisiones_evaluacion_y_auditorias | `2.3.1_Auditoria_AU-01_8igual1_2026-11-11_SIMULADA.docx` y `.pdf` | Auditoría AU-01 de RT-01, ejercicio simulado | 6 | Registro | NC-01 y NC-02 abiertas |
| 06_Revisiones_evaluacion_y_auditorias | `3.1.1_Modelo_de_calidad_ISO25010_2026-10-08.docx` | Modelo de calidad elegido | 8 | Registro | Vigente |
| 06_Revisiones_evaluacion_y_auditorias | `3.2.1_Plan_de_evaluacion_v1.1_2026-10-15.pdf` | Plan de evaluación, versión 1.1 | 9 | CFG-ASG-04 | Vigente en LB-ASEG-02 |
| 06_Revisiones_evaluacion_y_auditorias | `3.3.1_Informe_de_evaluacion_2026-10-22.pdf` | Informe de evaluación | 10 | Registro | Vigente |
| 08_Configuracion_y_versiones | `REG-01_Registro_del_estado_de_la_configuracion.xlsx` | Registro del estado: elementos, líneas base y solicitudes | 13 | Registro | Al día con LB-ASEG-02 |
| 08_Configuracion_y_versiones | `LB-ASEG-01.sha256` y `LB-ASEG-02.sha256` | Manifiestos de las líneas base | 13 | Registro | Se comprueban con `sha256sum -c` |
| 09_Problemas_acciones_y_mejora | `3.4.1_Analisis_de_causa_raiz_2026-11-05.pdf` y `.docx` | Matriz defecto-fuente y acciones AP-01 a AP-04 | 11 | Registro | Vigente. Faltan los hallazgos de RT-01 (NC-02) |

Las secciones 2, 4, 7 y 10 del SQAP no tienen carpeta. Las dos primeras se redactan dentro del plan, la 7 espera el plan de pruebas de la Clase 15 y la 10 se sustenta en el reporte de la Clase 4.

## Líneas base

| Etiqueta | Fecha | Contenido | Origen |
|---|---|---|---|
| `LB-ASEG-01` | 2026-11-23 | SQAP 1.0, ficha 1.1, matriz 1.0, plan de evaluación 1.1 y plan de revisión técnica 1.0 | Primera línea base |
| `LB-ASEG-02` | 2026-11-23 | SQAP 1.1, ficha 1.2, matriz 1.1, plan de evaluación 1.1 y plan de revisión técnica 1.0 | Cierre de SC-01 y SC-02 |

## Lo que falta

Estos son los compromisos que los documentos declaran con fecha, ordenados por fecha límite. Cumplirlos mantiene el plan coherente.

| Fecha límite | Pendiente | Responsable | Qué hay que hacer |
|---|---|---|---|
| HQ del 27 de noviembre | SC-03, que viene de NC-01 de AU-01 | Jorge y el comité | Presentar al comité la decisión sobre el documento de requerimientos vigente, su ubicación y su versión. Después ajustar la regla de admisión del plan de revisión técnica y repetir IE-1 |
| HQ del 27 de noviembre | Aprobación del cliente | Jaime | Pedir al Dr. Sánchez la aprobación del SQAP 1.0 y 1.1 y su participación en el comité de control de cambios |
| HQ del 27 de noviembre | R7 de la matriz | Jaime | Confirmar con el Dr. Sánchez qué cuentas de desarrollador de Apple y Google existen y quién las administra |
| 27 de noviembre | NC-02 de AU-01 | Jorge | Registrar en la matriz defecto-fuente de la Meta 3.4.1 los 11 hallazgos confirmados de RT-01 |
| Clase 14 | Control de versiones del código de 8=1 | Equipo | Proteger la rama principal, registrar la versión de CFG-SW-03 y llevar las solicitudes de cambio a issues del repositorio. El SQAP sube a la versión 1.2 |
| Sin fecha | Evidencias referenciadas | Equipo | Verificar que la hoja de costeo, el reporte de ESLint y jscpd y `evidencias/2026-10-22_proto-0.4.2/` estén en el repositorio del equipo de desarrollo |

## Componentes de las próximas sesiones

La Clase 14 agrega el control de versiones en `08_Configuracion_y_versiones`. La Clase 15 agrega el plan de pruebas en `07_Pruebas`. La Clase 16 cierra con el informe de calidad, que sube el SQAP a la versión 2.0 y crea una nueva línea base.

## Fuera de alcance

Estos documentos se conservan porque muestran el método que se siguió en el curso, pero no sustentan el SQAP.

| Archivo | Proyecto |
|---|---|
| `2.2.1_Revision_tecnica_PuntoNorte_2026-09-20_OTRO-PROYECTO.pdf` | PuntoNorte |
| `2.3.1_Auditoria_a_otro_equipo_PuntoNorte_2026-09-24_OTRO-PROYECTO.pdf` | PuntoNorte |
| `2.3.1_Plan_de_auditoria_PuntoNorte_2026-09-24_RECIBIDO_OTRO-PROYECTO.pdf` | PuntoNorte |
| `2.4.1_Costos_roles_y_herramientas_AutoStock_2026-09-29_OTRO-PROYECTO.pdf` | AutoStock |

## Registro de cambios de nombre

Esta tabla relaciona el nombre original de cada archivo con su ubicación actual, por si hay que revertir algo.

| Original | Actual |
|---|---|
| `2.1.1 Ficha del proyecto.pdf` | `01_Proposito_y_alcance/obsoletas/2.1.1_Ficha_del_proyecto_y_del_cliente_v1.0_2026-09-16_OBSOLETA.pdf` |
| `Lab-2.4.1-MMJ.pdf` | `03_Organizacion_y_roles/2.4.1_Costos_roles_y_analisis_estatico_2026-10-15.pdf` |
| `Practica+2.2.1++Diseño+y+ejecución+de+una+revisión+técnica.pdf` | `99_Fuera_de_alcance/2.2.1_Revision_tecnica_PuntoNorte_2026-09-20_OTRO-PROYECTO.pdf` |
| `2.3.1 Diseño y ejecución de auditoría.pdf` | `99_Fuera_de_alcance/2.3.1_Auditoria_a_otro_equipo_PuntoNorte_2026-09-24_OTRO-PROYECTO.pdf` |
| `Copia de Plan de auditoria de un tareas.pdf` | `99_Fuera_de_alcance/2.3.1_Plan_de_auditoria_PuntoNorte_2026-09-24_RECIBIDO_OTRO-PROYECTO.pdf` |
| `Meta_3.1.1_Modelos_de_calidad_del_producto_y_su_evolución.docx` | `06_Revisiones_evaluacion_y_auditorias/3.1.1_Modelo_de_calidad_ISO25010_2026-10-08.docx` |
| `Meta_3_2_1_Plan_de_evaluacion_de_la_calidad_del_producto.pdf` | `06_Revisiones_evaluacion_y_auditorias/3.2.1_Plan_de_evaluacion_v1.1_2026-10-15.pdf` |
| `Meta_3.3.1_Valoracion_de_la_calidad_del_producto.pdf` | `06_Revisiones_evaluacion_y_auditorias/3.3.1_Informe_de_evaluacion_2026-10-22.pdf` |
| `Meta_3.4.1_Analisis_de_causa_raiz.pdf` | `09_Problemas_acciones_y_mejora/3.4.1_Analisis_de_causa_raiz_2026-11-05.pdf` |
| `Meta_3.4.1_Analisis_de_causa_raiz_final.docx` | `09_Problemas_acciones_y_mejora/3.4.1_Analisis_de_causa_raiz_2026-11-05.docx` |
| `Meta_3.4.1_Analisis_de_causa_raiz.docx` | `09_Problemas_acciones_y_mejora/obsoletas/3.4.1_Analisis_de_causa_raiz_borrador_2026-11-05_OBSOLETA.docx` |
| `Meta+2.4.1.pdf` | `99_Fuera_de_alcance/2.4.1_Costos_roles_y_herramientas_AutoStock_2026-09-29_OTRO-PROYECTO.pdf` |
| `Meta_4.1.1_Plan_de_aseguramiento_de_la_calidad.pdf` (adjunto en el chat) | `00_SQAP/obsoletas/4.1.1_SQAP_v1.0_borrador_2026-11-05_OBSOLETA.pdf` |
| `Plantilla_Matriz_de_Riesgos_de_Calidad_40019 (1).xlsx` (Google Drive) | `05_Riesgos/obsoletas/2.1.1_Matriz_de_riesgos_v1.0_2026-09-18_OBSOLETA.xlsx`; la sustituye la versión 1.1 por SC-01 |
| `Lab-2.1.1-Reporte_40019.pdf` (Google Drive) | `05_Riesgos/obsoletas/2.1.1_Reporte_Clase4_formato_original_2026-09-18_OBSOLETA.pdf`; su contenido pasó a `2.1.1_Reporte_Clase4_riesgos_e_indicadores_2026-09-18.docx` |
| `2.2.1_Revision_tecnica_RT-01_8igual1_2026-11-11_POR-EJECUTAR.docx` | `06_Revisiones_evaluacion_y_auditorias/obsoletas/2.2.1_Revision_tecnica_RT-01_8igual1_plan_2026-11-11_OBSOLETA.docx`; lo sustituye la versión `SIMULADA` |
| `2.3.1_Auditoria_AU-01_8igual1_2026-11-11_POR-EJECUTAR.docx` | `06_Revisiones_evaluacion_y_auditorias/obsoletas/2.3.1_Auditoria_AU-01_8igual1_plan_2026-11-11_OBSOLETA.docx`; lo sustituye la versión `SIMULADA` |
| `Lab-2.4.1-MMJ.pdf` (segundo cambio) | `03_Organizacion_y_roles/obsoletas/2.4.1_Costos_roles_y_analisis_estatico_v1.0_2026-10-15_OBSOLETA.pdf`; lo sustituye la versión 1.1 |
| `00_SQAP/4.1.1_SQAP_v1.0_2026-11-05.docx` y `.pdf` | `00_SQAP/obsoletas/4.1.1_SQAP_v1.0_2026-11-05_OBSOLETA.docx` y `.pdf`; los sustituye la versión 1.1 por SC-02 |
| `01_Proposito_y_alcance/2.1.1_Ficha_del_proyecto_y_del_cliente_v1.1_2026-11-11.docx` y `.pdf` | `01_Proposito_y_alcance/obsoletas/2.1.1_Ficha_del_proyecto_y_del_cliente_v1.1_2026-11-11_OBSOLETA.docx` y `.pdf`; los sustituye la versión 1.2 por SC-01 |
