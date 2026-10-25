# Anexo A — Catálogo de reglas

[← Índice](../README.md)

Cada regla debe tener: categoría, condición, conclusión, prioridad, fuente, tipo de fuente, justificación y prueba.

**Categorías:** `DIAG` diagnóstico · `RIESGO` riesgo encadenado · `RUTA` efecto sobre la ruta · `DEC` decisión (Nivel 2).

**Tipo de fuente:** `NORMA` (valor citado del DS 024-2016-EM) · `SUPUESTO` (criterio razonado del equipo, sin respaldo normativo).

## Umbrales de referencia

Extraídos el 2026-10-17 del texto del **DS 024-2016-EM** (con las modificaciones del DS 023-2017-EM incluidas en el documento oficial de gob.pe) y de su documento de **Anexos**.

### Gases (Anexo 15 — Límites de exposición ocupacional para agentes químicos)

| Variable | TWA (8 h) | STEL (15 min) | Techo (C) | Unidad | Fuente | Verificado |
|---|---|---|---|---|---|---|
| O₂ (mínimo) | 19.5 | — | 22.5 (máximo) | % | Anexo 15, ítem 36; Art. 246 b) | ☑ |
| CO | 25 | — | — | ppm | Anexo 15, ítem 33 | ☑ |
| NO₂ | 3 | 5 | — | ppm | Anexo 15, ítem 21 | ☑ |
| CO₂ | 5000 | 30000 | — | ppm | Anexo 15, ítem 20 | ☑ |
| H₂S | 10 | 15 | — | ppm | Anexo 15, ítem 5 | ☑ |

Definiciones del propio Anexo 15:
- **TWA:** promedio ponderado durante la jornada de 8 h.
- **STEL:** exposición de corta duración, normalmente 15 min.
- **Techo (C):** límite que no debe sobrepasarse en ningún momento.

### Ventilación

| Variable | Valor | Unidad | Fuente | Verificado |
|---|---|---|---|---|
| Velocidad mínima del aire | 20 | m/min | Art. 248 | ☑ |
| Velocidad mínima del aire si se usa ANFO u otros agentes de voladura | 25 | m/min | Art. 248 | ☑ |
| Velocidad máxima del aire | 250 | m/min | Art. 248 | ☑ |
| Labor con una sola vía de acceso y avance > 60 m | Ventilador auxiliar obligatorio | — | Art. 246 f) | ☑ |

### Refugios (estaciones de refugio)

| Variable | Valor | Unidad | Fuente | Verificado |
|---|---|---|---|---|
| Distancia máxima del refugio a los frentes de trabajo | 500 | m | Anexo 19, ítem 1 | ☑ |
| Toda mina subterránea dispone de estaciones de refugio herméticas | — | — | Art. 151 (mod. DS 023-2017-EM) | ☑ |

### Lo que la norma **no** da

| Necesidad del sistema | Situación | Tratamiento |
|---|---|---|
| Niveles de gas **peligrosos de inmediato** (para cerrar un túnel durante una emergencia) | La norma solo fija límites de exposición laboral (TWA/STEL), no niveles de emergencia | `SUPUESTO` (ver tabla de niveles y D12) |
| Efecto de un incendio o derrumbe sobre túneles vecinos | No está en la norma | `SUPUESTO` |
| Multiplicadores de costo (×2, ×3…) | No está en la norma | `SUPUESTO` |

## Niveles de riesgo por gas

Cómo se usan los umbrales en las reglas (decisiones D09 y D12). Cada nivel aumenta el costo del túnel; solo el último lo cierra.

**Criterio del equipo (`SUPUESTO`):**
- *Riesgo alto* = STEL o techo si la norma lo da; si no, 2 × TWA.
- *Peligro inmediato* = 2 × el valor de riesgo alto.

| Gas | Normal | Alerta | Riesgo alto | Peligro inmediato (cierre) |
|---|---|---|---|---|
| CO (ppm) | ≤ 25 | > 25 `NORMA` | > 50 `SUPUESTO` | > 100 `SUPUESTO` |
| NO₂ (ppm) | ≤ 3 | > 3 `NORMA` | > 5 `NORMA` | > 10 `SUPUESTO` |
| CO₂ (ppm) | ≤ 5000 | > 5000 `NORMA` | > 30000 `NORMA` | > 60000 `SUPUESTO` |
| H₂S (ppm) | ≤ 10 | > 10 `NORMA` | > 15 `NORMA` | > 30 `SUPUESTO` |
| O₂ (%) | 19,5 – 22,5 | < 19,5 `NORMA` o > 22,5 `NORMA` | < 18 `SUPUESTO` | < 16 `SUPUESTO` |

