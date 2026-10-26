"""Filtro directo sobre datos de entrada, sin usar el motor ni sus conclusiones."""

from types import MappingProxyType

from .escenarios import validar_lecturas
from .modelo import _validar_numero


def costos_linea_base(mina, hechos, limite_co):
    _validar_numero(limite_co, "limite_co")
    if limite_co <= 0:
        raise ValueError("El límite de CO debe ser positivo")
    lecturas = validar_lecturas(mina, hechos)
    cerrados = set()
    for entidad, atributo, valor in lecturas:
        if ((atributo == "co_ppm" and valor > limite_co)
                or (atributo in ("incendio_reportado", "derrumbe_reportado") and valor is True)):
            cerrados.add(entidad)
    return MappingProxyType({id: None if id in cerrados else a.longitud_m
                             for id, a in mina.aristas.items()})
