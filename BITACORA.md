# Bitácora de sesiones

[← Índice](README.md)

Una entrada por sesión, la más reciente arriba. Tres líneas bastan.

## Plantilla

```
### AAAA-MM-DD · [Nombre] · [horas] h
- Hice:
- Falló / dudas:
- Siguiente paso exacto:
```

## Control semanal

| Sem. | Entregable (Sí/Parcial/No) | Horas A | Horas B | ¿Qué se recorta? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 ⚑ | | | | |
| 5 | | | | |
| 6 ⚑ | | | | |
| 7 | | | | |
| 8 | | | | |

⚑ = punto de decisión

## Sesiones

### 2026-10-25 · S1-08: esquema JSON de la mina · duración no registrada
- Hice: definí el contrato de la mina estática en `data/esquemas/mina.schema.json`, documenté D20, los campos y las restricciones del futuro cargador, y añadí términos al glosario. El formato usa coordenadas en metros y túneles bidireccionales con longitud física. Pasaron las 61 pruebas y la comprobación de dependencias.
- Falló / dudas: ninguna falla en la validación estructural. Todavía no hay cargador ni comprobación ejecutable de referencias, geometría, conectividad y recorridos de hasta 500 m; esos requisitos se registraron para S1-11. No se creó aún la mina de prueba.
- Siguiente paso exacto: S1-09, crear `data/mina_prueba.json` con 6–8 nodos y documentar los recorridos desde cada frente a un refugio, conforme a D10 y D20.

### 2026-10-25 · S1-07: ciclo del motor · duración no registrada
- Hice: preparé una guía de encadenamiento hacia adelante, prioridad, refracción y traza, con un recorrido manual de tres reglas abstractas y preguntas de comprensión. No se añadieron reglas de minería ni código del motor.
- Falló / dudas: la comprensión individual queda por comprobar; una guía no la acredita automáticamente. El desempate de reglas y la identificación de disparos siguen pendientes de S1-12.
- Siguiente paso exacto: revisar el recorrido y continuar con S1-08, diseño del esquema JSON de la mina, antes de crear los datos de S1-09.

### 2026-10-25 · S1-05: lectura y escritura de JSON · duración no registrada
- Hice: registré la modalidad individual aprobada por el usuario en el contexto. Añadí un ejemplo de escritura y lectura JSON con archivos temporales, guía y pruebas de errores y protección contra sobrescritura.
- Falló / dudas: la revisión de compañero deja de ser requisito por decisión del usuario. La API de GitHub sigue sin acceso confirmado; publicar ramas por Git funciona. No se ha integrado a main ni se han cerrado tarjetas automáticamente.
- Siguiente paso exacto: ejecutar las comprobaciones de S1-05 y publicar la rama; después abordar S1-07 (ciclo del motor y refracción) antes del diseño del esquema JSON de S1-08.

### 2026-10-25 · S1-02: clases y módulos · duración no registrada
- Hice: confirmé la publicación previa de S1-04 (`b744ad0`) y preparé S1-02 en `luis/s1-02-clases-modulos`, basada en esa rama. Añadí una clase con `__init__`, una `dataclass` y una demostración que las importa desde otro módulo, con guía y pruebas.
- Falló / dudas: la consulta de PR sigue bloqueada; se diagnosticó rechazo del proxy a `api.github.com` (conexión HTTPS, 403). No se abrió ni fusionó un PR ni se sustituyó la revisión del compañero. El aprendizaje individual sigue pendiente de revisión.
- Siguiente paso exacto: verificar y publicar las comprobaciones de S1-02; resolver la apertura y revisión de los PR cuando haya acceso a la API o desde el navegador. Después continuar con S1-05 (leer y escribir JSON), sin dar por cerradas las tarjetas de aprendizaje.

### 2026-10-25 · Preparación de S1-04 · duración no registrada
- Hice: añadí `requirements-dev.txt` y la guía multiplataforma de instalación, comprobación de rama y revisión por PR; preparé la rama `luis/s1-04-nivelacion`. La instalación, la comprobación de dependencias y las 14 pruebas pasaron.
- Falló / dudas: la API de GitHub devolvió `Forbidden`; no se pudo consultar la tarjeta ni abrir el PR automáticamente. La publicación de la rama se comprueba por separado; no se considera completada S1-04 sin revisión del compañero.
- Siguiente paso exacto: abrir el PR de esta rama en el fork, vincular la issue correcta y obtener revisión; después continuar con S1-02 (clases y módulos).