El O₂ funciona al revés (el peligro es que **falte**), por eso no sigue el criterio de multiplicar; sus valores bajo 19,5 % son supuestos del equipo.

> Estos valores **no son niveles reales de peligro para la vida**: son parámetros de la simulación. Se guardarán en un archivo de configuración JSON para poder cambiarlos sin tocar el código (D13).

## Plantilla de regla

### R00 — Nombre

| Campo | Valor |
|---|---|
| Categoría | DIAG / RIESGO / RUTA / DEC |
| SI | |
| ENTONCES | |
| Prioridad | |
| Fuente | |
| Tipo de fuente | NORMA / SUPUESTO |
| Justificación | *(una frase)* |
| Prueba | `tests/...::test_...` |

## Reglas

Cadena mínima de CO para el entregable del sprint 1. Las tres reglas se instancian por entidad, sin mezclar hechos de túneles diferentes. Usan `>` estricto: exactamente 25, 50 y 100 ppm no activan respectivamente el siguiente escalón. Los niveles se leen de `data/configuracion/umbrales.json`; sus valores iniciales son los de D09/D12. Las conclusiones de los escalones anteriores se conservan como justificaciones, no como niveles mutuamente excluyentes.

### R01 — Diagnóstico de alerta por CO

| Campo | Valor |
|---|---|
| Categoría | DIAG |
| SI | `co_ppm > co_ppm.alerta` (inicialmente 25 ppm) |
| ENTONCES | Añadir `(entidad, alerta_co, True)` |
| Prioridad | 30 |
| Fuente | Anexo 15, ítem 33 (TWA de CO: 25 ppm); política de simulación D09 |
| Tipo de fuente | SUPUESTO: clasificación instantánea basada en un valor normativo ocupacional |
| Justificación | Hace explícito el primer escalón del razonamiento sin cerrar un túnel solo por exceder un TWA. |
| Prueba | `tests/test_conocimiento.py::test_cadena_y_fronteras_co` |

### R02 — Riesgo alto por CO encadenado

| Campo | Valor |
|---|---|
| Categoría | RIESGO |
| SI | `alerta_co == True` y `co_ppm > co_ppm.riesgo_alto` (inicialmente 50 ppm), en la misma entidad |
| ENTONCES | Añadir `(entidad, riesgo_alto_co, True)` |
| Prioridad | 20 |
| Fuente | D12: 2 × TWA para CO, que no tiene STEL en el catálogo |
| Tipo de fuente | SUPUESTO |
| Justificación | Separa la alerta de un riesgo más alto y utiliza explícitamente la conclusión anterior. |
| Prueba | `tests/test_conocimiento.py::test_cadena_y_fronteras_co` |

### R03 — Cierre por peligro inmediato de CO

| Campo | Valor |
|---|---|
| Categoría | RUTA |
| SI | `riesgo_alto_co == True` y `co_ppm > co_ppm.peligro_inmediato` (inicialmente 100 ppm), en la misma entidad |
| ENTONCES | Añadir `(entidad, cerrado, True)`; el futuro planificador consumirá el cierre |
| Prioridad | 10 |
| Fuente | D12: 2 × riesgo alto |
| Tipo de fuente | SUPUESTO |
| Justificación | Reserva el cierre para el último escalón de la simulación, conservando la cadena de justificación. |
| Prueba | `tests/test_conocimiento.py::test_cadena_y_fronteras_co` |

### R04 — Cierre por incendio reportado

| Campo | Valor |
|---|---|
| Categoría | RUTA |
| SI | `incendio_reportado == True` |
| ENTONCES | Añadir `(entidad, cerrado, True)` |
| Prioridad | 100 |
| Fuente | Política académica del proyecto para el evento de incendio |
| Tipo de fuente | SUPUESTO |
| Justificación | Un reporte explícito impide considerar transitable el túnel afectado; no se modela propagación a vecinos. |
| Prueba | `tests/test_conocimiento.py::test_eventos_reportados` |

### R05 — Cierre por derrumbe reportado

| Campo | Valor |
|---|---|
| Categoría | RUTA |
| SI | `derrumbe_reportado == True` |
| ENTONCES | Añadir `(entidad, cerrado, True)` |
| Prioridad | 100 |
| Fuente | D04: caída de rocas como evento reportado, sin análisis geomecánico |
| Tipo de fuente | SUPUESTO |
| Justificación | Traduce el bloqueo reportado en un hecho de cierre, sin intentar predecir derrumbes. |
| Prueba | `tests/test_conocimiento.py::test_eventos_reportados` |
