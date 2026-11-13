---
tags: [aseguramiento, sqap, inventario, 8igual1]
actualizado: 2026-11-11
---

# Inventario de documentos del SQAP 8=1

Esta carpeta es el repositorio de la materia Aseguramiento de la Calidad del Software (40019). Guarda los productos que sustentan el plan de aseguramiento de 8=1 (SQAP-8IGUAL1), cada uno en la carpeta del componente del plan al que da sustento. Las carpetas siguen la numeración de las secciones del SQAP v1.0, así que la Tabla 17 del plan y este inventario se pueden leer lado a lado.

La regla del equipo es que todo lo que sustenta el plan debe ser del proyecto 8=1, el de la ficha. Lo que se hizo sobre otro proyecto se guarda en `99_Fuera_de_alcance` como referencia del método y se rehace sobre 8=1.

## Convención de nombres

Los nombres siguen la forma `<código>_<Título>_<AAAA-MM-DD>[_<ETIQUETA>].<ext>`. El código es el número de la actividad del curso (2.1.1 a 4.1.1), lo que ordena los archivos en el orden del semestre. El título va sin acentos ni espacios, y si el documento tiene versión propia, la versión va en el título. La fecha es la de «Lugar y fecha» del documento.

La etiqueta solo aparece cuando el archivo es una excepción. Hay cinco.

- `POR-EJECUTAR` marca un documento preparado cuya actividad todavía no ocurre. Cuando ocurre, se cambia la fecha por la de la sesión y se quita la etiqueta.
- `SIMULADA` marca una actividad que se documentó como ejercicio simulado de escritorio, con autorización del docente. El documento lo declara en su primer punto.
- `RECIBIDO` marca un documento hecho por otro equipo.
- `OBSOLETA` marca una versión superada, que se guarda en la subcarpeta `obsoletas` de su componente.
- `OTRO-PROYECTO` marca un documento que no es de 8=1 y que vive en `99_Fuera_de_alcance`.

Cuando entra un documento nuevo, se nombra con la convención, se guarda en la carpeta del componente principal que sustenta, la versión anterior pasa a `obsoletas` y se actualizan este inventario y la Tabla 17 del SQAP.

## Documentos por componente

| Carpeta | Archivo | Producto | Clase | Estado |
|---|---|---|---|---|
| 00_SQAP | `4.1.1_SQAP_v1.0_2026-11-05.docx` y `.pdf` | Plan de aseguramiento, versión 1.0 | 12 | Listo para entregar |
| 01_Proposito_y_alcance | `2.1.1_Ficha_del_proyecto_y_del_cliente_v1.1_2026-11-11.docx` y `.pdf` | Ficha del proyecto y del cliente, versión 1.1 | 1 y 4 | Vigente. Normas vigentes, roles del Lab 2.4.1 e hitos |
| 03_Organizacion_y_roles | `2.4.1_Costos_roles_y_analisis_estatico_v1.1_2026-11-11.docx` y `.pdf` | Costos de la mala calidad, roles y análisis estático, versión 1.1 | 7 | Vigente. El costeo usa los 11 hallazgos de RT-01: la revisión costó 7 h y evitó entre 1,266 y 1,386 h |
| 05_Riesgos | `2.1.1_Matriz_de_riesgos_v1.0_2026-09-18.xlsx` | Matriz de riesgos de calidad, versión 1.0 | 4 | Vigente. La versión 1.1 vence el 19 de noviembre |
| 05_Riesgos | `2.1.1_Reporte_Clase4_riesgos_e_indicadores_2026-09-18.docx` y `.pdf` | Reporte de la Clase 4: matriz, estimación de 67 horas, indicadores I1 a I3 y trazabilidad | 4 | Vigente, pasado al formato de reporte de la materia |
| 06_Revisiones_evaluacion_y_auditorias | `2.2.1_Revision_tecnica_RT-01_8igual1_2026-11-11_SIMULADA.docx` y `.pdf` | Revisión técnica RT-01 sobre 8=1, ejercicio simulado | 5 | Terminada. 11 hallazgos (4 críticos), dictamen «No aceptado» |
| 06_Revisiones_evaluacion_y_auditorias | `2.3.1_Auditoria_AU-01_8igual1_2026-11-11_SIMULADA.docx` y `.pdf` | Auditoría AU-01 de RT-01, ejercicio simulado | 6 | Terminada. 2 no conformidades abiertas (NC-01 y NC-02) |
| 06_Revisiones_evaluacion_y_auditorias | `3.1.1_Modelo_de_calidad_ISO25010_2026-10-08.docx` | Modelo de calidad elegido | 8 | Vigente |
| 06_Revisiones_evaluacion_y_auditorias | `3.2.1_Plan_de_evaluacion_v1.1_2026-10-15.pdf` | Plan de evaluación v1.1 | 9 | Vigente |
| 06_Revisiones_evaluacion_y_auditorias | `3.3.1_Informe_de_evaluacion_2026-10-22.pdf` | Informe de evaluación | 10 | Vigente |
| 09_Problemas_acciones_y_mejora | `3.4.1_Analisis_de_causa_raiz_2026-11-05.pdf` y `.docx` | Matriz defecto-fuente y acciones AP-01 a AP-04 | 11 | Vigente |

