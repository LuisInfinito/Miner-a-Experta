"""Conocimiento mínimo R01–R05; separado del motor genérico."""

import json
from pathlib import Path

from .cargador import _objeto_sin_repeticiones, _rechazar_constante
from .modelo import _validar_numero
from .motor import Condicion, Regla


def reglas_eventos() -> tuple[Regla, ...]:
    """Cierres por eventos reportados; supuestos R04/R05, sin geomecánica."""
    return (
        Regla("R04", (Condicion("incendio_reportado", "eq", True),),
              (("cerrado", True),), 100),
        Regla("R05", (Condicion("derrumbe_reportado", "eq", True),),
              (("cerrado", True),), 100),
    )


def reglas_co(ruta: str | Path) -> tuple[Regla, ...]:
    with Path(ruta).open(encoding="utf-8") as archivo:
        datos = json.load(archivo, object_pairs_hook=_objeto_sin_repeticiones,
                          parse_constant=_rechazar_constante)
    if not isinstance(datos, dict) or set(datos) != {"co_ppm"}:
        raise ValueError("La configuración requiere co_ppm")
    limites = datos["co_ppm"]
    nombres = ("alerta", "riesgo_alto", "peligro_inmediato")
    if not isinstance(limites, dict) or set(limites) != set(nombres):
        raise ValueError("Los niveles de CO son incorrectos")
    for nombre in nombres:
        _validar_numero(limites[nombre], nombre)
    if not 0 < limites["alerta"] < limites["riesgo_alto"] < limites["peligro_inmediato"]:
        raise ValueError("Los niveles de CO deben ser positivos y crecientes")
    return (
        Regla("R01", (Condicion("co_ppm", "gt", limites["alerta"]),),
              (("alerta_co", True),), 30),
        Regla("R02", (Condicion("alerta_co", "eq", True),
                      Condicion("co_ppm", "gt", limites["riesgo_alto"])),
              (("riesgo_alto_co", True),), 20),
        Regla("R03", (Condicion("riesgo_alto_co", "eq", True),
                      Condicion("co_ppm", "gt", limites["peligro_inmediato"])),
              (("cerrado", True),), 10),
    )
