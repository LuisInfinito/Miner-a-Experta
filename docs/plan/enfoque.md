# 1. Enfoque

[← Índice](../../README.md)

## 1.1 Problema

En una emergencia en una mina subterránea hay que decidir rápido qué zonas son peligrosas y por dónde evacuar a cada trabajador. Esa decisión la toma normalmente un experto en seguridad combinando lecturas de sensores, conocimiento técnico y normativa.

## 1.2 Propuesta

Un **sistema experto híbrido** que combina:

| Componente | Pregunta que responde |
|---|---|
| **Motor de reglas (forward chaining)** | ¿Qué está pasando y qué tan peligroso es cada túnel? |
| **Planificador (Dijkstra → A\*)** | ¿Cuál es la mejor ruta dado ese estado? |
| **Módulo de explicación** | ¿Por qué se cerró este túnel? ¿Cómo se llegó a esta decisión? |

Las reglas **traducen el mundo en costos y cierres**; el planificador **consume esos costos**. Ninguna mitad resuelve el problema sola.

## 1.3 Dominio: mina metálica peruana

Se modela una mina metálica subterránea, típica del Perú. Peligros cubiertos:

- Gases: CO, NO₂ (post-voladura), deficiencia de O₂.
- Falla de ventilación.
- Incendio.
- Caída de rocas (modelada como evento reportado que bloquea un túnel, sin análisis geomecánico).

Se descarta el metano: es propio de minas de carbón.

## 1.4 Fuente del conocimiento

Los umbrales numéricos de las reglas se toman del **DS 024-2016-EM** (Reglamento de Seguridad y Salud Ocupacional en Minería) y sus modificatorias, **solo como fuente de valores**, no como algo a modelar completo. Cada regla cita su fuente en el [catálogo](../reglas.md).

> Umbrales extraídos y verificados el 2026-10-17 (ver [catálogo](../reglas.md)). La norma da límites de exposición laboral, no niveles de emergencia: esos se tratan como supuestos del equipo o con una segunda fuente.

## 1.5 Prioridades (por ser un curso de Sistemas Expertos)

El peso del proyecto está en el **razonamiento**, no en el algoritmo de rutas:

1. Motor de inferencia propio, con prioridad y refracción.
2. Explicación de "¿por qué?" y "¿cómo?".
3. Factores de certeza (estilo MYCIN).
4. Conocimiento con fuente citada.

La simulación temporal (propagación de gases por turnos) queda como extra, porque es más ingeniería de simulación que sistemas expertos.

## 1.6 Decisiones de base

- Las reglas **solo pueden aumentar costos** (multiplicador ≥ 1 o cierre). Así la distancia euclidiana sigue siendo una heurística admisible y A\* sigue siendo correcto.
- Datos en **JSON**, sin base de datos.
- Motor y planificador **escritos por el equipo**, sin librerías de sistemas expertos.

## 1.7 Cómo se demuestra el valor

Se compara el sistema contra una **línea base fuerte: Dijkstra con filtro por umbral de sensor** (bloquea un túnel si un sensor supera su límite). El sistema debe mostrar casos donde el encadenamiento de reglas evita peligros que el filtro simple no detecta (por ejemplo, túneles vecinos a un riesgo que aún no tienen lecturas altas).