### 2026-10-25 · Soluciones verificadas de S1-01 · duración no registrada
- Hice: por petición del usuario, implementé los tres ejercicios en `ejercicios/nivelacion.py` y sus comprobaciones en `tests/test_nivelacion.py`; la ejecución de consola produjo los resultados esperados y pasaron 14 casos con pytest.
- Falló / dudas: ninguna falla en los casos ejecutados. Falta que el integrante revise y explique las soluciones para acreditar el aprendizaje; no se cerraron tarjetas ni se publicó en GitHub.
- Siguiente paso exacto: revisar las soluciones de S1-01 y después practicar S1-04 (rama y PR), antes de S1-02 según el orden sugerido. La aplicación sigue sin implementar.

### 2026-10-25 · Inicio de S1-01 en el fork · duración no registrada
- Hice: revisamos el plan y preparamos una guía de nivelación de Python con tres ejercicios del dominio, casos de comprobación y ejecución en el entorno virtual existente.
- Falló / dudas: no hay soluciones del integrante que revisar todavía; S1-01 continúa pendiente. No se implementó código de la aplicación ni se modificó el tablero del equipo.
- Siguiente paso exacto: resolver el ejercicio 1 de `docs/plan/nivelacion-python.md`, ejecutarlo con sus tres entradas y revisar el resultado antes de continuar con los ejercicios 2 y 3.

### 2026-10-24 · Tablero del sprint 1 · 2 h
- Hice: cerramos S1-00, S1-03 y S1-03b; configuramos GitHub Projects (columnas, campos, etiquetas, workflows) y cargamos las 27 tarjetas del sprint 1 con dueño, estimación, prioridad e iteración.
- Falló / dudas: S1-03 y S1-03b son de infraestructura y no pasan por PR (excepción consciente a la DoD). Horas estimadas, sin medir: ~2,5 h brutas y ~1,75 h productivas.
- Siguiente paso exacto: S1-01, nivelación de Python con ejercicios del dominio.

### 2026-10-17 · Guía de carga del tablero
- Hice: agregamos a kanban.md la guía paso a paso para cargar tarjetas (6.2.2) y los títulos del Backlog listos para copiar.
- Falló / dudas: ninguna.
- Siguiente paso exacto: S1-03 (configurar el tablero) y S1-03b (cargar tarjetas siguiendo 6.2.2).

### 2026-10-17 · Plantilla del tablero y Backlog
- Hice: elegimos la plantilla Kanban de GitHub Projects; definimos qué va en el Backlog.
- Falló / dudas: ninguna.
- Siguiente paso exacto: crear el proyecto con la plantilla Kanban y continuar con S1-03.

### 2026-10-17 · Aprendizaje de GitHub Projects
- Hice: agregamos `S1-00` (guía oficial, 0,5 h c/u) y extendimos `S1-04` para practicar PR vinculados a tarjetas.
- Falló / dudas: B queda 1,5 h sobre la capacidad en el sprint 1.
- Siguiente paso exacto: S1-00, leer *Quickstart for Projects*; luego S1-03.

### 2026-10-17 · Recalibración y configuración del tablero
- Hice: ajustamos el aprendizaje por la base en Java/C# (D17); documentamos la configuración de GitHub Projects y los sprints como iteraciones (D18).
- Falló / dudas: el tablero recién creado no tiene las columnas del plan.
- Siguiente paso exacto: S1-03, configurar GitHub Projects con los pasos 1–7; luego S1-03b, cargar las tarjetas.

### 2026-10-17 · Sprints y tablero
- Hice: aprobamos 4 sprints de 2 semanas; definimos el tablero Kanban, cómo escribir tareas y las 18 tareas del sprint 1; D15–D16; glosario de gestión.
- Falló / dudas: el núcleo del sprint 1 excede la capacidad en 1,5 h por persona.
- Siguiente paso exacto: S1-03, crear el repositorio en GitHub y el tablero con las tarjetas del sprint 1.

### 2026-10-17 · Niveles de riesgo y glosario
- Hice: elegimos la opción b (supuesto del equipo) para el peligro inmediato; tabla de niveles por gas; glosario; D12–D14.
- Falló / dudas: ninguna.
- Siguiente paso exacto: nivelación en Python y diseño del esquema JSON de la mina (con coordenadas en metros y refugios a ≤ 500 m).

### 2026-10-17 · Umbrales normativos
- Hice: extraje los umbrales del DS 024-2016-EM y sus Anexos (Anexo 15, Art. 246, 248, 151 y Anexo 19) al catálogo de reglas; registré D09–D11.
- Falló / dudas: la norma no da niveles de emergencia para gases. Decidir: segunda fuente o supuesto del equipo.
- Siguiente paso exacto: revisar con el compañero la tabla de umbrales y decidir la fuente del nivel de peligro inmediato.

### 2026-10-17 · Plan inicial
- Hice: definimos enfoque, alcance, cronograma, reparto y flujo de trabajo.
- Falló / dudas: verificar umbrales del DS 024-2016-EM.
- Siguiente paso exacto: reunión del equipo para aceptar el reparto y crear el repositorio en GitHub.
