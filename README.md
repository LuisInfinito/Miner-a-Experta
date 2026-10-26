# Sistema Experto para Emergencias y Evacuación en Minería Subterránea

Proyecto del curso **Sistemas Expertos**. Proyecto original de 2 integrantes; este fork se desarrolla individualmente con ayuda del asistente. Lenguaje: Python.

Sistema que, ante una emergencia simulada en una mina metálica subterránea, **infiere el estado de riesgo** con un motor de reglas propio (forward chaining), **calcula rutas de evacuación** para varios mineros y **explica cada decisión**.

## Cómo leer este repositorio

Este README es la portada. La documentación se lee como un informe, en orden:

### Parte I — Plan
1. [Enfoque](docs/plan/enfoque.md)
2. [Alcance](docs/plan/alcance.md)
3. [Cronograma y reparto de trabajo](docs/plan/cronograma-y-reparto.md)
4. [Flujo de trabajo](docs/plan/flujo-de-trabajo.md)
5. [Sprints](docs/plan/sprints.md)
6. [Tablero Kanban](docs/plan/kanban.md)
7. [S1-01: nivelación de Python](docs/plan/nivelacion-python.md)
8. [S1-04: práctica de rama y revisión](docs/plan/practica-git.md)
9. [S1-02: clases y módulos](docs/plan/clases-y-modulos.md)
10. [S1-05: lectura y escritura de JSON](docs/plan/lectura-json.md)
11. [S1-07: ciclo del motor y refracción](docs/plan/ciclo-motor.md)
12. [S1-08: esquema JSON de la mina](docs/plan/esquema-mina.md)
13. [S1-09: mina académica de prueba](docs/plan/mina-prueba.md)
14. [S1-10: modelo de la mina en Python](docs/plan/modelo-mina.md)
15. [Sprint 1: cargador y motor mínimo](docs/plan/entregable-minimo.md)
16. [Sprint 2: costos y rutas con Dijkstra](docs/plan/rutas-costos.md)
17. [Sprint 2: escenarios y línea base](docs/plan/escenarios-comparacion.md)
18. [Sprint 2: gases y ventilación](docs/plan/gases-ventilacion.md)
19. [Nivel 1: mina ampliada y verificación](docs/plan/nivel1-verificacion.md)

### Parte II — Desarrollo (un capítulo por semana)
- [Semana 1](docs/capitulos/semana-01.md)
- *(se agrega un capítulo cada semana a partir de la [plantilla](docs/capitulos/_plantilla.md))*

### Anexos
- [Catálogo de reglas](docs/reglas.md)
- [Registro de decisiones](docs/decisiones.md)
- [Glosario de siglas y términos](docs/glosario.md)
- [Bitácora de sesiones](BITACORA.md)
- [Contexto vivo del proyecto](docs/contexto.md) *(interno)*

## Cronología del código

Cada semana cerrada se marca con un tag (`semana-01`, `semana-02`, …). Cada capítulo enlaza al tag de su semana, para ver el código exacto de ese momento.

## Estructura

```
mina-experta/
├── README.md            # portada e índice
├── BITACORA.md          # diario de sesiones
├── docs/
│   ├── plan/            # enfoque, alcance, cronograma, flujo, sprints, kanban
│   ├── capitulos/       # un capítulo por semana
│   ├── reglas.md        # catálogo de reglas con fuente y prueba
│   ├── decisiones.md    # decisiones de diseño y su porqué
│   └── glosario.md      # siglas y términos técnicos
├── data/escenarios/     # minas y emergencias en JSON
├── src/                 # código fuente
└── tests/               # pruebas pytest
```

## Ejecución

La consola dispone de 25 tipos de regla, traza, explicación directa y rutas con Dijkstra y costos dinámicos. El punto de control técnico de Nivel 1 incluye una mina de 16 nodos y tres escenarios completos, además de cuatro ejemplos de práctica. Un caso controlado muestra cómo el motor evita un vecino expuesto a humo que el filtro local no identifica. Las capacidades de Nivel 2 siguen pendientes. Desde la raíz del repositorio, con el entorno virtual preparado:

```bash
.venv/bin/python -m pip install -e . -r requirements-dev.txt
.venv/bin/python -m mina_experta --escenario data/escenarios/nivel1_riesgo_vecino.json --explicar tunel_10_12
.venv/bin/python -m mina_experta --desde n5 --co tunel_3_4=120
.venv/bin/python -m mina_experta --escenario data/escenarios/co_moderado.json
.venv/bin/python ejercicios/nivelacion.py
.venv/bin/python -m ejercicios.clases
.venv/bin/python -m ejercicios.mina_en_memoria
.venv/bin/python -m pytest -q
```

Consulta la [guía de nivelación](docs/plan/nivelacion-python.md) para los objetivos y los casos esperados.