Las carpetas `02` y `04` están vacías porque esos componentes se redactan dentro del SQAP. `07` y `08` esperan los productos de las Clases 13 a 15, y `10` se sustenta en el reporte de la Clase 4, que vive en `05_Riesgos`.

## Lo que falta

Todos los documentos de la carpeta están listos para entregar. Lo que sigue son compromisos que los propios documentos declaran con fecha, ordenados por fecha límite. Cumplirlos mantiene el plan coherente.

| Fecha límite | Pendiente | Responsable | Qué hay que hacer |
|---|---|---|---|
| 14 de noviembre | NC-01 de AU-01 | Jorge y Jaime | Confirmar cuál documento de requerimientos es el vigente (el SQAP y la Meta 3.3.1 citan un «v1.3 con 34 requisitos»; el SRS de Drive tiene RF-01 a RF-78), ponerle número de versión y ajustar la regla de admisión del plan de revisión |
| 14 de noviembre | NC-02 de AU-01 | Jorge | Registrar en la matriz defecto-fuente de la Meta 3.4.1 los 11 hallazgos confirmados de RT-01 (H-01 a H-12, sin H-11, que se descartó) |
| 19 de noviembre | Matriz de riesgos v1.1 | Jorge | Agregar el riesgo de las tiendas móviles y nuevas fechas de revisión |
| Clase 13 | SQAP v1.1 | Jorge | Registrar que RT-01 y AU-01 se hicieron como ejercicios simulados, sus resultados, que IC-7 se activó con 4 críticos y que el Lab 2.4.1 pasó a la versión 1.1 (Tabla 17) |
| Sin fecha | Evidencias referenciadas | Equipo | Verificar que la hoja de costeo, el reporte de ESLint y jscpd y `evidencias/2026-10-22_proto-0.4.2/` estén en el repositorio del equipo |

## Componentes de las próximas sesiones

La presentación de la Clase 12 asigna un componente a cada sesión. La Clase 13 agrega la configuración y la 14 el control de versiones, los dos en `08_Configuracion_y_versiones`. La Clase 15 agrega el plan de pruebas en `07_Pruebas`. La Clase 16 cierra con el informe de calidad, que sube el SQAP a la versión 2.0.

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
| `Plantilla_Matriz_de_Riesgos_de_Calidad_40019 (1).xlsx` (Google Drive) | `05_Riesgos/2.1.1_Matriz_de_riesgos_v1.0_2026-09-18.xlsx` |
| `Lab-2.1.1-Reporte_40019.pdf` (Google Drive) | `05_Riesgos/obsoletas/2.1.1_Reporte_Clase4_formato_original_2026-09-18_OBSOLETA.pdf`; su contenido pasó a `2.1.1_Reporte_Clase4_riesgos_e_indicadores_2026-09-18.docx` |
| `2.2.1_Revision_tecnica_RT-01_8igual1_2026-11-11_POR-EJECUTAR.docx` | `06_Revisiones_evaluacion_y_auditorias/obsoletas/2.2.1_Revision_tecnica_RT-01_8igual1_plan_2026-11-11_OBSOLETA.docx`; lo sustituye la versión `SIMULADA` |
| `2.3.1_Auditoria_AU-01_8igual1_2026-11-11_POR-EJECUTAR.docx` | `06_Revisiones_evaluacion_y_auditorias/obsoletas/2.3.1_Auditoria_AU-01_8igual1_plan_2026-11-11_OBSOLETA.docx`; lo sustituye la versión `SIMULADA` |
| `Lab-2.4.1-MMJ.pdf` (segundo cambio) | `03_Organizacion_y_roles/obsoletas/2.4.1_Costos_roles_y_analisis_estatico_v1.0_2026-10-15_OBSOLETA.pdf`; lo sustituye la versión 1.1 |
