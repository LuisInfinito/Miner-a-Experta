"""Consola de mina, inferencia y rutas por costo dinámico."""

import argparse
import math

from .cargador import cargar_mina
from .conocimiento import cargar_umbrales_co, reglas_co, reglas_eventos, reglas_costos
from .escenarios import cargar_escenario, validar_lecturas
from .linea_base import costos_linea_base
from .motor import Motor
from .planificador import costos_desde_hechos, ruta_menor_costo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mina")
    parser.add_argument("--umbrales")
    parser.add_argument("--costos")
    parser.add_argument("--escenario", metavar="ARCHIVO")
    parser.add_argument("--comparar", action="store_true",
                        help="Mostrar también Dijkstra con filtro directo por umbral")
    parser.add_argument("--desde", action="append", default=[], metavar="NODO",
                        help="Origen de una ruta; repetir para más ubicaciones")
    parser.add_argument("--hasta", action="append", default=[], metavar="NODO",
                        help="Destinos permitidos; por defecto, todas las salidas")
    parser.add_argument("--co", action="append", default=[], metavar="TUNEL=PPM",
                        help="Lectura simulada; repetir para túneles distintos")
    parser.add_argument("--incendio", action="append", default=[], metavar="TUNEL")
    parser.add_argument("--derrumbe", action="append", default=[], metavar="TUNEL")
    args = parser.parse_args()
    try:
        escenario = None
        if args.escenario:
            if (args.desde or args.hasta or args.co or args.incendio or args.derrumbe
                    or any(v is not None for v in (args.mina, args.umbrales, args.costos))):
                raise ValueError("--escenario no se mezcla con entradas manuales")
            escenario = cargar_escenario(args.escenario)
        mina = escenario.mina if escenario else cargar_mina(args.mina or "data/mina_prueba.json")
        umbrales = escenario.umbrales if escenario else args.umbrales or "data/configuracion/umbrales.json"
        config_costos = escenario.costos if escenario else args.costos or "data/configuracion/costos.json"
        hechos = []
        entidades = set()
        for lectura in args.co:
            entidad, texto = lectura.split("=", 1)
            valor = float(texto)
            if entidad not in mina.aristas:
                raise ValueError(f"Túnel desconocido: {entidad}")
            if entidad in entidades:
                raise ValueError(f"Lectura repetida para {entidad}; use una por ejecución")
            if not math.isfinite(valor) or valor < 0:
                raise ValueError("El CO debe ser un número finito no negativo")
            entidades.add(entidad)
            hechos.append((entidad, "co_ppm", valor))
        for atributo, reportados in (("incendio_reportado", args.incendio),
                                     ("derrumbe_reportado", args.derrumbe)):
            for entidad in reportados:
                if entidad not in mina.aristas:
                    raise ValueError(f"Túnel desconocido: {entidad}")
                hechos.append((entidad, atributo, True))
        hechos = escenario.hechos if escenario else validar_lecturas(mina, hechos)
        resultado = Motor((*reglas_co(umbrales), *reglas_eventos(),
                           *reglas_costos(config_costos))).ejecutar(hechos)
        costos = costos_desde_hechos(mina, resultado)
        if args.hasta and not args.desde:
            raise ValueError("--hasta requiere al menos un origen --desde")
        origenes = ([(m.id, m.nodo) for m in escenario.mineros] if escenario
                    else [(None, origen) for origen in args.desde])
        destinos = escenario.destinos if escenario else args.hasta or None
        rutas = [(id, origen, ruta_menor_costo(mina, origen, destinos, costos))
                 for id, origen in origenes]
        rutas_base = []
        if args.comparar or escenario:
            base = costos_linea_base(mina, hechos, cargar_umbrales_co(umbrales)["alerta"])
            rutas_base = [(id, origen, ruta_menor_costo(mina, origen, destinos, base))
                          for id, origen in origenes]
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(f"Mina: {mina.nombre} ({len(mina.nodos)} nodos, {len(mina.aristas)} túneles)")
    print("Simulación académica: no es una evaluación operativa de seguridad.")
    if escenario:
        print(f"Escenario: {escenario.nombre}")
    for paso in resultado.traza:
        print(f"{paso.regla_id} [{paso.entidad}]: {paso.antecedentes} -> {paso.conclusiones}")
    print(f"Disparos: {len(resultado.traza)}")
    if not rutas:
        print("Sin origen --desde: no se calcularon rutas.")
    for etiqueta, recorridos in (("Ruta", rutas), ("Línea base", rutas_base)):
        for id, origen, ruta in recorridos:
            persona = f" [{id}]" if id is not None else ""
            if ruta is None:
                print(f"{etiqueta}{persona} desde {origen}: SIN RUTA a los destinos solicitados")
            else:
                print(f"{etiqueta}{persona} desde {origen}: {' -> '.join(ruta.nodos)}; "
                      f"distancia {ruta.distancia_m:g} m; costo {ruta.costo:g}")


if __name__ == "__main__":
    main()
