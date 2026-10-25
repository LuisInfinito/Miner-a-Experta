"""Consola de mina, inferencia y rutas por costo dinámico."""

import argparse
import math

from .cargador import cargar_mina
from .conocimiento import reglas_co, reglas_eventos, reglas_costos
from .motor import Motor
from .planificador import costos_desde_hechos, ruta_menor_costo


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mina", default="data/mina_prueba.json")
    parser.add_argument("--umbrales", default="data/configuracion/umbrales.json")
    parser.add_argument("--costos", default="data/configuracion/costos.json")
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
        mina = cargar_mina(args.mina)
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
        resultado = Motor((*reglas_co(args.umbrales), *reglas_eventos(),
                           *reglas_costos(args.costos))).ejecutar(hechos)
        costos = costos_desde_hechos(mina, resultado)
        if args.hasta and not args.desde:
            raise ValueError("--hasta requiere al menos un origen --desde")
        rutas = [(origen, ruta_menor_costo(mina, origen, args.hasta or None, costos))
                 for origen in args.desde]
    except (OSError, UnicodeError, ValueError, RuntimeError) as error:
        parser.exit(2, f"Error: {error}\n")
    print(f"Mina: {mina.nombre} ({len(mina.nodos)} nodos, {len(mina.aristas)} túneles)")
    print("Simulación académica: no es una evaluación operativa de seguridad.")
    for paso in resultado.traza:
        print(f"{paso.regla_id} [{paso.entidad}]: {paso.antecedentes} -> {paso.conclusiones}")
    print(f"Disparos: {len(resultado.traza)}")
    if not rutas:
        print("Sin origen --desde: no se calcularon rutas.")
    for origen, ruta in rutas:
        if ruta is None:
            print(f"Ruta desde {origen}: SIN RUTA a los destinos solicitados")
        else:
            print(f"Ruta desde {origen}: {' -> '.join(ruta.nodos)}; "
                  f"distancia {ruta.distancia_m:g} m; costo {ruta.costo:g}")


if __name__ == "__main__":
    main()
