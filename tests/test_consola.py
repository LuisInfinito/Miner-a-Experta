"""Ejecuta la consola real, incluida la carga de datos y reglas."""

from pathlib import Path
import subprocess
import sys

import pytest


RAIZ = Path(__file__).resolve().parents[1]


def ejecutar(*argumentos):
    return subprocess.run([sys.executable, "-m", "mina_experta", *argumentos],
                          cwd=RAIZ, capture_output=True, text=True)


def test_demostracion_completa():
    resultado = ejecutar("--co", "tunel_1_2=120", "--co", "tunel_2_3=20")
    assert resultado.returncode == 0, resultado.stderr
    assert "8 nodos, 8 túneles" in resultado.stdout
    assert "Disparos: 3" in resultado.stdout
    assert "('tunel_1_2', 'cerrado', True)" in resultado.stdout
    assert "[tunel_2_3]" not in resultado.stdout
    assert "aún no calcula rutas" in resultado.stdout


@pytest.mark.parametrize("lectura", ["no_existe=120", "tunel_1_2=NaN",
    "tunel_1_2=-1", "tunel_1_2=abc", "sin_igual"])
def test_errores_lectura(lectura):
    resultado = ejecutar("--co", lectura)
    assert resultado.returncode == 2
    assert "Error:" in resultado.stderr
    assert "Traceback" not in resultado.stderr


def test_lectura_duplicada():
    resultado = ejecutar("--co", "tunel_1_2=120", "--co", "tunel_1_2=20")
    assert resultado.returncode == 2
    assert "repetida" in resultado.stderr


def test_archivo_ausente():
    resultado = ejecutar("--mina", "no_existe.json")
    assert resultado.returncode == 2
    assert "No se pudo cargar" in resultado.stderr


def test_eventos_en_consola():
    resultado = ejecutar("--incendio", "tunel_3_4", "--derrumbe", "tunel_4_5")
    assert resultado.returncode == 0, resultado.stderr
    assert "R04 [tunel_3_4]" in resultado.stdout
    assert "R05 [tunel_4_5]" in resultado.stdout
    assert "Disparos: 2" in resultado.stdout


def test_evento_en_tunel_desconocido():
    resultado = ejecutar("--derrumbe", "tunel_ausente")
    assert resultado.returncode == 2
    assert "Túnel desconocido" in resultado.stderr
